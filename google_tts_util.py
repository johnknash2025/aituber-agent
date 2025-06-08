import os
from google.cloud import texttospeech
from dotenv import load_dotenv

load_dotenv()

# サービスアカウントキーのパスを設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/keigofukumoto/Documents/feisty-return-462205-n8-b7cdd423b72d.json"

def text_to_speech(text, language_code="ja-JP"):
    """Google Cloud Text-to-Speechでテキストを音声に変換"""
    client = texttospeech.TextToSpeechClient()
    
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    
    return response.audio_content
