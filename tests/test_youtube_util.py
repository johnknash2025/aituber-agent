import pytest
import types
import youtube_util

class DummyResponse:
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data

class DummyClient:
    def __init__(self, data):
        self._data = data

    async def get(self, *args, **kwargs):
        return DummyResponse(self._data)

@pytest.mark.asyncio
async def test_get_live_chat_id(monkeypatch):
    dummy = {"items": [{"liveStreamingDetails": {"activeLiveChatId": "chat123"}}]}
    fake_httpx = types.SimpleNamespace(AsyncClient=lambda *args, **kwargs: DummyClient(dummy))
    monkeypatch.setattr(youtube_util, "httpx", fake_httpx)
    chat_id = await youtube_util.get_live_chat_id("vid", "key")
    assert chat_id == "chat123"

@pytest.mark.asyncio
async def test_fetch_comments(monkeypatch):
    dummy = {"items": [1, 2, 3]}
    fake_httpx = types.SimpleNamespace(AsyncClient=lambda *args, **kwargs: DummyClient(dummy))
    monkeypatch.setattr(youtube_util, "httpx", fake_httpx)
    res = await youtube_util.fetch_comments("chatid", "key", page_token="tok")
    assert res == dummy