# OBSにコメントを表示
def display_comment(text):
    try:
        ws = obsws(host, port, password)
        ws.connect()
        ws.call(requests.SetInputSettings(
            inputName="AIコメント",
            inputSettings={"text": text},
            overlay=True
        ))
        ws.disconnect()
    except Exception as e:
        print("OBS送信エラー:", e)
