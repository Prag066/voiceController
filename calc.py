import time
print('these are the commands for use to calculate..')
print(' add , sub , multi , div , reminder ')
print('ready to use calculator')
sleep=time.sleep(10)
class calculate(object):
	x=None
	y=None
	def add(self,x,y):
		return x+y;
	def sub(self,x,y):
		return x-y;
	def multi(self,x,y):
		return x*y;
	def div(self,x,y):
		return x/y;
	def remn(self,x,y):
		return x%y;

try:
	obj1=calculate()
	usr=input('add multi div sub ?').lower()
	p=int(input('first input:'))
	q=int(input('2nd input:'))
	if usr=='add':
		print(obj1.add(p,q))
	elif usr=='sub':
		print(obj1.sub(p,q))
	elif usr=='multi':
		print(obj1.multi(p,q))
	elif usr=='div':
		print(obj1.div(p,q))
	elif usr=='reminder':
		print(obj1.remn(p,q))
	else:
		print('you are trying !command not found')
except ValueError:print('you enterd invalid number')
