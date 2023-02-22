import os
import webbrowser
import sys
import subprocess
import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)   #скорость разговора

def speaker(text):
    engine.say(text)
    engine.runAndWait()
    
def browser():
	webbrowser.open('https://www.youtube.com', new=2)

def game():
	subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
	
def offpc():
    os.system('shutdown/s')  #Выключение
print('PC  выключен')

def weather():
    params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
    w = response.json()
    speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		

def offBot():
	sys.exit()


def passive():
	pass
