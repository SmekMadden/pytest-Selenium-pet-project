import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def driver():
    chrome_options = ChromeOptions()
    chrome_options.page_load_strategy = "eager"
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options,
    )
    yield driver
    driver.quit()
