# Write a Python program to change the voice of the text using pyttsx3 module.


# Import the pyttsx3 module
import pyttsx3
# Initialize the TTS engine
engine = pyttsx3.init()

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# Test the voice
engine.say("Hello, Voice is a test.")
engine.runAndWait()