from utils import navigate_and_authenticate, get_hostname, wait_for_text

def test_demo_app(browser):
    navigate_and_authenticate(browser, f'https://demo.{get_hostname()}')
    wait_for_text(browser, 'Hello from Ansible Roles Spring Demo!')
