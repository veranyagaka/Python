from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from dotenv import load_dotenv
import os
load_dotenv()

login_url = os.getenv('LOGIN_URL')
dashboard_url = os.getenv('DASHBOARD_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
logout_but = os.getenv('LOGOUT_BUT')
profile = os.getenv('PROFILE')

driver = webdriver.Chrome()
driver.maximize_window() 
def login():
    username_field = driver.find_element(By.NAME, 'email')
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Sign In")]')
    login_button.click()
    print('Successfully logged in')
    time.sleep(3)
    
def autologin(username, password):
    driver.get(login_url)
    login()
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
    except TimeoutException:
        print("Error: Dashboard element not found")
        driver.quit()
        return
    time.sleep(3)

    driver.get(dashboard_url)
    time.sleep(2)

    try:
        profile_button = driver.find_element(By.XPATH, profile)
        profile_button.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, logout_but))
        )
        logout_button = driver.find_element(By.XPATH, logout_but)
        logout_button.click()
        print('Successfully logged out')
        time.sleep(5) 
        
    except Exception as e:
        print('Logout button not found.')
        print('Error:', e)

for i in range(20):
    autologin(username, password)
driver.quit()
