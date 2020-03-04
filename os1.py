from subprocess import call
import os
#for clear terminal
#call(["clear"])
#for open application
#os.system("subl")
#os.system("vlc bum_diggy.mp4")
#os.system("firefox www.google.com")
#os.system("chromium-browser")
#os.system("skype")
#for supar user access
#os.system("sudo su")
#os.system("root")
#for update & upgrade
#os.system("sudo apt-get update")
#os.system("sudo apt-get upgrade")
#file:///home/chiru/Documents/j[0]
#os.system("subl name.py")

#os.system("vlc bum diggy.mp4")
#call(['vlc','bum diggy.mp4'])
#call(['sudo','su'])
#python=input(':')
#call(['chromium-browser','http://www.google.com/search?btnG=1&q='+python])
#call(['subl','os1.py'])
#call(['xampp start','file:///chiru@dev/opt/lampp'])
#for all saved wifi password
#os.system("sudo grep -r '^psk=' /etc/NetworkManager/system-connections/")
#for connected wifi password
#os.system("sudo grep -hr '^psk=' /etc/NetworkManager/system-connections/")
os.system("MYCWD=`pwd`; cd /etc/NetworkManager/system-connections/ ; sudo grep -e '^psk=' * | less ; cd $MYCWD")
#p id 
#os.system("ps -U")/("ps -A")
#os.system("sudo poweroff")
# cwd
#os.chdir("/opt/lampp")
#os.system("sudo ./xampp start")
#os.system("sudo ./xampp stop")
