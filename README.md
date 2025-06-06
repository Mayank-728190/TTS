# 🗣️ Responsive Text-to-Speech (TTS) Web App

A modern, production-ready Text-to-Speech (TTS) web application that converts text to natural-sounding speech using OpenAI’s TTS API.  
Supports **Hindi, Indian English, and Hinglish** with automatic language/voice detection, a beautiful single-page web UI, and fast, secure deployment.

---

## 🌟 Features

- **OpenAI TTS:** Leverages OpenAI’s cutting-edge API for premium voice quality.
- **Automatic Language Detection:** No user selection needed—handles Hindi, Indian English, and Hinglish.
- **Voice Variety:**  
  - English (male voice)  
  - Hindi (female voice)  
  - Hinglish (female Indian-accented voice)
- **Streaming Audio Output:** Immediate playback and download in browser.
- **Single-Page UI:** Clean, responsive, easy-to-use HTML frontend.
- **Secure:** API key is never exposed or committed to code.
- **Ready for Production:** Deployable to Vercel, Render, Railway, etc.

---

## 🚀 Demo

**[Try Live (after you deploy!)](https://your-app-url.vercel.app/)**

---

## ⚙️ Setup & Local Run

1. **Clone the repo and enter directory:**
    ```bash
    git clone https://github.com/yourusername/your-tts-app.git
    cd your-tts-app
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate          # On Windows
    # source venv/bin/activate     # On macOS/Linux
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**  
   Create a file named `.env` (in the project root) with:
    ```
    OPENAI_API_KEY=sk-...your-openai-api-key...
    ```

5. **Run the backend:**
    ```bash
    python app.py
    ```
    The app will be live at [http://localhost:8000/](http://localhost:8000/).

6. **Use the app:**  
   Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## 🌐 Deployment (Vercel Example)

1. **Push to GitHub** (do NOT push `.env`—it’s in `.gitignore`)
2. **On [vercel.com](https://vercel.com/import):**
   - Import your repo.
   - Set environment variable `OPENAI_API_KEY` in the Vercel dashboard.
   - Deploy!
3. **Your app is live at:**  
   `https://your-app-name.vercel.app/`

---

## 🎤 API Usage Example

**POST** `/speak`
```json
{ "text": "Namaste! How are you? आप कैसे हैं?" }
