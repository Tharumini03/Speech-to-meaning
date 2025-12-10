from flask import Flask, render_template, request, jsonify
import re
import os
import requests

# Create the Flask application object
app = Flask(__name__)


def clean_and_improve(text: str) -> str:
    """Clean spaces, capitalize first letter, add final punctuation."""
    text = text.strip()
    # Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text)

    if text:
        # Capitalize first letter if not already
        if not text[0].isupper():
            text = text[0].upper() + text[1:]

        # Add period if missing punctuation at the end
        if text[-1] not in ".?!":
            text += "."

    return text


def translate_with_google(text: str, source_lang: str, target_lang: str) -> str:
    """
    Use Google Translate (unofficial API - completely FREE, no API key needed!)
    
    Args:
        text: The text to translate
        source_lang: Source language code (e.g., 'en', 'si', 'vi')
        target_lang: Target language code (e.g., 'en', 'si', 'vi')
    
    Returns:
        Translated text string
    """
    # Safety: if source == target, just return original
    if source_lang == target_lang:
        return text

    try:
        # Google Translate unofficial API endpoint
        url = "https://translate.googleapis.com/translate_a/single"
        
        params = {
            "client": "gtx",
            "sl": source_lang,      # source language
            "tl": target_lang,      # target language
            "dt": "t",              # return translation
            "q": text               # text to translate
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        
        # Make the API call
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse the response
        # Google returns a nested array structure
        result = response.json()
        
        # Extract translated text from the complex structure
        translated_text = ""
        if result and len(result) > 0 and result[0]:
            for item in result[0]:
                if item and len(item) > 0:
                    translated_text += item[0]
        
        return translated_text if translated_text else text

    except requests.exceptions.Timeout:
        print("Google Translate timeout")
        return f"[Translation timeout] {text}"
    
    except requests.exceptions.RequestException as e:
        # Log error for debugging
        print(f"Google Translate error: {e}")
        return f"[Translation failed] {text}"
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        return f"[Translation error] {text}"


# Define a route (URL) for the home page
@app.route("/")
def home():
    # This will look for templates/index.html and return it
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """
    Process the speech input:
    1. Receive raw text from frontend
    2. Clean and improve it
    3. Translate to target language using Google Translate (FREE!)
    """
    data = request.get_json()
    text = data.get("text", "")
    input_lang = data.get("input_lang", "en-US")  # from browser (e.g., "en-US")
    output_lang = data.get("output_lang", "en")   # from dropdown (e.g., "en", "si", "vi")

    # 1) Clean / improve the text
    improved = clean_and_improve(text)

    # 2) Extract source language code from input_lang (e.g., "en-US" -> "en")
    source_lang_code = input_lang.split("-")[0]
    
    # 3) Translate using Google Translate (FREE!)
    translated = translate_with_google(improved, source_lang_code, output_lang)

    # 4) Return results to frontend
    return jsonify({
        "improved_text": improved,
        "translated_text": translated
    })


# Only run the server if this file is executed directly
if __name__ == "__main__":
    # Run on port 5000 by default
    app.run(debug=True, port=5000)