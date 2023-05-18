from googletrans import Translator
import unidecode

def translate_text(text, target_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=target_language).text
    translation = unidecode.unidecode(translation)
    return translation

# Example usage
input_text = input("Enter text to translate: ")
target_language = input("Enter target language: ")

translated_text = translate_text(input_text, target_language)
print(f"Translated text: {translated_text}")





