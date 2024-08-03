from config import urls, passwords, logins
from mess import send_message
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import schedule

def wd() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver2 = webdriver.Chrome(options=options)
    for num, url in enumerate(urls):
        login = logins[num]
        password = passwords[num]
        driver.get(url=url)
        driver.find_element(by=By.NAME, value='login').send_keys(login)
        driver.find_element(by=By.NAME, value='password').send_keys(password)
        driver.find_element(by=By.TAG_NAME, value='button').click()
        time.sleep(5)
        work_url = change_link(url)
        driver.get(work_url)
        time.sleep(5)
        try:
            table = driver.find_element(by=By.TAG_NAME, value='tbody')
            users = table.find_elements(by=By.TAG_NAME, value='tr')
            if len(users) > 1:

                users.pop(0)
                for index, user in enumerate(users):
                    name = user.find_elements(by=By.TAG_NAME, value='td')[3].text
                    phone = user.find_elements(by=By.TAG_NAME, value='td')[4].text
                    print(f'[INFO] filial №{num} {name} {phone} DONE')
                    if num == 0 and index == 0:
                        send_message(driver2, num, name, phone, effort = 1)
                    else:
                        send_message(driver2, num, name, phone)
                    
            else:
                value = driver.find_element(by=By.TAG_NAME, value='tbody').find_element(by=By.TAG_NAME, value='tr').text
                print(value)
        except Exception as e:
            print(e)
    driver.quit()
    driver2.quit()


def change_link(url: str) -> str:
    date = datetime.now().strftime('%Y-%m-%d')
    return f'{url}/guests.cards/?from={date}&to={date}'

if __name__ == '__main__':
    schedule.every().day.do(wd)
    while True:
        schedule.run_pending()
        time.sleep(0.1)