import os
import speech_recognition as sr

with sr.Microphone as source:
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()
	recognizer.adjust_for_ambient_noise(source)
	audio=recognizer.listen(source)
	user=recognizer.recognize_google(audio)
	print(user)
def tictok_game():
	import tictok
def random_no_game():
	import rando
def calculate():
	import calc
def send_mail():
	import gmail_send1
