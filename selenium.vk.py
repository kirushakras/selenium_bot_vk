import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
print("You mail or number")
login = str(input())
print("You password")
pas = str(input())
print("adres of you interlocutor")
vk_com =
mes = []#several elements to prevent captcha
driver = webdriver.Chrome(executable_path='') 
driver.set_window_size(1366, 768)
driver.implicitly_wait(20)
driver.get('https://vk.com')
time.sleep(10)
username = driver.find_element_by_id('index_email')
username.clear()
username.send_keys(login)
password = driver.find_element_by_id('index_pass')
password.clear()
password.send_keys(pas)
log = driver.find_element_by_id('index_login_button')
log.click()
me = random.choice(mes)
driver.get(vk_com)
message_op = driver.find_element_by_class_name('profile_btn_cut_left')
message_op.click()
text = driver.find_element_by_id('mail_box_editable')
text.send_keys(me)
send = driver.find_element_by_class_name('mail_box_send_btn')
send.click()
i = 0
try:
while i < 1000:
    me = random.choice(mes)
    driver.get(vk_com)
    message_op = driver.find_element_by_class_name('profile_btn_cut_left')
    message_op.click()
    text = driver.find_element_by_id('mail_box_editable')
    text.send_keys(me)
    send = driver.find_element_by_class_name('mail_box_send_btn')
    send.click()
    time.sleep(5)
    i = i+1
except Exception:
    os.system('say "We have some problem"')
