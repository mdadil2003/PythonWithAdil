# Jarvis voice assistant with speech recognition and text-to-speech

import speech_recognition as sr # For speech recognition
import webbrowser # For opening web pages
import pyttsx3 # Text-to-speech conversion library
import datetime # For telling the time
import musicLibrary # For music playback
import os # For operating system interactions

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function: Process voice commands
def speak(text):
    engine.say(text)
    engine.runAndWait()
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
        
    elif "play" in c:
        # Extract song name after 'play'
        words = c.split()
        try:
            idx = words.index("play")
            song = " ".join(words[idx + 1:]).strip()
        except ValueError:
            song = ""
        
        if not song:
            speak("Please tell me which song you want to play.")
            return
        
        link = musicLibrary.music.get(song) if hasattr(musicLibrary, "music") else None
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have {song} in my library.")
        
    elif "how are you" in c.lower():
        speak("I'm doing great, thank you for asking!")

    elif "exit" in c.lower() or "quit" in c.lower() or "stop" in c.lower():
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Sorry, I didn’t understand that command.")

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
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
    
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except KeyboardInterrupt:
            print("Program interrupted by user")
            break
        except Exception as e:
            print("Error; {0}".format(e))
            speak("Some error occurred. Please try again.")
            continue


# Jarvis voice assistant with speech recognition and text-to-speech
