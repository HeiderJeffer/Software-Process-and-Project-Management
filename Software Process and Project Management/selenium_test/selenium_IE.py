from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Ie()

browser = driver

browser.get('http://127.0.0.1:8000/admin')
username = 'admin'

print browser.title
print browser.title
print browser.title

textinput = browser.find_element_by_id('id_username')
textinput.send_keys(username)

password = 'password123'
textinput = browser.find_element_by_id('id_password')
textinput.send_keys(password)

browser.find_element_by_id('id_username').send_keys(Keys.RETURN)

sleep(1)

browser.get('http://127.0.0.1:8000/admin/logout')

#browser.close()
 