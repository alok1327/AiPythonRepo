import webbrowser
import speech_recognition as sr
import win32com.client
import os
import datetime
import wikipedia
import time
import random
import requests
import openai
from config import apikey

openai.api_key = apikey

response = openai.  Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email for resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")

    elif hour>=12 and hour<18:
        say("Good Afternoon")
    
    else:
        say("Good Evening!")
    say("I am EDITH Sir. Please tell me how may I help you")
    print("I am EDITH Sir. Please tell me how may I help you")
       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred, Sorry from EDITH"

if __name__ == '__main__':
    wishMe()

    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            say('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            say("According to Wikipedia")
            say(results)
            print(results) 

        if 'open youtube' in query:
            webbrowser.open("youtube.com") 

        if 'open google' in query:
            webbrowser.open("google.com") 
        
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            
        if "play music" in query:
            music_path = "D:\\songs"
            songs = os.listdir(music_path)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_path, rd))
        
        if "the time" in query:
           strfTime = datetime.datetime.now().strftime("%H:%M:%S")
           say(f"Sir, The time is {strfTime}")       
                
                
                #break  # Exit the loop after opening the site



        #say(query)

