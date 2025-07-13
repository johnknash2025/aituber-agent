import types
import ollama_util

class DummyResponse:
    def __init__(self, status, data):
        self._status = status
        self._data = data

    def json(self):
        return self._data

    def raise_for_status(self):
        if self._status != 200:
            raise Exception("error")

def test_ask_ollama_success(monkeypatch):
    dummy = DummyResponse(200, {"response": " OK "})
    fake_http = types.SimpleNamespace(post=lambda *args, **kwargs: dummy)
    monkeypatch.setattr(ollama_util, "http", fake_http)
    assert ollama_util.ask_ollama("prompt") == "OK"

def test_ask_ollama_failure(monkeypatch):
    fake_http = types.SimpleNamespace(post=lambda *args, **kwargs: (_ for _ in ()).throw(Exception("fail")))
    monkeypatch.setattr(ollama_util, "http", fake_http)
    ret = ollama_util.ask_ollama("prompt")
    assert "すみません" in ret
