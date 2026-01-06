import speech_recognition as sr
import subprocess
import os
from gtts import gTTS


def convert_to_pcm(input_path):
    output_path = "temp/converted.wav"
    subprocess.run([
        "ffmpeg", "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path


def speech_to_text(audio_path, lang_code):
    recognizer = sr.Recognizer()

    pcm_audio = convert_to_pcm(audio_path)

    with sr.AudioFile(pcm_audio) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio, language=lang_code)
    except:
        return None


def text_to_speech(text, lang_code, out_path):
    from gtts import gTTS

    if not text or len(text.strip()) == 0:
        text = "मैं आपकी सहायता के लिए यहाँ हूँ"

    # Proper language mapping
    lang_map = {
        "hi-IN": "hi",
        "bn-IN": "bn",
        "or-IN": "or"
    }

    tts_lang = lang_map.get(lang_code, "hi")

    try:
        # Primary attempt: native voice
        gTTS(text=text, lang=tts_lang).save(out_path)
    except Exception as e:
        # Fallback (never fail silently)
        print("TTS failed for", tts_lang, "falling back to Hindi")
        gTTS(text=text, lang="hi").save(out_path)
