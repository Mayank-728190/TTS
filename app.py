from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
from langdetect import detect

# Load environment variables from .env
load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "unknown"

def is_hinglish(text):
    # Simple: If text contains both Devanagari and English characters, treat as Hinglish
    import re
    devnag = re.search(r'[\u0900-\u097F]', text)
    latin = re.search(r'[a-zA-Z]', text)
    if devnag and latin:
        return True
    # Optional: treat as Hinglish if English words but common Hindi vocab present
    hindi_words = ["kaise", "hai", "hai?", "kya", "aap", "namaste", "theek", "haan", "nahi", "kyun", "kyunki", "par", "aur", "bhi", "mein", "main"]
    for word in hindi_words:
        if word in text.lower():
            return True
    return False

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "Please provide text."}), 400

    # Detect language
    lang = detect_language(text)
    # Decide voice
    if lang == "en":
        if is_hinglish(text):
            voice = "shimmer"  # Female, good for Hinglish
        else:
            voice = "echo"     # Male, best for English
    elif lang == "hi":
        voice = "nova"         # Female, best for Hindi
    else:
        # If can't detect, default to shimmer (female)
        voice = "shimmer"

    model = "tts-1"

    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        def generate():
            for chunk in response.iter_bytes(chunk_size=4096):
                yield chunk
        return Response(generate(), mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve the UI at /
@app.route("/", methods=["GET"])
def serve_home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
