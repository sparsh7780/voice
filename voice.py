# Code for virtual assistant with GUI
import tkinter
from tkinter import *
import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser,datetime
import playsound,pyautogui
import os
import random
from gtts import gTTS
from PIL import ImageTk,Image
from os import system as s
import pywhatkit as kt

def greet():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        lee_voice("A very Good Morning to you")
    elif hour>=12 and hour<18:
        lee_voice("Good Afternoon Everyone!")
    elif hour>18 and hour<21:
        lee_voice("Good Evening!")
    else:
        lee_voice("Hope you had a great day sir.")
    #speak("I am jarvis sir. How may I help you.")

#print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()



def record_audio(ask = False):
#user voice record
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :'+ voice_data)
        except Exception:
            #print('Oops something went Wrong')
            lee_voice('Oops something went Wrong')
        return voice_data


def lee_voice(audio_string):
    #Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# greet()    

def gen():
    for i in range(1,1001):
        yield i
g=gen()

def reg():
    global name
    name=record_audio("Whats your good name")
    lee_voice("Welcome to voice assistant"+name)


class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS GIVEN
    def __init__(self):
        root = Tk()
        root.title('Heisenberg')
        p1 = PhotoImage('Heisenberg.ico')
  
# Setting icon of master window
        # root.iconphoto(False, p1)
        root.geometry('900x820')

        # img = PhotoImage(file="Heisenberg.jpg")
        img = tkinter.PhotoImage(file='practice/Heisenberg.jpg'); 
        # img = subsample(2)
        # backImg = Label(screen, image=img).place(x=50,y=50)
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Heisenberg', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        # compFrame = LabelFrame(root, text="Lena", font=('Railways',10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        greet() 
        reg()
        lee_voice('How can i help you?')
        root.mainloop()
        

    def clicked(self):
        #BUTTON CALLING
        print("Listening...")

        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            lee_voice('My name is Leena')
        if 'open vs code' in voice_data :
            codepath=r"C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        if 'search for me' in voice_data:
            target1 = record_audio('what do you want to search')
            kt.search(target1)
            lee_voice('Here is what i found for you as ' + target1)
        if 'toss a coin' in voice_data :
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            #playsound.playsound('quarter spin flac.mp3')
            lee_voice("It's " + cmove)
        if 'open notepad' in voice_data:
            lee_voice("opening Notepad")
            s("Notepad")
        if 'open chrome' in voice_data:
            lee_voice("opening chrome")
            webbrowser.get().open("https://www.google.com")
        
        if 'open youtube' in voice_data:
            webbrowser.get().open("https://www.youtube.com")
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location' + location)

        if 'play some music' in voice_data:
            song = record_audio('tell me the song name')
            url = 'https://www.youtube.com/results?search_query=' + song 
            webbrowser.get().open(url)
            lee_voice('Here is your song ' + song)

        if 'what is the time' in voice_data:
            lee_voice(+name+"the time is :" + ctime())
        if 'what is the date' in voice_data:
            strDay=datetime.date.today().strftime("%B %d, %Y")
            lee_voice(f"Today is {strDay}")
        if 'exit' in voice_data:
            lee_voice('Thanks have a good day '+name)
            quit()


if __name__== '__main__':
    widget = Widget()
time.sleep(1)
while 1:
    voice_data = record_audio()
    #respond(voice_data)

speaker.runAndWait()