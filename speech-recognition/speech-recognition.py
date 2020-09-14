import speech_recognition as sr
from googletrans import Translator

def main():
    phrase = speech_recognition()
    translate(phrase)

LANGUAGES = {
    'af': 'afrikaans',
    'ar': 'arabic',
    'hy': 'armenian',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'de': 'german',
    'el': 'greek',
    'haw': 'hawaiian',
    'hi': 'hindi',
    'hu': 'hungarian',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'kk': 'kazakh',
    'ko': 'korean',
    'lo': 'lao',
    'la': 'latin',
    'ms': 'malay',
    'mi': 'maori',
    'mn': 'mongolian',
    'ne': 'nepali',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ru': 'russian',
    'sm': 'samoan',
    'sr': 'serbian',
    'sd': 'sindhi',
    'sk': 'slovak',
    'so': 'somali',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'vi': 'vietnamese',
    'yi': 'yiddish',
    'zu': 'zulu',
}

def speech_recognition():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        
        try:
            # using google speech recognition
            print("English: " + r.recognize_google(audio_text))
            phrase = r.recognize_google(audio_text)
        except:
             print("Sorry, I did not get that")

    return phrase

def translate(phrase):
    translator = Translator()

    for language in LANGUAGES.values():
        translated_phrase = translator.translate(phrase, dest=language) 
        print(language + ": "+ translated_phrase.text) 


main()
