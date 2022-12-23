from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

browser = driver
browser.get('http://127.0.0.1:8000/admin')
username = 'admin'

textinput = browser.find_element_by_id('id_username')
textinput.send_keys(username)

password = 'password123'
textinput = browser.find_element_by_id('id_password')
textinput.send_keys(password)

browser.find_element_by_id('id_username').send_keys(Keys.RETURN)

browser.get('http://127.0.0.1:8000/admin/logout')

#browser.close()
