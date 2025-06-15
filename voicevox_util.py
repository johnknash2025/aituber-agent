import httpx
import asyncio
import os
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

VOICEVOX_API_URL = os.getenv("VOICEVOX_API_URL")

async def text_to_speech(text, speaker_id=1):
    """
    VoiceVox APIを使用してテキストを音声に変換します。
    
    Parameters:
        text (str): 音声合成するテキスト
        speaker_id (int): 音声を生成する話者ID
    
    Returns:
        bytes: 音声データ
    """
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        # 音声合成のリクエスト
        response = await client.post(
            f"{VOICEVOX_API_URL}/audio_query",
            params={"text": text, "speaker": speaker_id}
        )
        response.raise_for_status()
        audio_query = response.json()

        # 音声データの取得
        response = await client.post(
            f"{VOICEVOX_API_URL}/synthesis",
            params={"text": text, "speaker": speaker_id},
            json=audio_query
        )
        response.raise_for_status()
        return response.content
