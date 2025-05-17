# pip install pyaudio
import speech_recognition as sr # pip install speechrecognition
import pyttsx3 # pip install pyttsx3
import webbrowser
from musiclibrary import music
from gtts import gTTS # pip install gTTS
import google.generativeai as genai
import pygame # pip install pygame 
import os

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    try:
        pygame.mixer.init() # initializes pygame mixer
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()  # Play indefinitely
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except pygame.error as e:
        print(f"Error loading or playing music: {e}")


def aiprocess(command):
    

    # Replace with your actual API key
    genai.configure(api_key="AIzaSyC9_1nhVulsVbGd8gzKFZDod54bWfEmZCM")

    # Select a Gemini model
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Send a request
    response = model.generate_content(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
            parts = c.lower().split(" ")
            if len(parts) > 1:
                song = " ".join(parts[1:])  # Handle song names with multiple words
                if song in music:
                    link = music[song]
                    webbrowser.open(link)
                else:
                    speak(f"Sorry, I don't have the song '{song}' in your library.")
            else:
                speak("Please tell me which song you would like to play.")
    else:
        #Let AI handle the request
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis....")

while True:
    
    # obtain audio from the microphone
    r = sr.Recognizer()
   
    print("Recognizing....")
    # recognize speech using Google
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5,phrase_time_limit=3) # Listen takes time out parameter and phase_time_limit parameter
        
        word = r.recognize_google(audio)
        if (word.lower()== "jarvis"):
            speak("Yes Please!")
            #Listen to the command
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                command = r.recognize_google(audio)
                processCommand(command)

    except Exception as e:
        print("Error; {0}".format(e))