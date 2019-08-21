from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import json, re

with open('data.json') as f:
    data = json.load(f)

username = data['username']
password = data['password']

# Selecting UBC and proceeding to login
driver = webdriver.Chrome("./driver/chromedriver.exe")
driver.get("https://upassbc.translink.ca")
selectMenu = Select(driver.find_element_by_id('PsiId'))
selectMenu.select_by_visible_text('University of British Columbia')
submitButton = driver.find_element_by_id('goButton')
submitButton.click()

# Entering username and password
userElem = driver.find_element_by_id('username')
userElem.send_keys(username)
passElem = driver.find_element_by_id('password')
passElem.send_keys(password)
loginButton = driver.find_element_by_name('_eventId_proceed')
loginButton.click()

# If there's MFA enabled
pattern = re.compile("https://upassbc.translink.ca[/[.]*]?")
if not re.match(r"https://upassbc.translink.ca[/[.]*]?", driver.current_url):
    driver.switch_to_frame(driver.find_element_by_id("duo_iframe"))

