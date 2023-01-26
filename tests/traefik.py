#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text
from selenium.webdriver.common.by import By

with get_browser() as browser:
    navigate_and_authenticate(browser, '/traefik')
    wait_for_text(browser, 'Success')
    elements = browser.find_elements(
        By.XPATH, '//*[contains(text(), "Success")]/following-sibling::*[contains(text(), "100%")]')
    assert len(elements) >= 3, f"number greater or equal than 3 expected, got: {len(elements)}"
