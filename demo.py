import pytest
import time

def test_google_cats(browser):
    browser.get('https://google.com')
    time.sleep(1)
    # browser.wait_for('span', "i'm feeling lucky")
    browser.send('cats typing\n')
    browser.click('a', 'images for cats typing')
    browser.wait_for('a', 'google images home')


@pytest.fixture(autouse=True)
def report_test(report_test):
    """Turn on autouse for this module."""
    return report_test
