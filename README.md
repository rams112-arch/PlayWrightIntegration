# Playwright Integration Tests

This repository contains integration tests for the Playwright framework, designed to test a app with multiple browsers (Chromium, Firefox, and WebKit)

## Table of Contents

1. [Setup Instructions](@playwright.yml)
2. [Running the Tests](#running-the-tests)
3. [Test Details](#test-design-and-patterns)
4. 
# Code Details: 
Git HUB Respository Link: 
Setup Instruction, Dependencies, browsers details are listed in the @{playwright.yml}

# Task 1 Automated Tests Details: 

Tests are prepared for the mentioned requirements using playwright with python. POM model is used to organize the tests. 

## Locators are defned for each page, files are placed in store/models for the folloiwing pages: 
* Login @{LoginPage.py}
* Product Listing @{ProductListingPage.py}
* Product Details @{ProductDetailPage.py}
* Cart @{CartPage.py}

## Automated tests are prepared for the following scenarios and are placed in tests folder: 
1 - Verify Login functionality with valid credentials Test_LoginPage @{tests/test_login.py} 
2 - Verify Login with invalid creedentials, message should appear  @{tests/test_login.py} 
3 - Verify Product Listing page navigated after successful login @{tests/test_productlisting.py} 
4 - Verify products details page appear successfuly for the selected product @{tests/test_productdetail.py} 
5 - Verify cart functionality on product details page @{tests/test_cart.py} 
    Check product added
    Check if product added two times then quantity is increased 

# Task 2 Details Reporting 
Reports are generated using html report after the successful execution of tests, html report will be generated. Download the report and view the results. In case of any failure screenshot will be generated in the screenshot folder. Screenshot code details are mentioned in the conftest.py 

# Task 3 CI/CD 
Code is pushed to GITHUB 
On every push, jobs will be executed successfully for the the following broswers and report will be generated: 
* Chromium
* Firefox
* WebKit

Details can be found in (@playwright.yml) 
All the dependencies details are mentioned in the requirements.txt
