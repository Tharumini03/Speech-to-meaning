"""
Test script for FREE Google Translate version
NO API KEY NEEDED!
"""

import requests

print("=" * 70)
print("Google Translate Test (FREE - No API Key Needed!)")
print("=" * 70)

def test_translation(text, source_lang, target_lang):
    """Test Google Translate"""
    
    print(f"\n🔄 Testing translation...")
    print(f"   Text: '{text}'")
    print(f"   From: {source_lang}")
    print(f"   To: {target_lang}")
    print(f"   ---")
    
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        
        params = {
            "client": "gtx",
            "sl": source_lang,
            "tl": target_lang,
            "dt": "t",
            "q": text
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        
        print("   Sending request to Google Translate...")
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Extract translation
        translated_text = ""
        if result and len(result) > 0 and result[0]:
            for item in result[0]:
                if item and len(item) > 0:
                    translated_text += item[0]
        
        print(f"✅ SUCCESS!")
        print(f"   Translation: '{translated_text}'")
        return translated_text
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None

# Test 1: English to Vietnamese
test_translation(
    text="Hello, how are you today?",
    source_lang="en",
    target_lang="vi"
)

# Test 2: English to Sinhala
test_translation(
    text="Good morning, my friend.",
    source_lang="en",
    target_lang="si"
)

# Test 3: English to French
test_translation(
    text="Thank you very much.",
    source_lang="en",
    target_lang="fr"
)

print("\n" + "=" * 70)
print("Testing complete!")
print("=" * 70)
print("\n✅ If all tests passed, your app will work with NO API KEY!")
print("   Just use app_free_google.py instead of app.py")