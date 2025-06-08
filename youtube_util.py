
# liveChatId を取得するための関数

import requests as http

def get_live_chat_id(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={video_id}&key={api_key}"
    res = http.get(url)
    data = res.json()
    return data["items"][0]["liveStreamingDetails"]["activeLiveChatId"]

# コメント取得
def fetch_comments(chat_id, api_key, page_token=None):
    params = {
        "liveChatId": chat_id,
        "part": "snippet,authorDetails",
        "key": api_key,
    }
    if page_token:
        params["pageToken"] = page_token
    res = http.get("https://www.googleapis.com/youtube/v3/liveChat/messages", params=params)
    return res.json()