from selenium import webdriver
from datetime import datetime
import telegram_send
import time
import os
import sys
from register import register
from login import login
from startTransmission import start
from dataGenerator import generate_username
from dataGenerator import generate_password

# if executed as bundled exe
if getattr(sys, 'frozen', False):
    PATH = os.path.join(sys._MEIPASS, '\chromedriver.exe')
else:
    PATH = '\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('use-fake-ui-for-media-stream')
options.add_argument('window-size=1920,1080')
options.add_argument('start-maximized')
# options.add_argument('headless')


while True:
    start_time = datetime.now()
    start_time = start_time.replace(microsecond=0)

    is_registered = None
    is_started = None

    # try to register until successful
    while not is_registered:
        driver = webdriver.Chrome(executable_path=PATH,options=options)
        try:
            username = generate_username()
            password = generate_password()
            email = register(driver,username,password)
        except Exception as e:
            print(e)
            driver.quit()
            pass
        else:
            is_registered = True

    # try to start stream until successful
    while not is_started:
        driver = webdriver.Opera(executable_path=PATH,options=options)
        try:
            login(driver, email, password)

            start(driver)

            end_time = datetime.now()
            end_time = end_time.replace(microsecond=0)
            execution_time = end_time - start_time
            telegram_send.send(messages=["\U0001F534 STREAM IS LIVE | " + '{}'.format(execution_time)])

            time.sleep(300)
            driver.quit()
        except Exception as e:
            print(e)
            print("Restarting!")
            driver.quit()
            pass
        else:
            is_started = True
