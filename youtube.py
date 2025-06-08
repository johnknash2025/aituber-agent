
# liveChatId を取得するための関数
def get_live_chat_id():
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={VIDEO_ID}&key={API_KEY}"
    res = http.get(url)
    data = res.json()
    return data["items"][0]["liveStreamingDetails"]["activeLiveChatId"]


# コメント取得
def fetch_comments(chat_id, page_token=None):
    params = {
        "liveChatId": chat_id,
        "part": "snippet,authorDetails",
        "key": API_KEY,
    }
    if page_token:
        params["pageToken"] = page_token
    res = http.get(YOUTUBE_API_URL, params=params)
    return res.json()