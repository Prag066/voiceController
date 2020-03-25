from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class whatsapp_web:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver')
        self.driver.get('https://web.whatsapp.com/')

    def send_msg(self, username=None):
        search_name_by_xpath = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]'
        sleep(5)

        try:
            name = self.driver.find_element_by_xpath(search_name_by_xpath).send_keys(username)
            # Keys.ENTER
            import pyautogui
            pyautogui.press('enter')
        except NoSuchElementException as e:
            print(e)
            self.send_msg(username)
        sleep(5)
        chat_box = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        chat_box.send_keys('hi')
        send_button = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]'
        self.driver.find_element_by_xpath(send_button).click()
        print('message sent')
        self.driver.close()


obj = whatsapp_web()
obj.send_msg(username='prashant')