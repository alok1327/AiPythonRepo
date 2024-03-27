import webbrowser
import speech_recognition as sr
import win32com.client
import os
import sys
import datetime
import wikipedia
import time
import random
import requests
import datetime

def wishMe():
    time = datetime.datetime.now().strftime('%I:%M %p')  # Corrected time format
    city = "Delhi"
    api_key = "ac19358acbac4d7633c886a56efce9e8"  # Enclose the API key in quotes
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()
        temp = data['main']['temp']
    
    else:
        print("Error fetching weather data.")

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Good Morning")
        say("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
        say("Good Afternoon!")
    else:
        print("Good Evening")
        say("Good Evening!")

    say('the time is ' + time)  # Added space before time
    print('the time is ' + time)
    say(f'The current temperature in {city} is {temp} degrees Celsius.')
    print(f'The current temperature in {city} is {temp} degrees Celsius.')
    say("I am JARVIS, Please tell me how may I help you")
    print("I am JARVIS, Please tell me how may I help you")

    

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

   
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
            return "Some Error Occurred, Sorry from JARVIS"

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
            say("Opening Youtube Sir")

        if 'open google' in query:
            webbrowser.open("google.com")
            say("Opening Google Sir") 
        
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            say("Opening Notepad Sir")
            
        if "play music" in query:
            music_path = "D:\\songs"
            songs = os.listdir(music_path)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_path, rd))
            say("Playing Music Sir")
        
        if "the time" in query:
           strfTime = datetime.datetime.now().strftime("%H:%M:%S")
           say(f"Sir, The time is {strfTime}")    
                
                #break  # Exit the loop after opening the site
    

        #say(query)

