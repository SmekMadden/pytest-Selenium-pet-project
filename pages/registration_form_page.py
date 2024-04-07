import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from baseclasses.base_page import BasePage
from data.dataclasses.global_dc import Person
from locators import registration_form_page as locators


class RegistrationFormPage(BasePage):
    L = locators.FormLocators

    def click_random_element(self, elements_locators):
        self.element_is_visible(random.choice(elements_locators)).click()

    def click_random_gender_radio(self):
        self.click_random_element((self.L.MALE, self.L.FEMAIL, self.L.OTHER))

    def click_random_hobby_radio(self):
        self.click_random_element((self.L.SPORTS, self.L.READING, self.L.MUSIC))

    def enter_random_subject(self):
        subjects = [
            "English",
            "Maths",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "History",
        ]
        subjects_field: WebElement = self.element_is_visible(self.L.SUBJECT)

        random_count = random.randint(1, len(subjects))
        random_elements = random.sample(subjects, random_count)

        for i in range(random_count):
            subjects_field.send_keys(random_elements[i])
            subjects_field.send_keys(Keys.ENTER)

    def select_random_state(self):
        self.element_is_visible(self.L.STATE).click()
        states_given = self.elements_are_visible(self.L.STATE_MENU_ELEMENTS)
        random.choice(states_given).click()

    def fill_registration_form(self, person: Person):
        field_values = {
            self.L.FIRST_NAME: person.first_name,
            self.L.LAST_NAME: person.last_name,
            self.L.EMAIL: person.email,
            self.L.MOBILE: person.phone_number,
            self.L.CURRENT_ADDRESS: person.current_address,
        }

        for locator, value in field_values.items():
            self.element_is_visible(locator).send_keys(value)

        self.click_random_gender_radio()
        self.click_random_hobby_radio()
        self.enter_random_subject()
        self.select_random_state()

        self.element_is_visible(self.L.SUBMIT_BUTTON).click()

    def modal_window_presented(self) -> bool:
        try:
            self.element_is_visible(self.L.MODAL)
        except TimeoutException:
            return False
        return True

    def get_modal_title(self) -> str:
        return self.element_is_presented(self.L.MODAL_TITLE).text

    def close_modal_window(self):
        self.element_is_visible(self.L.MODAL_CLOSE_BTN).click()
