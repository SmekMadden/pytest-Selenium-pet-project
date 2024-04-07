import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from pathlib import Path
from faker import Faker

from config import BASE_DIR
from data.data_generator_factories import DataGeneratorFactory, FakerGeneratorFactory
from data.object_generators import generate_person


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


@pytest.fixture(scope="function")
def txt_file():
    fake = Faker()
    filename = f"{fake.word()}.txt"
    content = fake.text()
    path: Path = BASE_DIR / filename

    with open(path, "w") as f:
        f.write(content)

    yield path
    os.remove(path)


@pytest.fixture(scope="function")
def generated_person():
    factory: DataGeneratorFactory = FakerGeneratorFactory()
    return generate_person(data_generator=factory.create_generator())
