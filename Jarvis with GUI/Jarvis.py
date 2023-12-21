# Importing modules
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import os
import random
import smtplib
import requests
from tkinter import *
import threading
from PIL import ImageTk,Image


root = Tk()

global var_me
global var_you

var_me = StringVar() 
var_you = StringVar() 

# Main Variables
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# Functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def weather_report():
    api_add  = "http://api.openweathermap.org/data/2.5/weather?q=Hyderabad,Pk&appid=ebed657b48280bc77305acdc14ff4315"
    json_command = requests.get(api_add).json()
    weather_data = json_command['weather'][0]['main']
    wind_data = json_command['wind']['speed']
    speak(f"weather is {weather_data} sir and wind speed is {wind_data}")
    print(f"Jarvis: Weather is {weather_data} sir and Wind speed is {wind_data}")
    var_you.set(f"Jarvis: Weather is {weather_data} sir and Wind speed is {wind_data}")
    root.update()

def wish_me():
    global hour;
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Jarvis: Good Morning") 
        var_you.set("Good Morning")
        root.update()
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Jarvis: Good After Noon")
        var_you.set("Good After Noon")
        root.update()
    else:
        speak("Good Evening")
        print("Jarvis: Good Evening")
        var_you.set("Good Morning")
        root.update()
    speak("Hello Sir, I am jarvis, how was your day?")
    print("Jarvis: Hello Sir, I am jarvis, how was your day?")
    var_you.set("Hello Sir, I am jarvis, how was your day?")
    root.update()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Jarvis: Listening...")
        var_you.set("Jarvis: Listening...")
        root.update()
        energy_threshold = 0
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        audio = r.listen(source, phrase_time_limit=5)        
    try:
        speak("Recognizing")
        print("Jarvis: Recognizing...")
        var_you.set("Jarvis: Recognizing...")
        root.update()

        query = r.recognize_google(audio)
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please")
        print("Jarvis: Say that again please...")
        var_you.set("Jarvis: Say that again please...")
        root.update()
        return "None"
    var_me.set(f"User said: {query}")
    root.update()
    return query
def google_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What you want to search from google?")
        print("Jarvis: What you want to search from google?")
        var_you.set("Jarvis: What you want to search from google?")
        root.update()

        speak("listening")
        print("Jarvis: listening...")
        var_you.set("Jarvis: listening...")
        root.update()

        r.adjust_for_ambient_noise(source)
        audio  = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"Jarvis: You Said: {text}")
            var_you.set(f"Jarvis: You Said: {text}")
            root.update()
            url = 'https://www.google.com/search?client=firefox-b-d&q='
            search_url = url+text
            webbrowser.open(search_url)
        except Exception as e:
            speak("say again search google google")
            print("Jarvis: Say again search google google")
            var_you.set("Jarvis: Say again search google google")
            root.update()
def youtube_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What you want to search from youtube?")
        print("What you want to search from youtube")
        var_you.set("What you want to search from youtube")
        root.update()
        speak("listening")
        print("Jarvis: listening...")
        var_you.set("Jarvis: listening...")
        root.update()
        
        r.adjust_for_ambient_noise(source)
        audio  = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You Said: {text}")
            var_you.set(f"You Said: {text}")
            root.update()
            url = 'https://www.youtube.com/results?search_query='
            search_url = url+text
            webbrowser.open(search_url)
        except Exception as e:
            speak("say again search through youtube")
            print("Jarvis: Say again search through youtube")
            var_you.set("Jarvis: Say again search through youtube")
            root.update()
