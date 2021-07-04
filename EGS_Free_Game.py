from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import account

options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)
# options.headless = True   # Активация фонового режима

# options.add_argument( 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like Gecko)
# Chrome/89.0.4389.90 Safari/537.36', )

url = 'https://www.epicgames.com/store/ru'
url_login = 'https://www.epicgames.com/id/login/epic'
print('Webdriver starting...')
browser = webdriver.Firefox(options=options)


def login_egs():
    """Вход в аккаунт"""
    print('Authorization')
    browser.get(url_login)
    try:
        time_to_wait = WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.ID, "email"))
        )
    finally:
        email_input_field = browser.find_element_by_id('email')
        email_input_field.click()
        email_input_field.send_keys(account.email)
        password_input_field = browser.find_element_by_id('password')
        password_input_field.click()
        password_input_field.send_keys(account.password)
    try:
        time_to_wait = WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.ID, "sign-in"))
        )
    finally:
        sign_in_button = browser.find_element_by_id('sign-in')
        sign_in_button.click()


def return_to_main_page():
    """ Возвращение на главную страницу"""
    print('Return to main page')
    try:
        time_to_wait = WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "shieldLogo "))
        )
    finally:
        sign_in_button = browser.find_element_by_class_name('shieldLogo')
        sign_in_button.click()


def search_free_weekly():
    """Поиск еженедельной бесплатной игры"""
    print('Searching for free weekly game')
    free_weekly = browser.find_elements_by_class_name('css-1ihd7u3')
    browser.find_element_by_class_name('css-1ihd7u3').click()


def claim_free_game():
    """ Забираем бесплатную игру """
    print('Claim free game')
    try:
        time_to_wait = WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div[4]/main/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/button"))
        )
    except TimeoutException:
        browser.quit()
    finally:
        claim_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/main/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/button').click()

    # версия 1
    try:
        time_to_wait = WebDriverWait(browser, 10).until(
            ec.frame_to_be_available_and_switch_to_it('dieselReactWrapper')
        )
    finally:
        purchase_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[4]/div/div[4]/div[1]/div[2]/div[5]/div/div/button').click()

    # версия 2


'''
Решение найдено:

browser.switch_to.default_content()
browser.switch_to.window(browser.window_handles[1])
iframe = browser.find_element_by_id("example_id_1")
browser.switch_to.frame(iframe)
wait.until(EC.presence_of_element_located((By.ID, "SomeThing")))
'''

if __name__ == '__main__':
    login_egs()
    return_to_main_page()
    main_page = browser.page_source  # сохраняю html код в переменную
    search_free_weekly()
    claim_free_game()
    # browser.get(url)
    # browser.quit()
