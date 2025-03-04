from googletrans import Translator

from flask import Flask, request, jsonify 
from googletrans import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data['text']
    src_lang = data['src_lang']
    target_langs = data['target_langs']  # Updated to accept multiple target languages

    
    translator = Translator()
    translations = []
    for target_lang in target_langs:  # Loop through each target language
        translation = translator.translate(text, src=src_lang, dest=target_lang)
        translations.append(translation.text)
    return jsonify({'translated_texts': translations})  # Updated to return multiple translations



def main():
    print("Welcome to the Language Translation Tool!")
    text = input("Enter the text to translate: ")
    src_lang = input("Enter the source language (e.g., 'en' for English): ")
    target_langs = input("Enter the target languages (comma-separated, e.g., 'es,ta,hi'): ").split(",")  # Updated for multiple languages

    
    translated_texts = translate_text(text, src_lang, target_langs)  # Updated to handle multiple languages
    print(f"Translated texts: {translated_texts}")


if __name__ == "__main__":
    app.run(debug=True)
