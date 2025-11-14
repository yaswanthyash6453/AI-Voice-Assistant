import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print('Loading your AI personal assistant - Chinnu')

# Text-to-Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello Yashu, Good Morning")
        print("Hello Yashu, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello Yashu, Good Afternoon")
        print("Hello Yashu, Good Afternoon")
    else:
        speak("Hello Yashu, Good Evening")
        print("Hello Yashu, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening…")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")
        except:
            speak("Pardon me, please say that again")
            return "none"
        return statement


# Start Assistant
speak("Loading your AI personal assistant Chinnu")
wishMe()

if __name__ == '__main__':

    while True:

        statement = takeCommand().lower()

        # 🔵 WAKE WORD
        if "hey chinnu" in statement or "hi chinnu" in statement:
            speak("Yes Yashu, I'm listening. Tell me how can I help you?")
            print("Wake word detected!")
            continue

        if statement == "none":
            continue

        # 🔴 EXIT
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Your personal assistant Chinnu is shutting down, Good bye')
            print('Your personal assistant Chinnu is shutting down, Good bye')
            break

        # 🎯 COMMANDS
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Gmail opened")
            time.sleep(3)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                speak(f"Temperature is {current_temp} Kelvin")
                speak(f"Humidity is {current_humidity} percent")
                speak(f"Weather looks like {weather_description}")

                print(f"Temp = {current_temp}\nHumidity = {current_humidity}\nDescription = {weather_description}")

            else:
                speak("City Not Found")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement:
            speak("I am Chinnu Version 1 point 0. Your personal AI assistant, created to help you with tasks like opening apps, searching, checking weather, taking photos, reading news and answering questions.")

        elif 'who created you' in statement:
            speak("I was created by Yashu.")
            print("I was created by Yashu.")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is Stackoverflow")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from The Times of India')
            time.sleep(3)

        elif "take a photo" in statement or "camera" in statement:
            ec.capture(0, "AI Assistant Camera", "photo.jpg")
            speak("Photo taken")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            speak("Searching now")
            time.sleep(3)

        elif 'ask' in statement:
            speak('Ask me any question')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Okay, your PC will log off in 10 seconds.")
            subprocess.call(["shutdown", "/l"])


time.sleep(2)
