import datetime
import os
import time
import webbrowser

import pyttsx3
import speech_recognition as sr
import pyautogui as pg
import wikipedia
import functions as func

engine = pyttsx3.init('sapi5')  # Sapi5 is a Microsoft API
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set Male Voice
engine.setProperty("rate", 178)


def speak(audio):
    # Speak the audio string
    engine.say(audio)
    engine.runAndWait()


def wishMe(ai="Jarvis"):
    """
    Wish the user (Good Morning, Good evening...) according to time.
    Returns:
    """
    speak(func.greetHelloInRandomLang())
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Evening!")

    speak(f"I am {ai} Sir. Please tell me how may I help you!")
    return


def echoMode():
    # speak what he listens
    speak("Echo Mode On!")
    query = takeCommand()
    while not "echo mode off" in query:
        speak(query)
        query = takeCommand()

    speak("Echo Mode Off!")
    return


def takeCommand():
    """
    It takes microphone input from the User
    Returns:
        string: convert speech to text and return text as string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # Use Google speech recognition API
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        # print(e) # You Can print the error
        print("Say that again please...")
        return "None"


def openProgram(program_name):
    """
    This function will open any Programme by their name recognized by windows
    Args:
        program_name: name of the programme you want to open

    Returns:
    """
    program_name = program_name.replace("open", "")
    speak("Opening " + program_name)

    if "youtube" in program_name:
        webbrowser.open("youtube.com")
        return

    if "folder" in program_name:
        program_name = program_name.replace("folder", "")
        filepath = os.path.realpath(program_name)
        print("Opening ...", filepath)
        webbrowser.open("file://" + filepath)
        return

    pg.press("Win")
    time.sleep(1)
    pg.write(program_name)
    time.sleep(1)
    pg.keyDown("enter")


def wiki(query, no_of_sentences=3):
    """
        search the query on wikipedia and tell out the summary in given (no_of_sentences) no of lines.
    """
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, no_of_sentences)
    speak("According to Wikipedia")
    speak(results)
    return


def runQueries():
    """
    Takes query from takeCommand function and behave according the query.
    Match the functions with the command which is told user through query.
    Returns:
    """
    while True:
        query = takeCommand().lower()

        if "jarvis" not in query and "alexa" not in query:
            continue

        if "alexa" in query:
            engine.setProperty("voice", voices[1].id)
            if "hello jarvis" in query:
                speak("hello Sir! This is Alexa.")
                query.replace("hello ","")
            query = query.replace("alexa", "")

        elif "jarvis" in query:
            engine.setProperty("voice", voices[0].id)
            if "hello jarvis" in query:
                speak("hello Sir! This is Jarvis.")
                query.replace("hello ","")
            query = query.replace("jarvis", "")

        if "great me" in query or "wish me" in query:
            wishMe()

        elif "open" in query:
            # print(query)
            openProgram(query)  # opening command using pyautogui

        elif "wikipedia" in query:
            wiki(query)

        elif "echo mode on" in query or "eco mode on" in query:
            echoMode()

        elif "play" in query:
            query = query.replace("play ", "")
            # print(query)
            func.playMusicOnYoutube(query)

        elif "screenshot" in query:
            func.takeScreenShot("")
            speak("ScreenShot is saved in Documents folder")


if __name__ == '__main__':
    wishMe()
    runQueries()
