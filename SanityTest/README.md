# CommBox Automation Test Suite

## Prerequisite
Install Python 3.7 or above - [Link to downlaod python3.7](https://www.python.org/downloads/release/python-360/)


## Regression Testing
By Ran Yacobov, Head of QA Automation.
In this guide, I will describe how to run the tests from a remote computer.


## CommBox-automation-tests
This project is basicaly consists of a number of function that cover most of the featurs inside the CommBox site.

Its include also the regresion test and during the time more tests will be added.

In order to run the tests do the next steps:

## Installation

*To run the test must be python 3.6 version(link to download python under Prerequisite)

download python 3.6
step 1 :
sudo apt update
sudo apt install software-properties-common

step 2:
sudo add-apt-repository ppa:deadsnakes/ppa
*Press [ENTER] to continue or Ctrl-c to cancel adding it.

step 3:
sudo apt install python3.6

step 4 check your version:
python3 -V


Download pip3:
sudo apt install python3-pip

Update modules that related to automation project:
*run the command from project directory: pip3 install -r requirements

Download pytest:
*sudo pip3 install pytest


*Chrome driver is already in the project.
 If you are getting an exception while running the tests, please update the chrome driver to same version as your chrome browser.
 Url with drivers: https://chromedriver.storage.googleapis.com/index.html
 For example: if you have cjrome browser version 75.0.3770.90 download driver with the same version.


##Run the tests:

1.open the terminal and navigate to project's directory.

2.To run the tests please type:

Run with browser:
pytest  -s -v regression_test_suite_basic_fabric.py --html=report_summary.html

Run without browser(adding --is_headless argument):
pytest  -s -v regression_test_suite_basic_fabric.py --html=report_summary.html --is_headless

*If you are getting py.test: command not found, please run the tests in the following way:
python3 -m pytest  -s -v regression_test_suite_basic_fabric.py --html=report_summary.html 


*note that in --html argument can be any name, it is the name of the html report


## License
The test run on - 8 version - 
[Link to CommboxTest](https://bumpyard.commboxtest.com/)