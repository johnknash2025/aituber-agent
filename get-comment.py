import os
import time
import requests as http
from dotenv import load_dotenv
from obswebsocket import obsws, requests

# .env 読み込み
load_dotenv()

# OBS設定
host = os.getenv("OBS_HOST", "localhost")
port = int(os.getenv("OBS_PORT", 4455))
password = os.getenv("OBS_PASSWORD")

# YouTube設定
API_KEY = os.getenv("YOUTUBE_API_KEY")
VIDEO_ID = os.getenv("YOUTUBE_VIDEO_ID")

# API URLの準備
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/liveChat/messages"

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

# メインループ
def main():
    chat_id = get_live_chat_id()
    next_page_token = None
    seen = set()

    while True:
        data = fetch_comments(chat_id, next_page_token)
        for item in data.get("items", []):
            msg = item["snippet"]["displayMessage"]
            msg_id = item["id"]
            if msg_id not in seen:
                print("新コメント:", msg)
                display_comment(msg)
                seen.add(msg_id)
        next_page_token = data.get("nextPageToken")
        time.sleep(5)

if __name__ == "__main__":
    main()