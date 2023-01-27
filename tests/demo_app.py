#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/demo')
    wait_for_text(browser, 'Hello from Ansible Roles Spring Demo!')
