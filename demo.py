import pytest
import time

def test_google_cats(browser):
    """Check out the latest typing cat images."""
    browser.get('https://google.com')
    time.sleep(1)
    browser.snap()
    browser.send('cats typing\n')
    browser.click('a', 'images for cats typing')
    browser.wait_for('a', 'google images home')


@pytest.fixture(autouse=True)
def report_test(report_test):
    """Turn on autouse for this module."""
    return report_test
