from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

# Example usage
input_text = input("Enter text to translate: ")
target_language = input("Enter target language: ")

translated_text = translate_text(input_text, target_language)
print(f"Translated text: {translated_text}")