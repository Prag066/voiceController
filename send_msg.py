from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
from Main_auth import cred

opts = Options()
opts.set_headless()
assert opts.headless

url = 'https://www.way2sms.com/'
Myxpaths = {
    'username':'//*[@id="mobileNo"]',
    'password':'//*[@id="password"]',
    'login_button':'/html/body/div[6]/div[2]/div/div[3]/form/div[2]/div[2]/button',
    'mobile_to_send_message':'//*[@id="mobile"]',
    'message':'//*[@id="message"]',
    'send_button':'//*[@id="sendButton"]',
}
user_id=cred['u_way2sms']
user_pass=cred['p_way2sms']
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

username = driver.find_element_by_xpath(Myxpaths['username'])
password = driver.find_element_by_xpath(Myxpaths['password'])
login_button = driver.find_element_by_xpath(Myxpaths['login_button'])

time.sleep(3)

username.send_keys(user_id)
password.send_keys(user_pass)
login_button.click()

time.sleep(3)

mobile_to_send_message=driver.find_element_by_xpath(Myxpaths['mobile_to_send_message'])
message=driver.find_element_by_xpath(Myxpaths['message'])
send_button=driver.find_element_by_xpath(Myxpaths['send_button'])
mobile_to_send_message.send_keys('9125970365')
message.send_keys('hi checking')
send_button.click()
