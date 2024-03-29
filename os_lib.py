import os

class OsMethods:
    def poweroff(self):
        power_off = os.system("sudo poweroff")
        return power_off
    def shutdown(self):
        power_off = os.system("sudo shutdown now")
        return power_off

    def wifi_password_list(self):
        wifi = os.system("MYCWD=`pwd`; cd /etc/NetworkManager/system-connections/ ; sudo grep -e '^psk=' * | less ; cd $MYCWD")
        return wifi

    def full_update(self):
        os.system("sudo apt-get update")
        os.system("sudo apt-get upgrade -y")
        return "updated"

    def apt_install(self,package):
        my_package = 'sudo apt-get install {0} -y'.format(package)
        os.system(my_package)
        return 'installed {0}'.format(package)

    def current_directory(self):
        dir = os.system('os.getcwwd()')
        return dir

    def sublime(self,filename):
        subl = 'subl {0}'.format(filename)
        os.system(subl)
        return 'opening sublime'

    def firefox(self,website='www.google.com'):
        fox = 'firefox {0}'.format(website)
        os.system(fox)
        return 'opening firefox'

    def disk_sizes(self):
        sizes = os.system('df -h -x squashfs')
        return sizes

    def kill_process(self,pid):
        if(pid):
            kill = 'ps -e | grep {0}'.format(pid)
            os.system(kill)
            return 'closed'
        else:
            os.system('xkill')

    def find_file(self,name=None,path='/home/chiru/'):
       # file = 'find {0}'.format(name)
       # return os.system(file)
        os.chdir(path)
        for roots,dirs,files in os.walk(path):
            for file in files:
                if name in file:
                    return roots+"/"+file
                    break
                else:
                    pass
    def find_dir(self,name=None,path='/home/chiru/'):
        os.chdir(path)
        for roots,dirs,files in os.walk(path):
            for dir in dirs:
                if name in dir:
                    print( roots+name+"/")
                    my_path = roots+name+"/"
                    command = 'xdg-open '+my_path
                    os.system(command)
                    # break
                else:
                    pass

    def clear_screen(self):
        return os.system('clear')

    def exit(self):
        exit = os.system('exit')
        return 'bye'



# o=OsMethods()
# print(o.find_dir('Downloads'))
