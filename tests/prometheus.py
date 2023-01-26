#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(
        browser, '/prometheus/targets')
    wait_for_text(browser, 'Scrape Duration')
    find_element_by_text(
        browser, 'podMonitor/monitoring/traefik-service-monitor/0 (1/1 up)')
    find_element_by_text(
        browser, 'serviceMonitor/ansible-roles/spring-app/0 (1/1 up)')
