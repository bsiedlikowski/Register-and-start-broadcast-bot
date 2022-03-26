import time


def start(driver):
    driver.get("/start_transmission")
    time.sleep(20)
    # refresh
    driver.get("/start_transmission")
    time.sleep(15)

    driver.implicitly_wait(5)
    driver.find_element_by_class_name('photo-btn').click()
    driver.find_element_by_class_name('micro-btn').click()

    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div/div/div/form/div/div/input').send_keys('Example broadcast description')
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div/div/div/form/div/button').click()

    print('Stream is live')
