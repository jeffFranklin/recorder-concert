import pytest
import time

def test_google_cats(browser):
    """Check out the latest typing cat images."""
    browser.get('https://google.com')
    time.sleep(1)
    browser.snap()
    browser.send('keyboard cat\n')
    browser.click('a', 'images for keyboard cat')
    browser.wait_for('a', 'google images home')


def test_dubs(browser):
    """
    This test intentionally fails. There really is a link with text
    'Read more' but for some reason we can't pull it out.
    """
    browser.get('https://uw.edu')
    browser.click('a', 'read more')


@pytest.fixture(autouse=True)
def report_test(report_test):
    """Turn on autouse for this module."""
    return report_test
