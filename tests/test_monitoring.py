from utils import navigate_and_authenticate, wait_for_text, find_element_by_text, find_all_elements_by_text, get_hostname
from selenium.webdriver.common.by import By

def test_traefik(browser):
    navigate_and_authenticate(browser, f'https://traefik.{get_hostname()}')
    wait_for_text(browser, 'Success')
    elements = browser.find_elements(
        By.XPATH, '//*[contains(text(), "Success")]/following-sibling::*[contains(text(), "100%")]')
    assert len(elements) >= 3, f"number greater or equal than 3 expected, got: {len(elements)}"

def test_dashboard(browser):
  navigate_and_authenticate(browser, f'https://dashboard.{get_hostname()}')

  wait_for_text(browser, 'Skip')
  find_element_by_text(browser, 'Skip').click()

  wait_for_text(browser, 'CPU Usage (cores)')
  find_element_by_text(browser, 'authelia')
  find_all_elements_by_text(browser, 'Running')

def test_prometheus(browser):
  navigate_and_authenticate(browser, f'https://prometheus.{get_hostname()}')

  wait_for_text(browser, 'Scrape Duration')
  find_element_by_text(
      browser, 'podMonitor/monitoring/traefik-service-monitor/0 (1/1 up)')
  find_element_by_text(
      browser, 'serviceMonitor/ansible-roles/postgres-db/0 (1/1 up)')
  find_element_by_text(
      browser, 'serviceMonitor/ansible-roles/spring-app/0 (1/1 up)')
  find_element_by_text(
      browser, 'serviceMonitor/ansible-roles/client-app/0 (1/1 up)')
  
def test_grafana(browser):
  navigate_and_authenticate(browser, f'https://grafana.{get_hostname()}/admin/users')
  wait_for_text(browser, 'admin')
  wait_for_text(browser, 'admin@localhost')
  wait_for_text(browser, 'Auth Proxy')

def test_grafana_traefik(browser):
  navigate_and_authenticate(browser, f'https://grafana.{get_hostname()}/d/3ipsWfViz')
  wait_for_text(browser, 'Traefik 2')
  wait_for_text(browser, 'authelia-authelia')
  wait_for_text(browser, 'GET')
  wait_for_text(browser, 'POST')
  wait_for_text(browser, '200')

def test_grafana_nginx(browser):
  navigate_and_authenticate(browser, f'https://grafana.{get_hostname()}/d/MsjffzSZz')
  wait_for_text(browser, 'NGINX exporter')
  wait_for_text(browser, 'Up')
  wait_for_text(browser, 'active')
  wait_for_text(browser, 'reading')
  wait_for_text(browser, 'accepted')
  wait_for_text(browser, 'handled')

def test_grafana_java(browser):
  navigate_and_authenticate(browser, f'https://grafana.{get_hostname()}/d/ocFtVC74k')
  wait_for_text(browser, 'JVM (Micrometer)')
  wait_for_text(browser, 'JVM Heap')
  wait_for_text(browser, 'JVM Total')
  wait_for_text(browser, 'used')
  wait_for_text(browser, 'committed')
  wait_for_text(browser, 'max')
