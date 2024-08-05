from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from config import login, password
import logging




def log_in(driver: Chrome) -> None:
        driver.get('https://admin.revvy.ru/auth')
        time.sleep(10)
        driver.find_element(by=By.ID, value='input-email').send_keys(login)
        driver.find_element(by=By.ID, value='input-password').send_keys(password)
        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
        time.sleep(5)

        
def send_message(driver: Chrome, num: int, name:str, phone:str) -> None:
    driver.get('https://admin.revvy.ru/')
    time.sleep(5)
    driver.get('https://admin.revvy.ru/pages/request-feedback')
    time.sleep(5)
    driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
    if num == 0:
        driver.find_element(by=By.ID, value='nb-option-3').click()
        time.sleep(2)
    elif num == 1:
        driver.find_element(by=By.ID, value='nb-option-4').click()
        time.sleep(2)
    elif num == 2:
        driver.find_element(by=By.ID, value='nb-option-2').click()
        time.sleep(2)
    driver.find_element(by=By.ID, value='name').send_keys(name)
    driver.find_element(by=By.ID, value='phone').send_keys(phone)
    time.sleep(3)
    # driver.find_elements(by=By.TAG_NAME, value='button')[2].click()
    # time.sleep(3)
    logging.info('Message send')


