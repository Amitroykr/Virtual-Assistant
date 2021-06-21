
#import module
import pyttsx3
import speech_recognition
import datetime
import os
import webbrowser
import smtplib
import random
from requests import get
import wikipedia
import sys
import requests
import json
import time
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#text to speech
def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing.........")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        #speak("Say that again please...........")
        return "none"
    query = query.lower()
    return query

#wish function
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("Sir, I am your virtual assistent, How can i help you.")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anjali89088@gmail.com', 'raj89088')
    server.sendmail('anjali89088@gmail.com', to, content)
    server.close()

def taskExecution():
    assname = 'neo'
    wish()
    while True:
        query = takecommand()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtTime}")

        #open notepad
        elif "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("whome should i send")
                to = input()
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")

        elif 'play music' in query:
            music_dir = "E:\Moblie"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address  is {ip}")
        
        elif "wikipedia" in query:
            speak("searching in wikipedia.........")
            query =query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)
            print(result)
            
        elif "read news" in query or "read lastest news" in query:
            import bs4
            from bs4 import BeautifulSoup as soup
            from urllib.request import urlopen

            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            # Print news title, url and publish date
            for news in news_list:
                speak(news.title.text)
                speak(news.pubDate.text)
                speak("-"*60)
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
        
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        
        
        elif "thank you" in query or "thanks" in query:
            speak("It's my pleasure sir.")

        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime")
            break
            

if __name__ == '__main__':
    
    while True: 
        permission = takecommand()
        if "wake up" in permission:
            taskExecution()
            
        elif "goodbye" in permission:
            speak("thank for using me sir")
            sys.exit()      