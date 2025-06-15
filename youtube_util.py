
# liveChatId を取得するための関数

import httpx
import asyncio

async def get_live_chat_id(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={video_id}&key={api_key}"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    data = res.json()
    return data["items"][0]["liveStreamingDetails"]["activeLiveChatId"]

# コメント取得
async def fetch_comments(chat_id, api_key, page_token=None):
    params = {
        "liveChatId": chat_id,
        "part": "snippet,authorDetails",
        "key": api_key,
    }
    if page_token:
        params["pageToken"] = page_token
    async with httpx.AsyncClient() as client:
        res = await client.get("https://www.googleapis.com/youtube/v3/liveChat/messages", params=params)
    return res.json()
