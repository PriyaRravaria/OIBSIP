import pyttsx3
import wikipedia
voice=pyttsx3.init()
input=input("Searching wikipedia/Google:")
result=wikipedia.summary(input,sentences=4)
print(result)
voice.say(result)
voice.runAndWait()