from transformers import pipeline

asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def speech_to_text(audio_path):
    result = asr(audio_path)
    return result["text"]
