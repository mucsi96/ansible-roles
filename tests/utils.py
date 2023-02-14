from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from os import getenv, makedirs
from selenium.webdriver.remote.webdriver import WebDriver
from ansible.parsing.vault import VaultLib, VaultSecret
from ansible.constants import DEFAULT_VAULT_ID_MATCH
from pathlib import Path
from yaml import safe_load
from shutil import rmtree

current_directory = Path(__file__).parent
reports_directory = current_directory / "../reports"
rmtree(reports_directory, ignore_errors=True)
makedirs(reports_directory, exist_ok=True)

def read_utf8_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        print("Error reading file at", file_path)

def read_file(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except:
        print("Error reading file at", file_path)

def take_screenshot(browser: WebDriver, test_name: str):
    browser.save_screenshot(reports_directory / f'{test_name}.png')


def get_browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    return driver


def wait_for_text(browser: WebDriver, text: str):
    WebDriverWait(browser, 5).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, f'//*[contains(text(), "{text}")]')))


def find_element_by_text(browser: WebDriver, text: str):
    return browser.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')


def find_all_elements_by_text(browser: WebDriver, text):
    return browser.find_elements(By.XPATH, f'//*[contains(text(), "{text}")]')


def navigate_and_authenticate(browser: WebDriver, url: str):
    vault_secret = read_file(current_directory / '../.ansible/vault_key')
    vault = VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_secret))])
    vault_text = read_utf8_file(current_directory / '../vars/vault.yaml')
    data = safe_load(vault.decrypt(vault_text))
    public_domainname = data['public_domainname']
    username = data['username']
    password = data['password']
    subdomain = getenv("SUBDOMAIN") if getenv("SUBDOMAIN") is not None else "ansible-roles"
    hostname = f'{subdomain}.{public_domainname}'

    full_url = f'https://{hostname}{url}'
    browser.get(full_url)
    wait_for_text(browser, 'Powered by Authelia')

    browser.find_element(By.ID, 'username-textfield').send_keys(username)
    browser.find_element(By.ID, 'password-textfield').send_keys(password)
    browser.find_element(By.ID, 'sign-in-button').click()

    WebDriverWait(browser, 5).until(expected_conditions.url_matches(full_url))
