# Playwright Integration Tests

This repository contains integration tests for the Playwright framework, designed to test a app with multiple browsers (Chromium, Firefox, and WebKit)

## Table of Contents
1. [Code Details]
2. [Task 1 Automated Tests]
3. [Task 2 Reporting]
5. [Task 3 CI/CD]
5. [Task 4 Test Execution]

# Code Details: 
* Git HUB Respository Link: [https://github.com/rams112-arch/PlayWrightIntegration]
* Project Setup, Dependencies, Reporting CI/CD Details are listed in [playwright.yml] file 
* All the versions details can be found in the [requirements.txt] file
* Playwright browser and tests execution details are mentioned in the [conftest.py] file 

# Task 1 Automated Tests Details: 
Tests are prepared for the mentioned requirements using playwright and pytest. POM model is used to organize the tests. 

## Locators are defned for each page, files are placed in store/models for the following pages: 
* Login [LoginPage.py]
* Product Listing [ProductListingPage.py]
* Product Details [ProductDetailPage.py]
* Cart [CartPage.py]

## Automated tests are prepared for the following scenarios and are placed in tests folder: 
1 - Verify Login functionality with valid credentials Test_LoginPage [tests/test_login.py] 
2 - Verify Login with invalid creedentials, message should appear  [tests/test_login.py] 
3 - Verify Product Listing page navigated after successful login [tests/test_productlisting.py] 
4 - Verify products details page appear successfuly for the selected product [tests/test_productdetail.py] 
5 - Verify cart functionality on product details page [tests/test_cart.py] 

# Task 2 Details Reporting 
After the execution of tests, html report will be generated. Download the report and view the results. In case of any failure screenshot will be generated in the screenshot folder. Reporting and screenshot configurations are mentioned in the [conftest.py] 

# Task 3 CI/CD 
Github Actions is used for it.
1. Open the repository [https://github.com/rams112-arch/PlayWrightIntegration]
2. Clone the repository using command git clone https://Github.com/rams112-arch/PlayWrightIntegration
3. Push code to Github after setting up the repository 
4. Open Github, click Actions 
5. Check Job workflow summary
6. HTML Report will be generated after successful execution. 
7. Download tests summary report. In case of any tests failure screenshot will be generated. 
Jobs will be executed parallel for the the following broswers: 
* Chromium
* Firefox
* WebKit 

# Tests Execution Local:
1. Open the repository [https://github.com/rams112-arch/PlayWrightIntegration]
2. Clone the repository using command git clone https://github.com/rams112-arch/PlayWrightIntegration
3. Go to the directory execute code using command on terminal "python3 -m pytest" 
Note: In Conftest.py file, currently headless is marked as True, to execute the tests in browser mark this command False 