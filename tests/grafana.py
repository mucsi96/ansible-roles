#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/grafana/d/3ipsWfViz')
    wait_for_text(browser, 'Traefik 2')
    find_element_by_text(browser, 'ansible-roles-client-app-route')
    find_element_by_text(browser, 'authelia-authelia')
    find_element_by_text(browser, 'GET')
    find_element_by_text(browser, 'POST')
    find_element_by_text(browser, '200')
