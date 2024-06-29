# tablecheck-qa-automation-take-home
Take-home project for the TableCheck QA Automation role.

## Setup Instructions:

1. Clone the provided repository (you'll need to create a dummy repository with a simple web application or use a publicly available web application for testing purposes).
2. Install Playwright and any other necessary dependencies.
3. Write your tests in Python using the Playwright framework.

## Task 1: Write Automated Tests for a Web Application

Application Overview: The application provided in this repository includes several key business features: a login page, a product listing page, a cart, and a product details page.

### Requirements:
Implement automated tests for the following scenarios using Playwright and Python:
* Login Test: Verify that a user can log in with valid credentials.
* Login Negative Test: Ensure the system correctly handles invalid login attempts.
* Product Listing Navigation Test: Verify that after login, the user can navigate to the product listing page.
* Product Details Test: Implement a test to verify that clicking on a product in the listing page navigates to the correct product details page.
* Add to Cart Test: Test adding a product to the shopping cart from the product details page.
* Each test should assert the expected outcome to ensure the feature is working as intended.
* Use Page Object Model (POM) design pattern to structure your tests.

## Task 2: Test Reporting

* Integrate a reporting tool or framework of your choice with your test suite.
* Ensure the report includes the following details for each test: test name, status (passed/failed), and execution time.
* Bonus: Include screenshots of the final state of each test in the report for failed tests.

## Task 3: Continuous Integration (CI)
* Provide instructions or a configuration file (e.g., .yml or .json) for integrating your test suite with a CI/CD tool (e.g., GitHub Actions, Jenkins).
* The CI pipeline should install dependencies, run the tests, and generate a report on every push to the repository.


## Submission Guidelines:
Push your code to a public Git repository. GitHub is preferred.

Make sure to include a README file with:
* Instructions on how to set up and run your tests.
* A brief explanation of your test design and any design patterns used.
* Share the repository link by replying to the test invitation email.


### Evaluation Criteria:
* Code Quality: Readability, use of proper naming conventions, and adherence to Playwright best practices.
* Test Coverage: Completeness of testing scenarios covered for the given application features.
* Design Patterns: Effective use of design patterns like POM to enhance test maintainability.
* Problem Solving: Ability to handle edge cases and unexpected application behavior.
* Documentation: Clarity and completeness of the documentation provided.
