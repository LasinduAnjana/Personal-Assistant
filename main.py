import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('rate', 175)


def speak(text):
    time.sleep(0.1)
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    r = requests.get(url)
    json_data = r.json()
    setup = json_data["setup"]
    punchline = json_data["punchline"]
    print(setup + " " + punchline)
    speak(setup)
    time.sleep(1)
    speak(punchline)


print("Loading your AI personal assistant Moon")
speak("Loading your AI personal assistant Moon")
wish_me()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = take_command().lower()
        if statement == 0:
            continue
        if "goodbye" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Moon is shutting down, Good bye')
            print('your personal assistant Moon is shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("http://www.dailymirror.lk/top-storys/155")
            speak('Here are top stories from dailymirror, Happy reading')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "joke" in statement:
            tell_joke()

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = take_command()
            app_id = "Paste your unique ID here "
            client = wolframalpha.Client('2RWQVX-67UAJ5T6QQ')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am moon version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow ,predict time,search wikipedia,'
                  'predict weather, In different cities, get top headline news from DailyMirror and'
                  ' you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Lasindu Karunarathna")
            print("I was built by Lasindu Karunarathna")

        elif "weather" in statement:
            api_key = "4260e32df7bcf675e9654c615cf379ea"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            # speak("what is the city name")
            city_name = "ambalangoda"
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            q = response.json()
            print(q)
            if q["cod"] != "404":
                x = q["main"]
                current_temperature = x["temp"]
                current_humidiy = x["humidity"]
                y = q["wind"]
                wind_speed = y["speed"]
                z = q["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in Celsius unit is " +
                      str(round(current_temperature - 273.15)) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description) +
                      "\n wind speed" +
                      str(wind_speed))

                print(" Temperature in celsius unit = " +
                      str(round(current_temperature - 273.15)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description) +
                      "\n wind speed" +
                      str(wind_speed))



# elif "log off" in statement or "sign out" in statement:
#     speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
#     subprocess.call(["shutdown", "/l"])

    time.sleep(3)
