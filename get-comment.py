from ollama_util import ask_ollama
from youtube_util import get_live_chat_id, fetch_comments
from obs_util import display_comment
import os
import time
import requests as http
import asyncio
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

# 動画IDとAPIキーの設定


# API URLの準備
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/liveChat/messages"

# メインループ
async def main():
    chat_id = await get_live_chat_id(VIDEO_ID, API_KEY)
    next_page_token = None
    seen = set()

    while True:
        data = await fetch_comments(chat_id, API_KEY, next_page_token)
        for item in data.get("items", []):
            msg = item["snippet"]["displayMessage"]
            msg_id = item["id"]
            author = item["authorDetails"]["displayName"]
            if msg_id not in seen:
                print(f"{author}: {msg}")
                
                # Ollamaで返答を作成
                prompt = f"次のユーザーコメントに親しみを込めてAIとして答えてください：「{author}」さんのコメント『{msg}』"
                ai_reply = ask_ollama(prompt)
                
                # <think>タグを除去して純粋な返答のみを取得
                if "<think>" in ai_reply and "</think>" in ai_reply:
                    ai_reply = ai_reply.split("</think>")[-1].strip()
                
                print(f"AI: {ai_reply}")
                display_comment(ai_reply)
                # Google TTSで音声合成
                from google_tts_util import text_to_speech
                audio_data = text_to_speech(ai_reply)
                # 音声データを直接再生する処理
                import subprocess
                with open("temp.mp3", "wb") as f:
                    f.write(audio_data)
                subprocess.run(["afplay", "temp.mp3"])
                seen.add(msg_id)

        next_page_token = data.get("nextPageToken")
        time.sleep(5)
if __name__ == "__main__":
    asyncio.run(main())
