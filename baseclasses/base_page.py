from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    timeout = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):  # noqa
        self.driver.get(self.url)
        return self

    def element_is_visible(self, locator: Tuple[str, str], timeout=timeout):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.visibility_of_element_located(locator=locator),
        )

    def elements_are_visible(self, locator: Tuple[str, str], timeout=timeout):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.visibility_of_all_elements_located(locator=locator),
        )

    def element_is_presented(self, locator: Tuple[str, str], timeout=timeout):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.presence_of_element_located(locator=locator),
        )

    def elements_are_presented(self, locator: Tuple[str, str], timeout=timeout):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.presence_of_all_elements_located(locator=locator),
        )

    def element_is_invisible(
        self,
        web_element_or_locator: WebElement | Tuple[str, str],
        timeout: int = timeout,
    ):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.invisibility_of_element_located(locator=web_element_or_locator),
        )

    def element_is_clickable(
        self,
        web_element_or_locator: WebElement | Tuple[str, str],
        timeout=timeout,
    ):
        return wait(driver=self.driver, timeout=timeout).until(
            EC.element_to_be_clickable(mark=web_element_or_locator),
        )

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def double_click_element(self, element: WebElement):
        ActionChains(self.driver).move_to_element(element).double_click(
            element,
        ).perform()

    def right_click_element(self, element: WebElement):
        ActionChains(self.driver).move_to_element(element).context_click(
            element,
        ).perform()
