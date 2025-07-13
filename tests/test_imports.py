import importlib
import sys
import types
import pytest

MODULES = [
    "main",
    "google_tts_util",
    "obs_util",
    "ollama_util",
    "voicevox_util",
    "youtube_util",
]

@pytest.mark.parametrize("module_name", MODULES)
def test_import(module_name, monkeypatch):
    if module_name == "google_tts_util":
        fake_mod = types.ModuleType("google.cloud.texttospeech")
        fake_mod.TextToSpeechClient = lambda *args, **kwargs: None
        fake_mod.SynthesisInput = lambda text: None
        fake_mod.VoiceSelectionParams = lambda **kwargs: None
        fake_mod.AudioConfig = lambda **kwargs: None
        fake_mod.AudioEncoding = types.SimpleNamespace(MP3=None)
        fake_mod.SsmlVoiceGender = types.SimpleNamespace(NEUTRAL=None)
        pkg_google = types.ModuleType("google")
        pkg_cloud = types.ModuleType("google.cloud")
        sys.modules["google"] = pkg_google
        sys.modules["google.cloud"] = pkg_cloud
        sys.modules["google.cloud.texttospeech"] = fake_mod
    if module_name == "obs_util":
        fake_obsws = lambda host, port, password: types.SimpleNamespace(
            connect=lambda: None,
            call=lambda *args, **kwargs: None,
            disconnect=lambda: None
        )
        fake_requests = types.SimpleNamespace(SetInputSettings=lambda **kwargs: None)
        pkg = types.ModuleType("obswebsocket")
        pkg.obsws = fake_obsws
        pkg.requests = fake_requests
        sys.modules["obswebsocket"] = pkg
    importlib.reload(importlib.import_module(module_name))
