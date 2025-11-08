<<<<<<< HEAD
# Jarvis voice assistant with speech recognition and text-to-speech

import speech_recognition as sr # For speech recognition
import webbrowser # For opening web pages
import pyttsx3 # Text-to-speech conversion library
import datetime # For telling the time
=======
import speech_recognition as sr
import webbrowser
import pyttsx3
>>>>>>> 56b7ed0b2fedd59871ab8550144983a8c6354cc0


recognizer = sr.Recognizer()
engine = pyttsx3.init()

<<<<<<< HEAD
# Function: Process voice commands
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    print(c)
# Process the command
=======
def speak(text):
    engine.say(text)
    engine.runAndWait()

>>>>>>> 56b7ed0b2fedd59871ab8550144983a8c6354cc0
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
<<<<<<< HEAD
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

=======
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2)

            print("Recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
>>>>>>> 56b7ed0b2fedd59871ab8550144983a8c6354cc0
        except Exception as e:
            print("Error; {0}".format(e))


<<<<<<< HEAD

    # Jarvis voice assistant with speech recognition and text-to-speech


    
'''

# Jarvis voice assistant with speech recognition and text-to-speech

import speech_recognition as sr  # For speech recognition
import webbrowser  # For opening web pages
import pyttsx3  # Text-to-speech conversion library
import datetime  # For telling the time

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function: Text to Speech
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Function: Process voice commands
def processCommand(c):
    c = c.lower()
    print(f"Command received: {c}")

    if "open youtube" in c:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")

    elif "time" in c:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "how are you" in c:
        speak("I'm doing great, thank you for asking!")

    elif "exit" in c or "quit" in c or "stop" in c:
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Sorry, I didn’t understand that command.")

# Main program
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
            if word.lower() == "jarvis":
                speak("Ya")
                # Listen for the next command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            pass  # No voice detected, keep listening

        except sr.UnknownValueError:
            pass  # Unrecognized speech, ignore

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I didn't catch that.")
            speak("Could you please repeat?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)
                speak("What can I do for you?")
                
'''
=======
    
    # recognizer = sr.Recognizer()
    # microphone = sr.Microphone()
    # tts_engine = pyttsx3.init()

    # with microphone as source:
    #     print("Please say the name of the website you want to visit:")
    #     recognizer.adjust_for_ambient_noise(source)
    #     audio = recognizer.listen(source)

    # try:
    #     command = recognizer.recognize_google(audio)
    #     print(f"You said: {command}")
    #     url = f"https://{command.replace(' ', '')}.com"
    #     webbrowser.open(url)
    #     tts_engine.say(f"Opening {command}")
    #     tts_engine.runAndWait()
    # except sr.UnknownValueError:
    #     print("Sorry, I could not understand the audio.")
    #     tts_engine.say("Sorry, I could not understand the audio.")
    #     tts_engine.runAndWait()
    # except sr.RequestError as e:
    #     print(f"Could not request results; {e}")
    #     tts_engine.say("Could not request results from the speech recognition service.")
    #     tts_engine.runAndWait()
    
>>>>>>> 56b7ed0b2fedd59871ab8550144983a8c6354cc0
