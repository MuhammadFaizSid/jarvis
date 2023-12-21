# import webbrowser
# import speech_recognition as sr
# # chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# # webbrowser.get(chrome).open("youtube.com")
# def check():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print("Speack")
#         audio  = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             print("You Said: ".format(text))
#             url = 'https://www.google.com/search?client='
#             search_url = url+text
#             webbrowser.open(search_url)
#         except expression as e:
#             print("Can't recognize")
# check()
# import datetime
# print(datetime.date.today())
# import smtplib

# def sendemail(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()
#     server.login("email", "password@")
#     server.sendmail("email", to, content)

#     server.close()
# to = "email"
# content = "check"
# sendemail(to, content)


# shutdown_&_more_commands
# import os
# Shutdown
# check = input("Want to shutdown your computer ? (y/n): ");
# if check == 'n':
#     exit();
# else:
#     os.system("C:/Windows/System32/shutdown.exe /s /t 0" )
#     print("runing")

# Sleep
# check = input("Want to sleep your computer ? (y/n): ");
# if check == 'n':
#     exit();
# else:
#     os.system("C:/Windows/System32/rundll32.exe powrprof.dll,SetSuspendState 0,1,0" )
#     print("runing")

# Lock
# check = input("Want to lock your computer ? (y/n): ");
# if check == 'n':
#     exit();
# else:
#     os.system("C:/Windows/System32/rundll32.exe User32.dll ,LockWorkStation" )
#     print("runing")

# Hibernate
# check = input("Want to hibernate your computer ? (y/n): ");
# if check == 'n':
#     exit();
# else:
#     os.system("C:/Windows/System32/rundll32 powrprof.dll ,SetSuspendState" )
#     print("runing")

# Restart
# import os
# check = input("Want to restart your computer ? (y/n): ");
# if check == 'n':
#     exit();
# else:
#     os.system("C:\Windows\System32\shutdown.exe -r -t 00" )
#     print("runing")
# import webbrowser
# chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# webbrowser.get(chrome).open("google.com") 
# speak("opening google")
# print("Jarvis: opening google")
# import os
# import random
# music_dir = "F:/Muhammad Faiz/BY INTERNET/Songs"
# songs = os.listdir(music_dir)
# os.startfile(os.path.join(music_dir,random.choice(songs)))
# import requests
# api_add  = "http://api.openweathermap.org/data/2.5/weather?q=Hyderabad,Pk&appid=ebed657b48280bc77305acdc14ff4315"
# # dd = input("City name: ")
# # url = api_add+dd
# json = requests.get(api_add).json()
# formatted_data = json['weather'][0]['main'], json['wind']['speed']
# print(formatted_data)
# import os
# os.system('C:/Windows/System32/taskkill.exe /F /IM .exe')
# import time
# import speech_recognition as sr
# import datetime
# import wikipedia
# import pyttsx3
# import webbrowser
# import os
# import random
# import smtplib
# # import requests
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty("voices")
# engine.setProperty('voice',voices[1].id)
# chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# strtime = datetime.datetime.now().strftime("%H:%M:%S")
# strdate = datetime.date.today()
# speak(f"Sir, the time is {strtime} and the date is {strdate}")    
# print(f"Jarvis: Sir, the time is {strtime} and the date is {strdate}")    
## Adding or subtracting datetime with time
# from datetime import datetime, timedelta
 
# # Original datetime
# datetime_original = datetime(year=2006, month=11, day=23)
# print("\nOriginal datetime: ", datetime_original, "\n")
 
# # Time to add or subtract
# time_delta = timedelta(hours=10, minutes=23, seconds=45, microseconds=162342)
# print("Timedelta: ", time_delta, "\n")
 
# # Add
# datetime_new = datetime_original + time_delta
# print("After adding time: ", datetime_new, "\n")
 
# # Subtract
# datetime_new = datetime_original - time_delta
# print("After subtracting time: ", datetime_new, "\n")
# import datetime
# import os
# import time

# # now = datetime.datetime.now()

# # # Choose 6PM today as the time the alarm fires.
# # # This won't work well if it's after 6PM, though.
# # fajar_time = datetime.datetime.combine(now.date(), datetime.time(21, 0, 0))

# # # Think of time.sleep() as having the operating system set an alarm for you,
# # # and waking you up when the alarm fires.
# # print((fajar_time - now))
# now =  datetime.datetime.now().strftime("%H:%M:%S")
# fajar = datetime.datetime.(now), datetime.time(21,0,0)
# import datetime
# hour = int(datetime.datetime.now().hour)
# mint = int(datetime.datetime.now().minute)
# if hour>=12 and mint>=17:
#     print("finished")
# else:
#     print("time is remaining")
import pyttsx
engine = pyttsx.init('sapi5')
engine.say('hellow world')
print('hellow world')
engine.runAndWait()
