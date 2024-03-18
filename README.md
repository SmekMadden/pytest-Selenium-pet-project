# Automation Testing Project

This project is a pet project focused on automating tests for the DemoQA website. DemoQA offers a playground for practicing various web automation techniques, making it an ideal candidate for automation projects.

## Overview

The DemoQA website encompasses a wide range of elements and interactions that can be automated for testing purposes. This project aims to cover various aspects of the site, including form submissions, checkbox interactions, button clicks, and more, using Python, Pytest, and Selenium.

## Technologies Used

- **Python**: The core programming language used for writing the test scripts.
- **Pytest**: A powerful testing framework that simplifies the creation and execution of test cases.
- **Selenium**: A suite of tools for automating web browsers, allowing for interaction with web elements.
- **Poetry**: A dependency management and packaging tool in Python, used for managing project dependencies.
- **Allure**: An open-source framework designed for test reporting, making it easier to understand test execution results.

## Project Structure

The project is structured as follows:

- `tests/`: Contains all the test scripts organized by the page module. For example, `elements_page_test.py` includes tests for various elements like text boxes, checkboxes, etc.
- `data/`: Includes data generators and any other data-related utilities for tests.
- `pages/`: Contains page object models for each page of the DemoQA site being tested. This includes classes that encapsulate the functionality of the pages.
- `baseclasses/`: Contains base classes that other classes can inherit from. For example, it includes base_page. py which may serve as a foundation for page object models.
- `locators/`: Contains locator classes or modules, which hold the locators for different web elements in a centralized location, making them easier to manage.
- `allure-results/`: Directory for storing the results of the tests in Allure report format. 

## Setup

To set up this project on your local machine, follow these steps:

1. Ensure you have Python installed on your system.
2. Install Poetry if you haven't already. You can install it by following the instructions on the [official Poetry website](https://python-poetry.org/docs/).
3. Clone the project repository to your local machine.
4. Navigate to the project directory and run `poetry install` to install all the required dependencies.

## Running Tests

To run the tests, use the following command:
```bash
pytest
```
Additionally, to generate an Allure report of the test results, you can use:
```bash
pytest --alluredir=allure-results
```
After running the tests, you can generate and view the report with:
```bash
allure serve allure-results
```


## Pre-commit Hooks

This project utilizes pre-commit hooks to ensure code quality and consistency. These hooks include formatters and linters that automatically check and fix issues before each commit.

To run the pre-commit hooks manually, execute the following command in your terminal:
```bash
pre-commit run --all-files
```