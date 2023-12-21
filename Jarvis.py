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

def wish_me():
    global hour;
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Jarvis: Good Morning") 
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Jarvis: Good After Noon")
    else:
        speak("Good Evening")
        print("Jarvis: Good Evening")
    speak("Hello Sir, I am jarvis, how was your day?")
    print("Jarvis: Hello Sir, I am jarvis, how was your day?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Jarvis: Listening...")
        energy_threshold = 0
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        audio = r.listen(source, phrase_time_limit=5)        
    try:
        speak("Recognizing")
        print("Jarvis: Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please")
        print("Jarvis: Say that again please...")
        return "None"
    return query
def google_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What you want to search from google?")
        print("What you want to search from google?")
        speak("listening")
        print("listening...")
        r.adjust_for_ambient_noise(source)
        audio  = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You Said: {text}")
            url = 'https://www.google.com/search?client=firefox-b-d&q='
            search_url = url+text
            webbrowser.open(search_url)
        except Exception as e:
            speak("say again search google google")
            print("Jarvis: Say again search google google")
def youtube_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What you want to search from youtube?")
        print("What you want to search from youtube")
        speak("listening")
        print("listening...")
        r.adjust_for_ambient_noise(source)
        audio  = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You Said: {text}")
            url = 'https://www.youtube.com/results?search_query='
            search_url = url+text
            webbrowser.open(search_url)
        except Exception as e:
            speak("say again search through youtube")
            print("Jarvis: Say again search through youtube")

