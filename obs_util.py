import os
from dotenv import load_dotenv
from obswebsocket import obsws, requests
# 環境変数を読み込む
load_dotenv()

# OBSにコメントを表示
def display_comment(comment, host="localhost", port=4455, password=""):
    try:
        host = os.getenv("OBS_HOST", "localhost")
        port = int(os.getenv("OBS_PORT", 4455))
        password = os.getenv("OBS_PASSWORD", "")

        ws = obsws(host, port, password)
        ws.connect()
        ws.call(requests.SetInputSettings(
          inputName="AIコメント",
          inputSettings={"text": comment},
          overlay=True
       ))
        ws.disconnect()
    except Exception as e:
        print("OBS送信エラー:", e)
