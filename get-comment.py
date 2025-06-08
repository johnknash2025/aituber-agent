from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()

host = os.getenv("OBS_HOST", "localhost")
port = int(os.getenv("OBS_PORT", 4455))
password = os.getenv("OBS_PASSWORD")

text = sys.argv[1] if len(sys.argv) > 1 else "こんにちは！AIからの返事です。"

ws = obsws(host, port, password)

try:
    ws.connect()
    ws.call(requests.SetInputSettings(
        inputName="AIコメント",
        inputSettings={"text": text},
        overlay=True
    ))
    print("表示完了")
except Exception as e:
    print(f"エラー: {e}")
finally:
    ws.disconnect()