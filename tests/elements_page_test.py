from typing import Tuple

import pytest

from data.data_generator_factories import (
    DataGeneratorFactory,
    FakerGeneratorFactory,
)
from data.object_generators import generate_person
from pages.elements_page import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonsPage,
    WebTablesPage,
)
from urls import ElementsPageUrls


class TestElementsPage:
    class TestTextBoxPage:
        page_url = ElementsPageUrls.TEXT_BOX

        @pytest.mark.parametrize("factory", [FakerGeneratorFactory()])
        def test_text_box(self, driver, factory: DataGeneratorFactory):
            """Test filling out the text box form with valid data and verifying
            the output matches the input."""

            person = generate_person(data_generator=factory.create_generator())

            page = TextBoxPage(driver, url=self.page_url).open()
            page.fill_out_form_and_send(
                full_name=f"{person.first_name} {person.last_name}",
                email=person.email,
                current_address=person.current_address,
                permanent_address=person.permanent_address,
            )

            output_data: dict = page.get_output_user_data()

            assert output_data["name"] == person.fullname
            assert output_data["email"] == person.email
            assert output_data["current_address"] == person.current_address
            assert output_data["permanent_address"] == person.permanent_address

    class TestCheckBoxPage:
        page_url = ElementsPageUrls.CHECKBOX

        def test_checkbox(self, driver):
            """Test ensures that the checkboxes can be clicked and that the
            names of the clicked checkboxes are correctly displayed in the
            success list."""
            page = CheckBoxPage(driver, url=self.page_url).open()
            page.expand_all_list()

            clicked_names = page.click_random_leafs_of_checkbox_tree()
            result_names = page.get_checkbox_name_from_success_list()

            for name in clicked_names:
                assert name in result_names

    class TestRadoButtonPage:
        page_url = ElementsPageUrls.RADIO_BUTTON

        def test_radio_buttons(self, driver):
            """Test ensures that radio buttons can be clicked and that the
            success message correctly reflects the clicked radio button
            option."""

            page = RadioButtonsPage(driver, url=self.page_url).open()

            page.click_yes()
            assert page.get_success_text() == "Yes"

            page.click_impressive()
            assert page.get_success_text() == "Impressive"

            # Deliberately made page bug on website!
            page.click_no()
            assert page.get_success_text() == "No"

    class TestWebTablesPage:
        page_url = ElementsPageUrls.WEB_TABLES

        @pytest.mark.parametrize("factory", [FakerGeneratorFactory()])
        def test_add_person_to_table(self, driver, factory: DataGeneratorFactory):
            """Test the functionality of the web tables page by registering a
            person and verifying their data in the table."""

            page = WebTablesPage(driver, url=self.page_url).open()
            page.open_registration_form()

            p = generate_person(data_generator=factory.create_generator())

            person_data_for_assert = page.fill_registration_form(
                first_name=p.first_name,
                last_name=p.last_name,
                email=p.email,
                age=p.age,
                salary=p.salary,
                department=p.department,
            )

            people: Tuple = page.get_all_people_from_table()

            assert (
                person_data_for_assert in people
            ), f"Person {person_data_for_assert} not found in {people}"
