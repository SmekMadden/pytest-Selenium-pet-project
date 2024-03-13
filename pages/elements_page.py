from typing import Dict

from baseclasses.base_page import BasePage
from locators.elements_page import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_out_form_and_send(
        self,
        full_name,
        email,
        current_address,
        permanent_address,
    ):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(
            current_address,
        )
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(
            permanent_address,
        )
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def get_output_data(self) -> Dict:
        return {
            "name": self.element_is_visible(self.locators.CREATED_NAME).text.split(":")[
                1
            ],
            "email": self.element_is_visible(self.locators.CREATED_EMAIL).text.split(
                ":",
            )[1],
            "current_address": self.element_is_visible(
                self.locators.CREATED_CURRENT_ADDRESS,
            ).text.split(":")[1],
            "permanent_address": self.element_is_visible(
                self.locators.CREATED_PERMANENT_ADDRESS,
            ).text.split(":")[1],
        }
