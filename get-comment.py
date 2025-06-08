from ollama_util import ask_ollama
from youtube_util import get_live_chat_id, fetch_comments
from obs_util import display_comment
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

# メインループ
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
            author = item["authorDetails"]["displayName"]
            if msg_id not in seen:
                print(f"{author}: {msg}")
                
                # Ollamaで返答を作成
                prompt = f"次のユーザーコメントに親しみを込めてAIとして答えてください：「{author}」さんのコメント『{msg}』"
                ai_reply = ask_ollama(prompt)

                print(f"AI: {ai_reply}")
                display_comment(ai_reply)
                seen.add(msg_id)

        next_page_token = data.get("nextPageToken")
        time.sleep(5)
if __name__ == "__main__":
    main()