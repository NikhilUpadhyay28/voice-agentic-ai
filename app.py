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
    import uuid, os
    from speech import speech_to_text, text_to_speech
    from agent import run_agent

    audio = request.files["audio"]
    lang = request.form.get("language", "hi-IN")

    input_path = f"temp/{uuid.uuid4()}.webm"
    audio.save(input_path)

    user_text = speech_to_text(input_path, lang)

    if not user_text:
        reply = {
            "hi-IN": "मैं आपकी आवाज़ समझ नहीं पाया",
            "bn-IN": "আমি আপনার কথা বুঝতে পারিনি",
            "or-IN": "ମୁଁ ଆପଣଙ୍କ କଥା ବୁଝିପାରିଲି ନାହିଁ"
        }.get(lang, "कृपया पुनः बोलें")
    else:
        reply = run_agent(user_text, lang)

    output_path = f"temp/{uuid.uuid4()}.mp3"
    text_to_speech(reply, lang, output_path)

    if not os.path.exists(output_path):
        return "Audio generation failed", 500

    return send_file(output_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
