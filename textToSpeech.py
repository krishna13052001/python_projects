import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


str=input("Enter the string!!  ")

speak(str)