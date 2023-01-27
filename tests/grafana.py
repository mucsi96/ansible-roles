#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/grafana/admin/users')
    wait_for_text(browser, 'admin')
    wait_for_text(browser, 'admin@localhost')
    wait_for_text(browser, 'Auth Proxy')
