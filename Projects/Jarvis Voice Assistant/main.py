# Jarvis voice assistant with speech recognition and text-to-speech

import speech_recognition as sr # For speech recognition
import webbrowser # For opening web pages
import pyttsx3 # Text-to-speech conversion library
import datetime # For telling the time
import musicLibrary # For music playback
import requests # For making HTTP requests
from openai import OpenAI # OpenAI API client
from gtts import gTTS # Google Text-to-Speech
import os # For operating system interactions
import pygame # For playing audio files


recoognizer = sr.Recognizer() # Initialize the recognizer
engine = pyttsx3.init() # Initialize the TTS engine
newsapi = " key " # News API key

# Function: Process voice commands
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()   # initialize mixer
    pygame.mixer.music.load('temp.mp3')  # load file
    pygame.mixer.music.play()      # play file

    while pygame.mixer.music.get_busy():  # keep script running
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')
    
    
def aiProcess(command):
    client = OpenAI(api_key="paste-your-openai-api-key-here ",
    )

    completion =client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content  
    
def processCommand(c):
    if "open youtube" in c.lower():
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        
    elif "open google" in c.lower():
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
            
    elif "open facebook" in c.lower():
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")
        
    elif "open github" in c.lower():
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")

    elif "time" in c.lower():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        
    elif "play music" in c:
        # Extract song name after 'play'
        words = c.split()
        try:
            idx = words.index("play music")
            song = " ".join(words[idx + 1:]).strip()
        except ValueError:
            song = " "
        
        if not song:
            speak("Please tell me which song you want to play.")
            return
        
        link = musicLibrary.music.get(song) if hasattr(musicLibrary, "music") else None
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have {song} in my library.")
            
    elif "news" in c.lower():
         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
         if r.status_code == 200:
             data = r.json()            
             
             articles = data.get('articles', [])
             
             for article in articles:
                    speak(article['title'])
    else:
        # Use AI to process other commands                       
        output = aiProcess(c)
        speak(output)
        
    # elif "how are you" in c.lower():
    #     speak("I'm doing great, thank you for asking!")

    # elif "exit" in c.lower() or "quit" in c.lower() or "stop" in c.lower():
    #     speak("Goodbye! Have a nice day.")
    #     exit()

    # else:
    #     speak("Sorry, I didn’t understand that command.")



# Process the command
# Main program loop
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("jarvis Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes, how can I help you?")
                # listen for the next command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)             
                    
                    
        except Exception as e:
            print("Error; {0}".format(e))
            speak("Some error occurred. Please try again.")
