from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import json





def facebook_login():
    driver = webdriver.Chrome("C:\Python27\chromedriver_win32\chromedriver.exe")
    driver.get('https://facebook.com')
    driver.maximize_window()
    element = driver.find_element_by_id('email').send_keys('')
    element = driver.find_element_by_id('pass').send_keys('')
    element = driver.find_element_by_id('loginbutton').click()
    
    sleep(2)
    return element

element = facebook_login()

#driver.get('https://accounts.google.com')


def gmail_login():
    
    driver1 = webdriver.Chrome("C:\Python27\chromedriver_win32\chromedriver.exe")
    #driver1.execute_script('''window.open("https://accounts.google.com")''')
    driver1.get('https://accounts.google.com')
    
    driver1.maximize_window()
    driver1.implicitly_wait(9)
    
    emailElem = driver1.find_element_by_id('identifierId')
    emailElem.send_keys('')
    nextButton = driver1.find_element_by_id('identifierNext')
    nextButton.click()
    time.sleep(1)
    passwordElem = driver1.find_element_by_name('password')
    passwordElem.send_keys('')
    signinButton = driver1.find_element_by_id('passwordNext')
    signinButton.click()
    return emailElem, nextButton, passwordElem, signinButton

emailElem, nextButton, passwordElem, signinButton = gmail_login()











