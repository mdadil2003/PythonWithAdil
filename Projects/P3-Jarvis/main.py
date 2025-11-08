import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2)

            print("Recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Error; {0}".format(e))


    
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
    