def sendemail(to,subject,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("email", "password@")
    server.sendmail("email", to, f"Subject:{subject}\n\n{content}")
    server.close()

def jarvis():
    # Executing
    if __name__ == "__main__":
        wish_me()    
        while True:
            query = take_command().lower()
            # Searching by Wikipidia
            if 'wikipedia' in query:
                try:
                    speak('Searching Wikipedia...')
                    print('Jarvis: Searching Wikipedia...')
                    var_you.set('Jarvis: Searching Wikipedia...')
                    root.update()
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print("Jarvis: According to Wikipedia")
                    var_you.set("Jarvis: According to Wikipedia")
                    root.update()
                    speak(results)
                    print(results)
                    var_you.set(results)
                    root.update()
                    speak("The End")
                    print("The End")
                    var_you.set("The End")
                    root.update()
                except Exception as e:
                    speak("Try again by saying full name or say another")
                    print("Jarvis: Try again by saying full name or say another")
                    var_you.set("Jarvis: Try again by saying full name or say another")
                    root.update()
            # Browsing
            elif 'open youtube' in query:
                webbrowser.get(chrome).open("youtube.com")
                speak("opening youtube")
                print("Jarvis: opening youtube")
                var_you.set("Jarvis: opening youtube")
                root.update()
            elif 'open google' in query:
                webbrowser.get(chrome).open("google.com") 
                speak("opening google")
                print("Jarvis: opening google")
                var_you.set("Jarvis: opening google")
                root.update()
            elif 'open facebook' in query:
                webbrowser.get(chrome).open("facebook.com") 
                speak("opening facebook")
                print("Jarvis: opening facebook")
                var_you.set("Jarvis: opening facebook")
                root.update()
            elif 'gold rate' in query:
                webbrowser.get(chrome).open("http://www.livepriceofgold.com/pakistan-gold-price.html")
                speak("opening gold rate")
                print("Jarvis: opening gold rate")
                var_you.set("Jarvis: opening gold rate")
                root.update()
            # commands which take data
            elif 'google' in query:
                try:
                    speak("working")
                    print("Jarvis: wroking...")
                    var_you.set("Jarvis: wroking...")
                    root.update()
                    google_search()
                except Exception as e:
                    speak("say again search from google")
                    print("Jarvis: say again search from google")
                    var_you.set("Jarvis: say again search from google")
                    root.update()
            elif 'youtube' in query:
                try:
                    speak("working")
                    print("Jarvis: wroking...")
                    var_you.set("Jarvis: wroking...")
                    root.update()

                    youtube_search()
                except Exception as e:
                    speak("say again search from google")
                    print("Jarvis: say again search from google")        
                    var_you.set("Jarvis: say again search from google")
                    root.update()        
            elif "email" in query:
                try:
                    speak(" Sir enter the email")
                    try:
                        to = input("Sir enter the email: ")
                    except Exception as e:
                        speak("Sir input is invalid, try again by saying email")
                        print("Jarvis: Sir input is invalid, try again by saying email")
                        var_you.set("Jarvis: Sir input is invalid, try again by saying email")
                        root.update()
                    speak("Sir what's the subject should be")
                    print("Jarvis: Sir what's the subject should be")
                    var_you.set("Jarvis: Sir what's the subject should be")
                    root.update()
                    subject = take_command()
                    speak("what should i say")
                    print("Jarvis: what should I say?")
                    var_you.set("Jarvis: what should I say?")
                    root.update()
                    content = take_command()
                    sendemail(to,subject,content)
                    speak("Email has been sent")
                except Exception as e:
                    speak("please retry")
                    print("Jarvis: please retry")
                    var_you.set("Jarvis: please retry")
                    root.update()
            # Local queries
            elif "the date time" in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                strdate = datetime.date.today()
                speak(f"Sir, the time is {strtime} and the date is {strdate}")    
                print(f"Jarvis: Sir, the time is {strtime} and the date is {strdate}")       
                var_you.set(f"Jarvis: Sir, the time is {strtime} and the date is {strdate}")
                root.update()       
            elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strtime}")
                print(f"Jarvis: Sir, the time is {strtime}")
                var_you.set(f"Jarvis: Sir, the time is {strtime}")
                root.update()
                datetime.datetime.now()
            elif "the date" in query:
                strdate = datetime.date.today()
                speak(f"The date is {strdate}")
                print(f"Jarvis: Sir, the date is {strdate}")
                var_you.set(f"Jarvis: Sir, the date is {strdate}")
                root.update()
            elif "i am fine" in query:
                speak("Sir what you want to do?")
                print("Sir what you want to do?")
                var_you.set("Sir what you want to do?")
                root.update()
            elif 'weather' in query:
                weather_report()
            # Prayer information
            # ''' Prayers correct pronounciation
            #         speak('qazza')
            #         speak('jummah')
            #         speak('fajjar')
            #         speak('zo har')
            #         speak('as sar')
            #         speak('magh rib')
            #         speak('ishaa')
            #         speak('nammaz')
            # '''
            elif 'fajr' in query:
                globals(hour and mint)
                hour = int(datetime.datetime.now().hour)
                mint = int(datetime.datetime.now().minute)
                if hour>=6 and mint>=19:
                    speak("Sir nammazzay fajjar time has been finished"),
                    print("Sir nammazzay fajjar time has been finished")
                    var_you.set("Sir nammazzay fajjar time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you din't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'fajar' and 'remaining' in query:
                if hour<=6 and mint<=19:
                    speak("Yes sir, nammazzay fajjar time is remaining you can perform"),
                    print("Yes sir, nammazzay fajjar time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay fajjar time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            elif 'zohar' in query:
                if hour>=16 and mint>=45:
                    speak("Sir nammazzay zo har time has been finished"),
                    print("Sir nammazzay zo har time has been finished")
                    var_you.set("Sir nammazzay zo har time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you dint't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'johar'in query:
                if hour<=16 and mint<=45:
                    speak("Yes sir, nammazzay zo har time is remaining you can perform"),
                    print("Yes sir, nammazzay zo har time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay zo har time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            elif 'asar' and 'finshed' in query:
                if hour>=18 and mint>=29:
                    speak("Sir nammazzay as sar time has been finished"),
                    print("Sir nammazzay as sar time has been finished")
                    var_you.set("Sir nammazzay as sar time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you dint't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'asar' and 'remaining' in query:
                if hour<=18 and mint<=29:
                    speak("Yes sir, nammazzay as sar time is remaining you can perform"),
                    print("Yes sir, nammazzay as sar time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay as sar time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            elif 'maghrib' and 'finshed' in query:
                if hour>=19 and mint>=45:
                    speak("Sir nammazzay magh rib time has been finished"),
                    print("Sir nammazzay magh rib time has been finished")
                    var_you.set("Sir nammazzay magh rib time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you dint't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'maghrib' and 'remaining' in query:
                if hour<=19 and mint<=45:
                    speak("Yes sir, nammazzay magh rib time is remaining you can perform"),
                    print("Yes sir, nammazzay magh rib time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay magh rib time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            elif 'isha' and 'finshed' in query:
                if hour>=00 and mint>=30:
                    speak("Sir nammazzay ishaa time has been finished"),
                    print("Sir nammazzay ishaa time has been finished")
                    var_you.set("Sir nammazzay ishaa time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you dint't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'isha' and 'remaining' in query:
                if hour<=00 and mint<=30:
                    speak("Yes sir, nammazzay ishaa time is remaining you can perform"),
                    print("Yes sir, nammazzay ishaa time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay ishaa time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            elif 'jumma' and 'finshed' in query:
                if hour>=5 and mint>=17:
                    speak("Sir nammazzay jummah time has been finished"),
                    print("Sir nammazzay jummah time has been finished")
                    var_you.set("Sir nammazzay jummah time has been finished")
                    root.update()
                else:
                    speak("Sir time is remaining you should go and perform if you dint't"),
                    print("Sir time is remaining you should go and perform if you dint't")
                    var_you.set("Sir time is remaining you should go and perform if you dint't")
                    root.update()
            elif 'jumma' and 'remaining' in query:
                if hour<=5 and mint<=17:
                    speak("Yes sir, nammazzay jummah time is remaining you can perform"),
                    print("Yes sir, nammazzay jummah time is remaining you can perform")
                    var_you.set("Yes sir, nammazzay jummah time is remaining you can perform")
                    root.update()
                else:
                    speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                    print("Sir you are late time has finished but you can perfrom qazza nammaz")
                    var_you.set("Sir you are late time has finished but you can perfrom qazza nammaz")
                    root.update()
            # Open programs
            elif "open mega" in query:
                mega_path = "C://Users//mfaiz//AppData//Local\MEGAsync//MEGAsync.exe"
                os.startfile(mega_path)
                speak("opening mega")
                print("Jarvis: opening mega")
                var_you.set("Jarvis: opening mega")
                root.update()
            elif "open control panel" in query:
                control_panel_path = "C://Users//Home.AHMEDIBRAHIM//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//System Tools//Control Panel.lnk"
                os.startfile(control_panel_path)
                speak("opening control panel")
                print("Jarvis: opening control panel")
                var_you.set("Jarvis: opening control panel")
                root.update()
            elif 'open visual studio' in query:
                speak("opening visual studio")
                print("Jarvis: opening Visual Studio")
                var_you.set("Jarvis: opening Visual Studio")
                root.update()
                vs_code_path = 'C:/Users/Home.AHMEDIBRAHIM/AppData/Local/Programs/Microsoft VS Code/Code.exe'
                os.startfile(vs_code_path)
            elif 'open firefox' in query:
                mozilla_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
                os.startfile(mozilla_path)
                speak("opening mozilla firefox")
                print("Jarvis: opening Mozilla Firefox")
                var_you.set("Jarvis: opening Mozilla Firefox")
                root.update()
            elif 'music' in query:
                music_dir = "F:/Muhammad Faiz/BY INTERNET/Songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,random.choice(songs)))
            # Close program
            elif 'close mega' in query:
                speak("closing Mega"),print("Jarvis: closing Mega")
                os.system('C:/Windows/System32/taskkill.exe /F /IM MEGAsync.exe')
                speak("Sir Mega has closed")
                print("Jarvis: Sir Mega has closed")
                var_you.set("Jarvis: Sir Mega has closed")
                root.update()
            elif 'close control panel' in query :
                speak("closing control panel"),print("Jarvis: closing control panel")
                os.system('C:/Windows/System32/taskkill.exe /F /IM Control_Panel.lnk')
                speak("Sir Control panel has closed")
                print("Jarvis: Sir control panel has closed")
                var_you.set("Jarvis: Sir control panel has closed")
                root.update()
            elif 'close visual studio' in query:
                speak("closing visual studio"),print("Jarvis: closing visual studio")
                os.system('C:/Windows/System32/taskkill.exe /F /IM code.exe')
                speak("Sir visual studio has closed")
                print("Jarvis: Sir visual studio has closed")
                var_you.set("Jarvis: Sir visual studio has closed")
                root.update()
            elif 'close firefox' in query:
                speak("closing firefox"),print("Jarvis: closing firefox")
                os.system('C:/Windows/System32/taskkill.exe /F /IM firefox.exe')
                speak("Sir firefox has closed")
                print("Jarvis: Sir firefox has closed")
                var_you.set("Jarvis: Sir firefox has closed")
                root.update()
            elif 'close chrome' in query:
                speak("closing chrome")
                print("Jarvis: closing chrome")
                var_you.set("Jarvis: closing chrome")
                os.system('C:/Windows/System32/taskkill.exe /F /IM chrome.exe')
                speak("Sir google chrome has closed")
                print("Jarvis: Sir google chrome has closed")
                var_you.set("Jarvis: Sir google chrome has closed")
                root.update()
            elif 'close all programs' in query:
                speak("closing programs"),print("Jarvis: closing programs")
                os.system('C:/Windows/System32/taskkill.exe /F /IM *.exe')
                speak("Sir all programs have closed")
                print("Jarvis: Sir all program have closed")
                var_you.set("Jarvis: Sir all program have closed")
            # Program exit
            elif "exit" in query:
                speak("Quieting sir, thank you for your time")
                print("Quieting sir, thank you for your time")
                var_you.set("Quieting sir, thank you for your time")
                exit()
            # System Power
            elif "shutdown" in query:
                speak("Shutdowning sir, have a nice day")
                var_you.set("Shutdowning sir, have a nice day")
                root.update()
                speak("good bye sir")
                var_you.set("good bye sir")
                root.update()
                os.system("C:/Windows/System32/shutdown.exe /s /t 0")     
            elif "hibernate" in query:
                speak("hibernating sir, i hope we will meet soon")
                var_you.set("hibernating sir, i hope we will meet soon")
                root.update()
                speak("good bye sir")
                var_you.set("good bye sir")
                root.update()
                os.system("C:/Windows/System32/rundll32 powrprof.dll ,SetSuspendState")
                exit()
            elif "lock" in query:
                speak("logoffing sir, you can switch to another account")
                var_you.set("logoffing sir, you can switch to another account")
                root.update()
                speak("goodbye sir")
                var_you.set("goodbye sir")
                root.update()
                os.system("C:/Windows/System32/rundll32.exe User32.dll ,LockWorkStation")
            elif "restart the computer" in query:
                speak("restarting sir, i hope it will reopen quickly")
                var_you.set("restarting sir, i hope it will reopen quickly")
                root.update()
                speak("good bye")
                var_you.set("good bye")
                root.update()
                os.system("C:\Windows\System32\shutdown.exe -r -t 00")
            elif "sleep" in query:
                speak("sleeping sir")
                var_you.set("sleeping sir")
                root.update()
                speak("good bye sir")
                var_you.set("good bye sir")
                root.update()
                os.system("C:/Windows/System32/rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
from tkinter import ttk

# buttons functions
def minimize_button_hover(event):
    minimize_button.configure(bg="white", fg="black")
def minimize_button_leave(event):
    minimize_button.configure(fg="white", bg="black")

def close_button_hover(event):
    close_button.configure(bg="red", fg="white")
def close_button_leave(event):
    close_button.configure(fg="white", bg="black")

# buttons functions exit

root.attributes('-alpha',0.85)
root.configure(background="black", borderwidth=7)
# root.overrideredirect(0)
root.wm_attributes('-fullscreen','true')

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

canvas=Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())

image=ImageTk.PhotoImage(Image.open("D:\Muhammad Faiz\Python\Jarvis\Jarvis with GUI\Background.jpg"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack(fill=BOTH, expand=TRUE)

close_button = Button(canvas, text = "Close", relief=FLAT, pady=2, fg="white", activebackground='black',activeforeground='white', width=6, font=("Roboto", 13), bg="black",command =lambda : root.destroy())
close_button.pack(side=RIGHT, anchor=NE)

close_button.bind("<Enter>", close_button_hover)
close_button.bind("<Leave>", close_button_leave)

minimize_button = Button(canvas, text = "Minimize", relief=FLAT, pady=2, fg="white", activebackground='black',activeforeground='white', width=8, font=("Roboto", 13), bg="black",command = lambda: root.wm_state("iconic"))
minimize_button.pack(side=RIGHT, anchor=NE)

minimize_button.bind("<Enter>", minimize_button_hover)
minimize_button.bind("<Leave>", minimize_button_leave)

def start_function():

    start_button.place_forget()

    var_you_label = Label(canvas, textvariable = var_you, pady=2, bg="white",  width=root.winfo_screenwidth(), height=2, font=("Roboto", 18), fg="dark blue")
    var_you.set('Welcome')
    var_you_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    var_me_label = Label(canvas, textvariable = var_me, pady=2, bg="dark blue",  width=root.winfo_screenwidth(), height=2, font=("Roboto", 18), fg="white")
    var_me.set('Say Exit for Quit')
    var_me_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    close_button.configure(state=DISABLED)
    # minimize_button.configure(state=DISABLED)

    def update(ind):
        frame = frames[(ind)%100]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)


    frames = [PhotoImage(file='D:\Muhammad Faiz\Python\Jarvis\Jarvis with GUI\Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]

    label = Label(canvas, width = 400, height = 400, bg= "black")
    label.place(rely=0.65, relx=0.5, anchor=CENTER)
    root.after(100, update, 100)


    threading.Thread(target=jarvis).start()




start_button = Button(canvas, text = "START", relief=FLAT, pady=2, bg="white", activebackground='black',activeforeground='white', width=8, font=("Roboto", 13), fg="black", command = start_function)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)




root.mainloop()
