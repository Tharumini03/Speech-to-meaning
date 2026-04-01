# 🎙️ Speech-to-Meaning Translator

Convert speech to text, enhance it with AI, and translate into 60+ languages - all in real-time!

## 🌟 What it Does

1. **Speak** in your language → 2. **AI cleans up** the text → 3. **Translate** to any language

## ✨ Features

- 🎤 Speech recognition in 60+ languages
- ✍️ Automatic grammar correction
- 🌍 Translate to 60+ languages
- 💎 Beautiful modern interface
- 📱 Works on mobile & desktop
- 🆓 100% Free (no API keys needed)

## 🚀 Quick Start

### Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser
http://localhost:5000
```

### Deploy Online (Free)

1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload your files
3. Install dependencies: `pip3 install --user -r requirements.txt`
4. Create Flask web app
5. Done! Your site is live 🎉

## 📁 Files

```
speech-translator/
├── app.py              # Backend (Flask)
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html     # Frontend HTML
└── static/
    ├── css/
    │   └── style.css  # Styling
    └── js/
        └── main.js    # JavaScript
```

## 🎯 How to Use

1. Select your **input language** (what you'll speak)
2. Select your **output language** (translation target)
3. Click **"Start Recording"** and speak
4. Click **"Stop Recording"**
5. View your **translation**!

## 🌐 Supported Languages

60+ languages including:
- English, Spanish, French, German, Italian, Portuguese
- Chinese, Japanese, Korean, Arabic, Hindi, Bengali
- Vietnamese, Sinhala, Thai, Indonesian, Malay, Filipino
- And many more!

## 🛠️ Built With

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Translation**: Google Translate API (free)
- **Speech**: Web Speech API (browser built-in)

## 📝 Requirements

- Python 3.8+
- Modern browser (Chrome recommended)
- Internet connection

## 🐛 Common Issues

**Speech not working?**
- Use Chrome browser
- Allow microphone permissions
- Make sure you're on HTTPS

**Translation failed?**
- Check internet connection
- Verify language codes