def sendemail(to,subject,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("emailaddress", "password")
    server.sendmail("emailaddress", to, f"Subject:{subject}\n\n{content}")
    server.close()

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
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print("Jarvis: According to Wikipedia")
                speak(results)
                print(results)
                speak("The End")
                print("The End")
            except Exception as e:
                speak("Try again by saying full name or say another")
                print("Jarvis: Try again by saying full name or say another")
        # Browsing
        elif 'open youtube' in query:
            webbrowser.get(chrome).open("youtube.com")
            speak("opening youtube")
            print("Jarvis: opening youtube")
        elif 'open google' in query:
            webbrowser.get(chrome).open("google.com") 
            speak("opening google")
            print("Jarvis: opening google")
        elif 'open facebook' in query:
            webbrowser.get(chrome).open("facebook.com") 
            speak("opening facebook")
            print("Jarvis: opening facebook")
        elif 'gold rate' in query:
            webbrowser.get(chrome).open("http://www.livepriceofgold.com/pakistan-gold-price.html")
            speak("opening gold rate")
            print("Jarvis: opening gold rate")
        # commands which take data
        elif 'google' in query:
            try:
                speak("working")
                print("Jarvis: wroking...")
                google_search()
            except Exception as e:
                speak("say again search from google")
                print("Jarvis: say again search from google")
        elif 'youtube' in query:
            try:
                speak("working")
                print("Jarvis: wroking...")
                youtube_search()
            except Exception as e:
                speak("say again search from google")
                print("Jarvis: say again search from google")        
        elif "email" in query:
            try:
                speak(" Sir enter the email")
                try:
                    to = input("Sir enter the email: ")
                except Exception as e:
                    speak("Sir input is invalid, try again by saying email")
                    print("Jarvis: Sir input is invalid, try again by saying email")
                speak("Sir what's the subject should be"),print("Jarvis: Sir what's the subject should be")
                subject = take_command()
                speak("what should i say"),print("Jarvis: what should I say?")
                content = take_command()
                sendemail(to,subject,content)
                speak("Email has been sent")
            except Exception as e:
                speak("please retry")
                print("Jarvis: please retry")
        # Local queries
        elif "the date time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            strdate = datetime.date.today()
            speak(f"Sir, the time is {strtime} and the date is {strdate}")    
            print(f"Jarvis: Sir, the time is {strtime} and the date is {strdate}")       
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
            print(f"Jarvis: Sir, the time is {strtime}")
            datetime.datetime.now()
        elif "the date" in query:
            strdate = datetime.date.today()
            speak(f"The date is {strdate}")
            print(f"Jarvis: Sir, the date is {strdate}")
        elif "i am fine" in query:
            speak("Sir what you want to do?")
            print("Sir what you want to do?")
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
            else:
                speak("Sir time is remaining you should go and perform if you din't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'fajar' and 'remaining' in query:
            if hour<=6 and mint<=19:
                speak("Yes sir, nammazzay fajjar time is remaining you can perform"),
                print("Yes sir, nammazzay fajjar time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        elif 'zohar' in query:
            if hour>=16 and mint>=45:
                speak("Sir nammazzay zo har time has been finished"),
                print("Sir nammazzay zo har time has been finished")
            else:
                speak("Sir time is remaining you should go and perform if you dint't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'johar'in query:
            if hour<=16 and mint<=45:
                speak("Yes sir, nammazzay zo har time is remaining you can perform"),
                print("Yes sir, nammazzay zo har time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        elif 'asar' and 'finshed' in query:
            if hour>=18 and mint>=29:
                speak("Sir nammazzay as sar time has been finished"),
                print("Sir nammazzay as sar time has been finished")
            else:
                speak("Sir time is remaining you should go and perform if you dint't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'asar' and 'remaining' in query:
            if hour<=18 and mint<=29:
                speak("Yes sir, nammazzay as sar time is remaining you can perform"),
                print("Yes sir, nammazzay as sar time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        elif 'maghrib' and 'finshed' in query:
            if hour>=19 and mint>=45:
                speak("Sir nammazzay magh rib time has been finished"),
                print("Sir nammazzay magh rib time has been finished")
            else:
                speak("Sir time is remaining you should go and perform if you dint't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'maghrib' and 'remaining' in query:
            if hour<=19 and mint<=45:
                speak("Yes sir, nammazzay magh rib time is remaining you can perform"),
                print("Yes sir, nammazzay magh rib time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        elif 'isha' and 'finshed' in query:
            if hour>=00 and mint>=30:
                speak("Sir nammazzay ishaa time has been finished"),
                print("Sir nammazzay ishaa time has been finished")
            else:
                speak("Sir time is remaining you should go and perform if you dint't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'isha' and 'remaining' in query:
            if hour<=00 and mint<=30:
                speak("Yes sir, nammazzay ishaa time is remaining you can perform"),
                print("Yes sir, nammazzay ishaa time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        elif 'jumma' and 'finshed' in query:
            if hour>=5 and mint>=17:
                speak("Sir nammazzay jummah time has been finished"),
                print("Sir nammazzay jummah time has been finished")
            else:
                speak("Sir time is remaining you should go and perform if you dint't"),
                print("Sir time is remaining you should go and perform if you dint't")
        elif 'jumma' and 'remaining' in query:
            if hour<=5 and mint<=17:
                speak("Yes sir, nammazzay jummah time is remaining you can perform"),
                print("Yes sir, nammazzay jummah time is remaining you can perform")
            else:
                speak("Sir you are late time has finished but you can perfrom qazza nammaz"),
                print("Sir you are late time has finished but you can perfrom qazza nammaz")
        # Open programs
        elif "open mega" in query:
            mega_path = "C://Users//mfaiz//AppData//Local\MEGAsync//MEGAsync.exe"
            os.startfile(mega_path)
            speak("opening mega")
            print("Jarvis: opening mega")
        elif "open control panel" in query:
            control_panel_path = "C://Users//Home.AHMEDIBRAHIM//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//System Tools//Control Panel.lnk"
            os.startfile(control_panel_path)
            speak("opening control panel")
            print("Jarvis: opening control panel")
        elif 'open visual studio' in query:
            speak("opening visual studio")
            print("Jarvis: opening Visual Studio")
            vs_code_path = 'C:/Users/Home.AHMEDIBRAHIM/AppData/Local/Programs/Microsoft VS Code/Code.exe'
            os.startfile(vs_code_path)
        elif 'open firefox' in query:
            mozilla_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
            os.startfile(mozilla_path)
            speak("opening mozilla firefox")
            print("Jarvis: opening Mozilla Firefox")
        elif 'music' in query:
            music_dir = "F:/Muhammad Faiz/BY INTERNET/Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
        # Close program
        elif 'close mega' in query:
            speak("closing Mega"),print("Jarvis: closing Mega")
            os.system('C:/Windows/System32/taskkill.exe /F /IM MEGAsync.exe')
            speak("Sir Mega has closed"),print("Jarvis: Sir Mega has closed")
        elif 'close control panel' in query :
            speak("closing control panel"),print("Jarvis: closing control panel")
            os.system('C:/Windows/System32/taskkill.exe /F /IM Control_Panel.lnk')
            speak("Sir Control panel has closed"),print("Jarvis: Sir control panel has closed")
        elif 'close visual studio' in query:
            speak("closing visual studio"),print("Jarvis: closing visual studio")
            os.system('C:/Windows/System32/taskkill.exe /F /IM code.exe')
            speak("Sir visual studio has closed"),print("Jarvis: Sir visual studio has closed")
        elif 'close firefox' in query:
            speak("closing firefox"),print("Jarvis: closing firefox")
            os.system('C:/Windows/System32/taskkill.exe /F /IM firefox.exe')
            speak("Sir firefox has closed"),print("Jarvis: Sir firefox has closed")
        elif 'close chrome' in query:
            speak("closing chrome"),print("Jarvis: closing chrome")
            os.system('C:/Windows/System32/taskkill.exe /F /IM chrome.exe')
            speak("Sir google chrome has closed"),print("Jarvis: Sir google chrome has closed")
        elif 'close all programs' in query:
            speak("closing programs"),print("Jarvis: closing programs")
            os.system('C:/Windows/System32/taskkill.exe /F /IM *.exe')
            speak("Sir all programs have closed"),print("Jarvis: Sir all program have closed")
        # Program exit
        elif "exit" in query:
            speak("Quieting sir, thank you for your time")
            print("Quieting sir, thank you for your time")
            exit()
        # System Power
        elif "shutdown" in query:
            speak("Shutdowning sir, have a nice day")
            speak("good bye sir")
            os.system("C:/Windows/System32/shutdown.exe /s /t 0")     
        elif "hibernate" in query:
            speak("hibernating sir, i hope we will meet soon")
            speak("good bye sir")
            os.system("C:/Windows/System32/rundll32 powrprof.dll ,SetSuspendState")
            exit()
        elif "lock" in query:
            speak("logoffing sir, you can switch to another account")
            speak("goodbye sir")
            os.system("C:/Windows/System32/rundll32.exe User32.dll ,LockWorkStation")
        elif "restart the computer" in query:
            speak("restarting sir, i hope it will reopen quickly")
            speak("good b")
            os.system("C:\Windows\System32\shutdown.exe -r -t 00")
        elif "sleep" in query:
            speak("sleeping sir")
            speak("good bye sir")
            os.system("C:/Windows/System32/rundll32.exe powrprof.dll,SetSuspendState 0,1,0")