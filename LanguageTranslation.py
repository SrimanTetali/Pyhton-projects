from googletrans import Translator

# Initialize the Google Translate API translator
translator = Translator()

# Input source language, destination language, and text to be translated
src = input('Enter the source language code (e.g., en for English): ')
dest = input('Enter the destination language code (e.g., te for Telugu): ')
src_text = input("Enter the text to translate: ")

# Translate the text
translation = translator.translate(src_text, src=src, dest=dest)

# Display the translated text
print(f"Translated text: {translation.text}")
