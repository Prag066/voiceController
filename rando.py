import random
secretno=random.randint(1,20)
print('i am thinking of a no. b/w 1 to 20')
def validate(guess):
 	if guess<0:
 		raise ValueError
 		print('should be a positive number')
 	else:
 		return guess
try:
	for guesstake in range(1,7):
		print('take a guess')
		usr=int(input('choose guess:'))
		guess=validate(usr)
		if guess<secretno:
			print('your guess is low')
			print('nope no. is not right')
		elif guess>secretno:
			print('your guess is high')
			print('nope no. is not right')
		elif guess==secretno:print('good job right ans in '+str(guesstake)+' guesses')
		else:
			break
except ValueError:print('no. is not valide')
print("right one is %d"%secretno)
