from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
driver = webdriver.Chrome()
driver.get("https://m.facebook.com")

def fb_login():


    driver.find_element_by_id('email').send_keys('minhdq99hp@gmail.com')
    driver.find_element_by_id('pass').send_keys('facebookminh0110')
    driver.find_element_by_id('loginbutton').click()

    page = requests.get('https://m.facebook.com')

    print(page.text)

fb_login()
