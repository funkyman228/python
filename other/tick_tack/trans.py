from googletrans import Translator
from gtts import gTTS
import os
import vlc
import sys

translator = Translator()
stop = 0

def stopcheck():
    if text == "stop":
        sys.exit()

while stop != "stop":
    translated_text = None
    detranslated_text = None
    os.system('cls')
    print("Enter text =")
    text = input()
    stopcheck()
    translated_text = translator.translate(text, dest='ja').text
    print(translated_text)
    detranslated_text = translator.translate(translated_text, dest='en').text
    print(detranslated_text)
    myobj = gTTS(text=detranslated_text, lang='en', slow=False)
    myobj.save("temp.mp3")
    p = vlc.MediaPlayer("temp.mp3")
    p.play()
    stop = input()
    p.stop()
    try:
        os.remove("temp.mp3")
    except FileNotFoundError:
        print("Error: The file could not be found.")
        input()

