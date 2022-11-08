from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import  sleep
from decouple import  config

def login_fn(driver):

    username = driver.find_element(By.NAME, 'text')
    username.send_keys(config("USERTWITTER"))
    username.send_keys(Keys.RETURN)
    sleep(5)

    username = driver.find_element(By.NAME, 'password')
    username.send_keys(config("PASSWORD"))
    username.send_keys(Keys.RETURN)

    driver.get("https://twitter.com/edgarm_v")
