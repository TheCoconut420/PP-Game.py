# pip install selenium
# install Chrome/ChromeDriver
#https://www.google.com/intl/de_de/chrome/
#https://sites.google.com/chromium.org/driver/
#Drop the driver file to "C:\Program Files(x86)

from argparse import Action
from webbrowser import Chrome
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)
action = ActionChains(driver)

def login(site):
    if site == "1":
        username = "username"
        password = "password"
        driver.get("https://hb.itslearning.com")
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Username_input").send_keys(username)
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Password_input").send_keys(password)
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_nativeLoginButton").click()
    elif site == "2":
        username = "username"
        password = "password"
        driver.get("https://cissa.webuntis.com/WebUntis/?school=SZ+II+Utbremen#/basic/login")
        driver.find_element(By.CLASS_NAME, "un-input-group__input").send_keys(username)
        driver.find_element(By.CLASS_NAME, "un-input-group__input").send_keys(Keys.TAB, password, Keys.TAB, Keys.TAB, Keys.ENTER)
        time.sleep(3)
        for i in range (0,4):
            action.send_keys(Keys.TAB).perform()
        action.send_keys(Keys.ENTER).perform()
login(input("1 for hb.itslearning.com, 2 for cissa.webuntis.com: "))