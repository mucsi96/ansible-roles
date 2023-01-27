#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/grafana/d/MsjffzSZz')
    wait_for_text(browser, 'NGINX exporter')
    wait_for_text(browser, 'Up')
    wait_for_text(browser, 'active')
    wait_for_text(browser, 'reading')
    wait_for_text(browser, 'accepted')
    wait_for_text(browser, 'handled')
