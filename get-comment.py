from obswebsocket import obsws, requests

# OBSのWebSocket設定
host = "localhost"
port = 4455
password = "あなたが設定したパスワード"

# 接続
ws = obsws(host, port, password)
ws.connect()

# ソースを更新（例：「AIコメント」というソースに文字を表示）
response = ws.call(requests.SetInputSettings(
    inputName="AIコメント",
    inputSettings={"text": "こんにちは！AIからの返事です。"},
    overlay=True
))

print("表示完了")
ws.disconnect()