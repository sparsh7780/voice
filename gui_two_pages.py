 # shortcuts GUI MENU   

# GUI program
#pip install pyttsx3
#ip install tkinter
#pip install os

from tkinter import *
from os import system as s
#from pyttsx3 import speak as sp
# import speech_recognition as sr

root = Tk()

root.title("IVR GUI MENU")

root.geometry("480x700")  # height=700  , width=480


def gui_win():
    
    a=Toplevel()
    a.title("2nd page")
    
    
    def openn():
        sp("Opening Notepad")
        s("notepad")

    def opengc():
        sp("Opening Google Chrome")
        s("start chrome")

    def opengg():
        sp("Opening  Gmail")
        s("start https://www.gmail.com/")

    def openb():
        sp("Opening Brave Browser")
        s("start brave")

    def openyt():
        sp("Opening Youtube")
        #s("cd desktop")
        s("start https://www.youtube.com/")

    def openc():
        sp("Opening calculator")
        s("calc")

    def openo():
        sp("Opening Microsoft office")
        s("start winword")



    a.iconbitmap(r"C:\Users\ASUS\Downloads\menu_icon.ico")

    l1 = Label(a,text="Welcome to IVR GUI MENU",font=("Times New Roman",28,"bold"),fg="orange",bg="black")
    l1.pack(fill=X,pady=10)

    # padding is used here for padding(spacing) from y-axis or x-axis

    b1 = Button(a,text="Notepad",width=8,relief=SOLID,font=("Times New Roman",24,"bold"),command=openn)
    b1.pack(pady=5)

    b2 = Button(a,text="Google Chrome",width=12,relief=SOLID,font=("Times New Roman",24,"bold"),command=opengc)
    b2.pack(pady=5)

    b3 = Button(a,text="Gmail  @",width=8,relief=SOLID,fg="red",font=("Times New Roman",24,"bold"),command=opengg)
    b3.pack(pady=5)

    b4 = Button(a,text="Brave",width=8,relief=SOLID,fg="orange",font=("Times New Roman",24,"bold"),command=openb)
    b4.pack(pady=5)

    b5 = Button(a,text="Youtube",width=8,relief=SOLID,fg="red",font=("Times New Roman",24,"bold"),command=openyt)
    b5.pack(pady=5)

    b6 = Button(a,text="Calculator",width=8,relief=SOLID,font=("Times New Roman",24,"bold"),command=openc)
    b6.pack(pady=5)

    b7 = Button(a,text="Office",width=6,relief=SOLID,font=("Times New Roman",24,"bold"),
              command=openo)
    b7.pack(pady=5)

    b8 = Button(a,text="Exit",width=6,relief=SOLID,font=("Times New Roman",24,"bold"),
              fg="black",bg="grey",command=a.destroy)
    b8.pack(pady=5,side=RIGHT,padx=5)


    a.mainloop()
    
    
    
but = Button(root,text="next page",font=("Times",20,"bold"),comm=gui_win)
but.pack(pady=300)

root.mainloop()