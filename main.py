import time

import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



from time import  sleep
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser = Service("C:\\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get("https://twitter.com/i/flow/login")
    driver.maximize_window()
    sleep(5)
    login.login_fn(driver)

    driver.get("https://twitter.com/edgarm_v/likes")

    sleep(5)
    page_cards = driver.find_elements(By.XPATH, '//div[@data-testid="like"]')

    driver.execute_script("arguments[0].click();", page_cards[0]);


    for card in page_cards:
        print(card)
    sleep(9*1000)

