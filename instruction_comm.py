import speech_recognition as sr
import os

import tts_response
import os_lib 
import time_lib

# url_reg = \b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b

osMethod = os_lib.OsMethods()
timeMethod = time_lib.Time_DateMethod()

# def tictok_game():
# 	import tictok
# def random_no_game():
# 	import random_number_game
# def calculate():
# 	import calc
# def send_mail():
# 	import gmail_send1
def user_greet():
	import greet_file


while True:
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()
	with microphone as source:
		tts_response.speak_response('say something')
		# print('say something')
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
		print('i think you said ',recognizer.recognize_google(audio))
		user = recognizer.recognize_google(audio)
		if user == 'hai':
			user_greet()
		elif user == 'find folder downloads':
			osMethod.find_dir('Downloads')
		elif user == 'install tree':
			print('installing tree')
			osMethod.apt_install('tree')
		elif user == 'update full system':
			osMethod.full_update()
		elif user == 'shutdown':
			osMethod.shutdown()
		elif user == 'show Wi-Fi password list':
			osMethod.wifi_password_list()
		elif user == 'kill process':
			osMethod.kill_process()
		elif user == 'wait':
			timeMethod.sleep()
		elif user == 'time':
			timeMethod.current_time()
		elif user == 'open firefox':
			osMethod.firefox()
		elif user == 'sublime':
			osMethod.sublime()
		elif user == 'bye':
			quit()
	except sr.UnknownValueError:
		print('not understand your command')
	except sr.RequestError as e:
		print('error {0}'.format(e))
		break


