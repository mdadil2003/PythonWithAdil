# Jarvis voice assistant with speech recognition and text-to-speech

import speech_recognition as sr # For speech recognition
import webbrowser # For opening web pages
import pyttsx3 # Text-to-speech conversion library
import datetime # For telling the time


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
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                    # listen for the next command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
 
                    processCommand(command)
    
        except Exception as e:
            print("Error; {0}".format(e))


# Jarvis voice assistant with speech recognition and text-to-speech
