import ctypes
import subprocess
import pyjokes as pyjokes
import pyttsx3
import datetime  #Library related to date and time functions
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id) #For male voice use 0


def speak(audio): #To speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir!")

    elif hour >= 10 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Zara Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and return string output.
    r = sr.Recognizer() #Recogniser class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query= takeCommand().lower()
        if 'wikipedia' in query: #Wikipedia is a keyword. If user doesn't say that, it will not work.
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            # print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\New songs' #\\ slash is to escape the character
            songs = os.listdir(music_dir)  #listdir is used to enlist all the songs of mentioned directory
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) #song[0] will play the first song using randmodule, song can be suffled

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime}")


        elif 'open pycharm' in query:
            pycharm="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin"
            os.startfile(pycharm)

        elif 'open code' in query:
            codePath="C:\\Users\\Shahnawaz Khan\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shahnawaz.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Shahnawaz")

        elif 'reason for you' in query:
            speak("I was created as a Major project by Mister Shahnawaz ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0, "Location of wallpaper", 0)
            speak("Background changed succesfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'sleep' in query:
            exit()
















