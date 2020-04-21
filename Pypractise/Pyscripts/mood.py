# this program is to tell me what to play song  according to my mood

import webbrowser
import string
import speech_recognition as sr

# obtain audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hello,how are you feeling now ?[Happy,boring ,Relaxed,excited, lazy, sober,  or just to search the web: ]")
    audio = r.listen(source)
