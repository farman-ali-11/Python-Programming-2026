import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hey my name is Python, I am a programming language. I am here to help you learn programming. Let's have fun learning together!")
engine.runAndWait()
