import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 133)
engine.say(
    "We are Anonymous, We Are Legion, We don't forgive, We don't forget, Expect us!")
engine.runAndWait()
