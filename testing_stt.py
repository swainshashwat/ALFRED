import speech_recognition as sr

# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

print(type(audio))
print("Stopped Listening")
try:
    print("You said: "+ r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))