from utils import navigate_and_authenticate, wait_for_text, find_element_by_text, find_all_elements_by_text

def test_dashboard(browser):
  navigate_and_authenticate(browser, '/dashboard')

  wait_for_text(browser, 'Skip')
  find_element_by_text(browser, 'Skip').click()

  wait_for_text(browser, 'CPU Usage (cores)')
  find_element_by_text(browser, 'loki-stack-0')
  find_all_elements_by_text(browser, 'Running')
