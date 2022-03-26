from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from captchaSolver import solve_captcha
import time


def register(driver, username, password):
    driver.get("")
    main = driver.current_window_handle
    time.sleep(2)

    driver.execute_script("window.open()")
    temp_mail = driver.window_handles[1]
    driver.switch_to.window(temp_mail)
    driver.get("https://tempmail.dev/en#")
    time.sleep(5)

    email = driver.find_element_by_id('current-mail').text
    print(email)

    driver.switch_to.window(main)
    driver.find_element_by_class_name('btn--blue').click()

    driver.implicitly_wait(5)

    driver.find_element_by_class_name('register-btn').click()

    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('password2').send_keys(password)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_xpath('//*[@id="registerModal"]/div/div/form/div[5]/label').click()
    driver.find_element_by_xpath('//*[@id="registerModal"]/div/div/form/div[7]/label').click()
    regulations = driver.find_elements_by_xpath('//*[@id="registerModal"]/div/div/form/div[8]/label')[0]
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(regulations, 5, 5)
    action.click()
    action.perform()

    solve_captcha(driver)

    driver.switch_to.window(temp_mail)
    time.sleep(12)
    driver.find_element_by_xpath('//*[@id="inbox-dataList"]').click()
    driver.find_element_by_xpath('//*[@id="ReadContent"]/table/tbody/tr/td/div[5]/div/div/div/div/div/a/div/div/span').click()

    driver.quit()

    return email
