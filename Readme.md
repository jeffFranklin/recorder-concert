# Using storyboarding to accurately capture your web application's health and to drive its design

## Quickstart for this repository

Assuming python3 and npm installed on the system...
```
# Create and activated the virtualenv
python3 -m venv venv
source venv/bin/activate

# install the dependendencies and phantomjs
pip install -U -r requirements.txt
npm install phantomjs-prebuilt

# run the tests, result file is webdriver-report.html
pytest demo.py
```

## The problem

* People designing the user experience had a hard time accessing all the various facets of our UI
* Service owners/managers didn't have a view into the progress of the project and the work remaining to be done
* A fair amount of our code was javascript and html, for which we had zero test coverage.

## Enter the web-recorder

* Write some tests for your core functionality, taking screenshots along the way
* Report the results in a place that can be shared easily with others
* Announce the results in a place where people are watching, especially on failure

## How we got there

* New repository https://github.com/UWIT-IAM/webdriver-recorder that is a convenience wrapper around the python `selenium` package, with screenshot capturing and reporting baked in.
* Automatically run by bamboo (build.s.uw.edu) on updates to git repository, along with once-a-day reports
* Results stored on bamboo and reported out to slack.

## Our strategy

* The less we know about our html structure, the better. Aim to key off the visibility of critical text on the page.
* Dynamic pages can change asynchronously, especially with AJAX requests. For our browser we `wait_for` text to appear, which we default to 5 seconds. The end of a wait is commonly a good time to grab a screenshot. 
* **Keep an eye towards automation and reporting** - you've got your tests working, now automate them. Run them every time the server changes, and/or on a regular schedule.

## Issues

* PhantomJS deprecation in favor of headless chrome
* webdriver-recorder still slightly tailored to Identity.UW styles.