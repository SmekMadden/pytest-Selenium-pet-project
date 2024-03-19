import re
from typing import Dict, List

from baseclasses.base_page import BasePage
from locators.elements_page import (
    TextBoxPageLocators,
    CheckBoxPageLocators,
    RadioButtonPageLocators,
)
import random


class TextBoxPage(BasePage):
    L = TextBoxPageLocators()

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
    L = CheckBoxPageLocators()

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
    L = RadioButtonPageLocators()

    def get_success_text(self):
        return self.element_is_visible(self.L.SUCCESS_TEXT).text

    def click_yes(self):
        self.element_is_visible(self.L.YES_LABEL).click()

    def click_impressive(self):
        self.element_is_visible(self.L.IMPRESSIVE_BUTTON_W_LABEL).click()

    def click_no(self):
        self.element_is_visible(self.L.NO_BUTTON_W_LABEL).click()
