a = input("Enter Username ")
b = input("Enter password ")
c = input("Enter student ID ")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import wget
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
searchbox = driver.find_element_by_name('q')
searchbox.send_keys("KNUST student portal")
searchbox.send_keys(Keys.RETURN)
portal = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()

username = driver.find_element_by_id("username")
username.send_keys(a)

password = driver.find_element_by_id("password")
password.send_keys(b)

studentid = driver.find_element_by_id("studentid")
studentid.send_keys(c)
driver.find_element_by_id("sign_in_button").click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[5]/a').click()
driver.find_element_by_id("ACADYEAR").click()
driver.find_element_by_id("SEM")
driver.find_element_by_id("displayresult").click()






