import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
version=os.environ['version']
#print(apikey)

authenticator = IAMAuthenticator(str(apikey))
language_translator = LanguageTranslatorV3(
    version=str(version),
    authenticator=authenticator
)

language_translator.set_service_url(str(url))

#language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    #write the code here
    if english_text=="": 
        return ""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print(type(translation))#, indent=2, ensure_ascii=False)) dict
    french_text = translation["translations"][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    if french_text=="":
        return ""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    english_text = translation["translations"][0]['translation']
    return english_text
