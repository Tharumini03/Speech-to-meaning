# 🎙️ Speech-to-Meaning Translator
 
A real-time speech recognition and translation web app. Speak in your language, get clean text, and instantly translate it into 60+ languages — no API keys required.
 
---
 
## ✨ Features
 
- 🎤 Speech recognition in 60+ languages via the browser's built-in Web Speech API
- ✍️ Automatic text cleanup — capitalization, punctuation, spacing
- 🌍 Translation to 60+ languages powered by Google Translate (free, no key needed)
- 📱 Responsive design — works on desktop and mobile
- ⚡ Fast and lightweight — no heavy frameworks or paid services
 
---
 
## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Speech Recognition | Web Speech API (browser built-in) |
| Translation | Google Translate unofficial API |
| Deployment | Vercel |
 
---
 
## 📁 Project Structure
 
```
speech-to-meaning/
├── app.py                  # Flask backend — routes and translation logic
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
├── api/
│   └── index.py            # Vercel serverless entry point
├── templates/
│   └── index.html          # Main frontend page
└── static/
    ├── css/
    │   └── style.css       # Stylesheet
    └── js/
        └── main.js         # Speech and UI logic
```
 
---
 
## 🚀 Running Locally
 
```bash
# 1. Install dependencies
pip install -r requirements.txt
 
# 2. Start the app
python app.py
 
# 3. Open in browser
http://localhost:5000
```
 
> Use **Chrome** for best speech recognition support.
 
---
 
## ☁️ Deploying to Vercel
 
### Prerequisites
- A [GitHub](https://github.com) account
- A [Vercel](https://vercel.com) account (free — sign up with GitHub)
 
### Step 1 — Add Vercel config files
 
Create `vercel.json` in the root folder:
 
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```
 
Create `api/index.py`:
 
```python
from app import app
 
handler = app
```
 
### Step 2 — Push to GitHub
 
Upload all project files to a new GitHub repository. Do **not** include the `venv/` folder.
 
### Step 3 — Import to Vercel
 
1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Leave all settings as default
4. Click **Deploy**
 
Your app will be live at `https://your-project-name.vercel.app` within 1–2 minutes.
 
> Vercel provides HTTPS automatically, which is required for the Web Speech API to work.
 
---
 
## 🎯 How to Use
 
1. Select your **input language** (the language you will speak)
2. Select your **output language** (the translation target)
3. Click **Start Recording** and speak
4. Click **Stop Recording**
5. Your cleaned-up text and translation will appear instantly
 
---
 
## 🌐 Supported Languages
 
60+ languages including English, Spanish, French, German, Portuguese, Arabic, Hindi, Chinese, Japanese, Korean, Vietnamese, Sinhala, Thai, Indonesian, Bengali, Filipino, and more.
 
---
 
## 🐛 Troubleshooting
 
**Microphone not working**
- Use Chrome (Firefox and Safari have limited Web Speech API support)
- Allow microphone permissions when prompted
- Make sure the page is served over HTTPS
 
**Translation shows `[Translation failed]`**
- Check your internet connection
- The Google Translate unofficial API may occasionally rate-limit — wait a moment and try again
 
**Vercel deployment fails**
- Ensure `requirements.txt` is in the root directory
- Ensure `vercel.json` routes are configured exactly as shown above
- Make sure `api/index.py` exists and imports `from app import app`
 
---
 
## 📝 License
 
This project is open source and free to use.