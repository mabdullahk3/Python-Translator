from googletrans import Translator

def get_language_code(language):
    language_codes = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Italian': 'it',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Chinese': 'zh-CN',
        'Russian': 'ru',
        'Arabic': 'ar',
        'Portuguese': 'pt',
        'Bengali': 'bn',
        'Dutch': 'nl',
        'Turkish': 'tr',
        'Swedish': 'sv',
        'Danish': 'da',
        'Finnish': 'fi',
        'Norwegian': 'no',
        'Greek': 'el',
        'Urdu': 'ur'
    }
    return language_codes.get(language, 'Invalid language')

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

def main():
    print("Welcome to Translator!")
    languages = ['English','Spanish','French','German','Italian','Japanese','Korean','Chinese','Russian','Arabic','Portuguese','Bengali','Dutch','Turkish','Swedish','Danish','Finnish','Norwegian','Greek','Urdu']
    text = input("Enter text to translate: ")
    print("The available languages are:")
    for idx, lang in enumerate(languages, start=1):
        print(f"{idx}. {lang}")

    src_lang_name = input("Enter source language: ")
    while src_lang_name not in languages:
        src_lang_name = input("Re-enter source language: ")

    dest_lang_name = input("Enter destination language: ")
    while dest_lang_name not in languages:
        dest_lang_name = input("Re-enter destination language: ")

    src_lang = get_language_code(src_lang_name)
    dest_lang = get_language_code(dest_lang_name)

    if src_lang == 'Invalid language' or dest_lang == 'Invalid language':
        print("Invalid source or destination language.")
    else:
        translated_text = translate_text(text, src_lang, dest_lang)
        print(f"Translated text: {translated_text}")


if __name__ == "__main__":
    main()