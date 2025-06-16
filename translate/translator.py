from deep_translator import GoogleTranslator

def translate_text(text, dest_lang="iw"):
    return GoogleTranslator(source="auto", target=dest_lang).translate(text)

