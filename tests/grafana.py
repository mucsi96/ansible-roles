#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/grafana/d/6be0s85Mk')
    wait_for_text(browser, 'Grafana Overview')
    wait_for_text(browser, 'Dashboards')
    wait_for_text(browser, '200')
    wait_for_text(browser, '304')
    wait_for_text(browser, '500')
