#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from os import environ

hostname = environ['HOSTNAME']
username = environ['USERNAME']
password = environ['PASSWORD']
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome(options=options) as browser:
    url = f'https://{hostname}/demo'
    browser.get(url)
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located((By.ID, 'username-textfield')))

    browser.find_element(By.ID, 'username-textfield').send_keys(username)
    browser.find_element(By.ID, 'password-textfield').send_keys(password)
    browser.find_element(By.ID, 'sign-in-button').click()

    WebDriverWait(browser, 5).until(expected_conditions.url_matches(url))

    WebDriverWait(browser, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.TAG_NAME, 'body'), 'Hello from Ansible Roles Spring Demo!'))
