import speech_recognition as sr
from pyttsx3 import speak as sp
from os import system as s

while True:
    a=sr.Recognizer()
    with sr.Microphone() as src:
        print("mircophone listening.......")
        audio=a.listen(src)
        query=a.recognize_google(audio,language="en-in")
        print(f"user said : {query}")
        sp("Welcome to mini alexa")
        if ("notepad" in query) or ("Notepad" in query) and ("open" in query):
            sp("opening notepad")
            s("notepad")
        elif ("explorer" in query) or ("Explorer" in query) and ("open" in query):
            sp("opening explorer")
            s("Explorer")
        elif "quit" in query or "close" in query  or "stop" in query or "Close" in query:
            sp("bye alexa")
            break
        else:
            sp("i do not understand")
