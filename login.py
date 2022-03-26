from selenium.common.exceptions import NoSuchElementException
from captchaSolver import solve_captcha
import time


def login(driver, email, password):
    logged_in = False
    while not logged_in:
        driver.get("")
        driver.find_element_by_class_name('btn--blue').click()

        driver.implicitly_wait(5)

        driver.find_element_by_class_name('login-btn').click()

        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)

        solve_captcha(driver)

        time.sleep(5)

        # check if already logged in
        try:
            driver.find_element_by_class_name('header__logged__icons')
        except NoSuchElementException as e:
            driver.close()
        else:
            logged_in = True
            print('logged in = true')
