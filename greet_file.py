import os
import subprocess
import time_lib

time_object = time_lib.Time_Date()

greet_list = {
    'greet_basic':['hi jarvis','hello jarvis','hey jarvis'],
    'greet_wish':['good morning','good noon','good evening','good night'],
    'greet_extra':[],
    }
inp = 'hi jarvis'

user = subprocess.check_output('whoami',shell=True)
if inp in greet_list['greet_basic']:
    print('hey',user.decode('utf-8'))
    time_greet = time_object.greet_main()
    print(time_greet)

