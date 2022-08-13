#import necessary libraries.
import time
import pyttsx3 

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id) 
# You might decide to use engine.setProperty('voice', voices[1].id) 
# if you need a different voice (female) but default is [0] which is a male
engine.setProperty("rate", 150) 
# You might choose to increase the speed/rate of the voice of you want by increasing the number {150}



# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()



print("\n\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("================================================================================================")
print("What is your name?")
name = input()

print("This code was written by Godspower Maurice AKA AnthemPython and its going to be telling you how old you are...")
time.sleep(4)
print("Initializing CODE....., PLEASE WAIT FOR 4 SECONDS......")
speak("Initializing CODE....., PLEASE WAIT FOR 4 SECONDS......")

time.sleep(4)
print("Please enter your year of birth")
speak("Please enter your year of birth")
actual = int(input())
age = str(2022 - actual)
print("Resolving Code..................")
time.sleep(2)
print("........................................")
time.sleep(2)
print("Collecting Results............................")
speak("Collecting Results............................")
time.sleep(3)
print("\n\n")
print("You are or will be " + age + " years old this year.")
speak("You are or will be " + age + " years old this year.")
print("\nThank you for using this tools")