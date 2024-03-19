import re
from typing import Dict, List, Tuple

from baseclasses.base_page import BasePage

from locators import elements_page as locators
import random


class TextBoxPage(BasePage):
    L = locators.TextBoxPageLocators()

    def fill_out_form_and_send(
        self,
        full_name,
        email,
        current_address,
        permanent_address,
    ):
        self.element_is_visible(self.L.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.L.EMAIL).send_keys(email)
        self.element_is_visible(self.L.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.L.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.L.SUBMIT_BUTTON).click()

    def get_output_user_data(self) -> Dict:
        output = {
            "name": self.element_is_visible(self.L.CREATED_NAME),
            "email": self.element_is_visible(self.L.CREATED_EMAIL),
            "current_address": self.element_is_visible(self.L.CREATED_CURRENT_ADDRESS),
            "permanent_address": self.element_is_visible(
                self.L.CREATED_PERMANENT_ADDRESS,
            ),
        }
        user_data = {key: value.text.split(":")[1] for key, value in output.items()}

        return user_data


class CheckBoxPage(BasePage):
    L = locators.CheckBoxPageLocators()

    def expand_all_list(self):
        expand_button = self.element_is_clickable(self.L.EXPAND_BUTTON)
        expand_button.click()

    def click_random_leafs_of_checkbox_tree(self) -> List:
        checkbox_list = self.elements_are_visible(self.L.CHECKBOX_LEAFS_LIST)

        chosen_checkboxes = []
        for item in checkbox_list:
            if random.choice((True, False)):  # noqa
                item_text = item.text.lower().replace(" ", "")
                item_text_cleaned = re.sub(pattern=r".doc", repl="", string=item_text)
                chosen_checkboxes.append(item_text_cleaned)
                item.click()

        return chosen_checkboxes

    def get_checkbox_name_from_success_list(self) -> List:
        return [
            element.text.lower()
            for element in self.elements_are_visible(self.L.RESULT_CHECKBOX_NAMES)
        ]


class RadioButtonsPage(BasePage):
    L = locators.RadioButtonPageLocators()

    def get_success_text(self):
        return self.element_is_visible(self.L.SUCCESS_TEXT).text

    def click_yes(self):
        self.element_is_visible(self.L.YES_LABEL).click()

    def click_impressive(self):
        self.element_is_visible(self.L.IMPRESSIVE_BUTTON_W_LABEL).click()

    def click_no(self):
        self.element_is_visible(self.L.NO_BUTTON_W_LABEL).click()


class WebTablesPage(BasePage):
    L = locators.WebTablesPageLocators()

    def open_registration_form(self):
        self.element_is_visible(self.L.ADD_BUTTON).click()

    def fill_registration_form(
        self,
        first_name,
        last_name,
        email,
        age,
        salary,
        department,
    ):
        self.element_is_visible(self.L.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.L.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.L.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.L.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.L.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.L.DEPARTMENT_INPUT).send_keys(department)

        self.element_is_visible(self.L.SUBMIT_BUTTON).click()

        return first_name, last_name, str(age), email, str(salary), str(department)

    def get_all_people_from_table(self) -> Tuple:
        people_objects = self.elements_are_presented(self.L.PEOPLE_LIST)
        people = []

        for person_object in people_objects:
            if person_object.text.strip():
                person: list = person_object.text.split("\n")
                people.append(tuple(person))

        return tuple(people)
