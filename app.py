from flask import Flask, request, send_file
import os, uuid

from speech import speech_to_text, text_to_speech
from agent import run_agent

app = Flask(__name__)

@app.route("/")
def home():
    return open("static/index.html").read()

@app.route("/process", methods=["POST"])
def process():
    from speech import speech_to_text, text_to_speech
    from agent import run_agent
    import uuid, os

    audio = request.files["audio"]
    lang = request.form["language"]

    input_path = f"temp/{uuid.uuid4()}.webm"
    audio.save(input_path)
    print("Saved input audio:", input_path)

    user_text = speech_to_text(input_path, lang)
    print("STT OUTPUT:", user_text)

    if not user_text:
        reply = "मैं आपकी आवाज़ समझ नहीं पाया"
    else:
        reply = run_agent(user_text, lang)

    output_path = f"temp/{uuid.uuid4()}.mp3"
    print("Generating TTS at:", output_path)

    text_to_speech(reply, lang, output_path)

    print("Checking file exists:", os.path.exists(output_path))

    return send_file(output_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
