import time
from twocaptcha import TwoCaptcha


def solve_captcha(driver):
    solver = TwoCaptcha('')

    try:  # solve captcha
        result = solver.recaptcha(
            sitekey='',
            url='',
            invisible=1)
    except Exception as e:
        print(e)
    else:
        print("Recaptcha result: " + result['code'])
        token = result['code']

    write_token_js = f'document.getElementById("g-recaptcha-response").innerHTML = "{token}";'
    driver.execute_script(write_token_js)
    time.sleep(5)
    try:  # excute callback function
        callback_js = f'___grecaptcha_cfg.clients[0].Y.Y.callback("{token}");'
        driver.execute_script(callback_js)
        time.sleep(3)
    except Exception as e:
        print(e)
    else:
        print('Recaptcha is solved!')



