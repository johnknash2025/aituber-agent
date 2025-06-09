# It's assumed that `obsws`, `requests` (from obswebsocket),
# `host`, `port`, and `password` are defined or imported elsewhere
# in the actual execution environment (e.g. in get-comment.py).

def sanitize_for_obs(text: str, max_length: int = 200) -> str:
    """
    Sanitizes text for display in OBS.
    - Ensures input is a string.
    - Replaces newline and tab characters with spaces.
    - Truncates the text to max_length.
    """
    if not isinstance(text, str):
        text = str(text) # Attempt to convert non-string input to string

    text = text.replace('\n', ' ').replace('\t', ' ')

    if len(text) > max_length:
        text = text[:max_length]
    return text

# OBSにコメントを表示
def display_comment(text):
    try:
        sanitized_text = sanitize_for_obs(text)
        # The following variables (host, port, password, obsws, requests)
        # are expected to be available in the global scope when this function is called.
        # This is often the case if obs.py is part of a larger script that defines them.
        ws = obsws(host, port, password)
        ws.connect()
        ws.call(requests.SetInputSettings(
            inputName="AIコメント",
            inputSettings={"text": sanitized_text}, # Use sanitized text
            overlay=True
        ))
        ws.disconnect()
    except Exception as e:
        print("OBS送信エラー:", e)
