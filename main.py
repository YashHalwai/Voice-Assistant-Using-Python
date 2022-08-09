# Voice Assistant Using Python

from ast import Try
from email.mime import audio
from logging.config import listen
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")    

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    if "hello lap" in sptext().lower():
        
        while True:
            
          data1 = sptext().lower()
        
          if "your name" in data1:
            name = "my name is lap"
            speechtx(name)
            
          elif "old are you" in data1:
             age = "i am two years old"    
             speechtx(age)
            
          elif 'time' in data1:
             time = datetime.datetime.now().strftime("%I:%M%p")
             speechtx(time)
            
          elif 'youtube' in data1:
             webbrowser.open("https://www.youtube.com/")
                
          elif 'github' in data1:
             webbrowser.open("https://github.com/YashHalwai")  
            
          elif "joke" in data1:
             joke_1 = pyjokes.get_joke(language="en",category="neutral")     
             speechtx(joke_1)     
            
          elif 'song' in data1:
             add ="D:\songs\Hindi Songs"
             listsong = os.listdir(add)
             print(listsong)
             os.startfile(os.path.join(add,listsong[5]))
             
          elif "exit" in data1:
              speechtx("thank you")
              break 
          
          time.sleep(7)

else:
    
    print("thanks")          