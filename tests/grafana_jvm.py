#!/usr/bin/env python3
from utils import navigate_and_authenticate, get_browser, wait_for_text, find_element_by_text

with get_browser() as browser:
    navigate_and_authenticate(browser, '/grafana/d/ocFtVC74k')
    wait_for_text(browser, 'JVM (Micrometer)')
    wait_for_text(browser, 'JVM Heap')
    wait_for_text(browser, 'JVM Total')
    wait_for_text(browser, 'used')
    wait_for_text(browser, 'committed')
    wait_for_text(browser, 'max')
