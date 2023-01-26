from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from os import environ

hostname = environ['HOSTNAME']
username = environ['USERNAME']
password = environ['PASSWORD']


def get_browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)


def get_hostname():
    return hostname


def wait_for_text(browser, text):
    WebDriverWait(browser, 5).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, f'//*[contains(text(), "{text}")]')))


def find_element_by_text(browser, text):
    return browser.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')


def navigate_and_authenticate(browser, url):
    full_url = f'https://{get_hostname()}{url}'
    browser.get(full_url)
    wait_for_text(browser, 'Powered by Authelia')

    browser.find_element(By.ID, 'username-textfield').send_keys(username)
    browser.find_element(By.ID, 'password-textfield').send_keys(password)
    browser.find_element(By.ID, 'sign-in-button').click()

    WebDriverWait(browser, 5).until(expected_conditions.url_matches(full_url))
