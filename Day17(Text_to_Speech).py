# Import text to speech python module
# Pyttsx3 -> it works offline

import pyttsx3

# Create a pyttsx3 object

engine = pyttsx3.init()

# See voices my machine has
#-------------------------------------------
# for voice in engine.getProperty("voices"):
#     print(voice)
#---------------------------------------------
# <Voice id=french
#           name=french
#           languages=[b'\x05fr-fr']
#           gender=male
#           age=None>

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[10].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


text = input('Enter any text to convert to speech: ')

speak(text)

# Is encounter aplay error
# Run sudo apt install alsa-utils   