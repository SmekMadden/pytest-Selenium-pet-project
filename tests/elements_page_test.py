import random
from typing import Tuple

import pytest
from selenium.webdriver.remote.webelement import WebElement

from data.data_generator_factories import (
    DataGeneratorFactory,
    FakerGeneratorFactory,
)
from data.dataclasses.global_dc import Person
from data.object_generators import generate_person
from pages.elements_page import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonsPage,
    WebTablesPage,
)
from urls import ElementsPageUrls


@pytest.fixture(scope="function")
def generated_person():
    factory: DataGeneratorFactory = FakerGeneratorFactory()
    return generate_person(data_generator=factory.create_generator())


class TestTextBoxPage:
    page_url = ElementsPageUrls.TEXT_BOX

    def test_text_box(self, driver, generated_person: Person):
        """Test filling out the text box form with valid data and verifying the
        output matches the input."""

        p: Person = generated_person

        page = TextBoxPage(driver, url=self.page_url).open()
        page.fill_out_form_and_send(
            full_name=p.full_name,
            email=p.email,
            current_address=p.current_address,
            permanent_address=p.permanent_address,
        )

        output_data: dict = page.get_output_user_data()

        assert output_data["name"] == p.full_name
        assert output_data["email"] == p.email
        assert output_data["current_address"] == p.current_address
        assert output_data["permanent_address"] == p.permanent_address


class TestCheckBoxPage:
    page_url = ElementsPageUrls.CHECKBOX

    def test_checkbox(self, driver):
        """Test ensures that the checkboxes can be clicked and that the names
        of the clicked checkboxes are correctly displayed in the success
        list."""
        page = CheckBoxPage(driver, url=self.page_url).open()
        page.expand_all_list()

        clicked_names = page.click_random_leafs_of_checkbox_tree()
        result_names = page.get_checkbox_name_from_success_list()

        for name in clicked_names:
            assert name in result_names


class TestRadoButtonPage:
    page_url = ElementsPageUrls.RADIO_BUTTON

    def test_radio_buttons(self, driver):
        """Test ensures that radio buttons can be clicked and that the success
        message correctly reflects the clicked radio button option."""

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

    def test_add_person_to_table(self, driver, generated_person: Person):
        """Test the functionality of the web tables page by registering a
        person and verifying their data in the table."""

        page = WebTablesPage(driver, url=self.page_url).open()
        page.open_registration_form()

        p: Person = generated_person

        person_data_for_assert = page.fill_registration_form(
            first_name=p.first_name,
            last_name=p.last_name,
            email=p.email,
            age=p.age,
            salary=p.salary,
            department=p.department,
        )

        people: Tuple = page.get_people_data()

        assert (
            person_data_for_assert in people
        ), f"Person {person_data_for_assert} not found in {people}"

    def test_person_search(self, driver):
        """Test the search functionality of the web tables page by inputting a
        keyword related to a randomly selected person's information.

        It verifies that the person appears in the search results and
        that the table's content changes accordingly. Additionally, it
        checks that clearing the search input restores the table to its
        original state, displaying all people.

        """
        page = WebTablesPage(driver, url=self.page_url).open()

        all_people: Tuple = page.get_people_data()
        random_person: Tuple = random.choice(all_people)  # noqa

        random_keyword: str = random.choice(random_person)  # noqa
        page.write_keyword_in_search_input_field(random_keyword)

        people_found = page.get_people_data()

        assert (
            random_person in people_found
        ), f"Person {random_person=}, searched by {random_keyword=}, not found in {people_found=}"
        assert (
            all_people != people_found
        ), f"Table have not changed after search by {random_keyword=}"

        page.clear_search_input()
        assert (
            page.get_people_data() == all_people
        ), "After clearing search input, table data is not the same as before"

    def test_update_person(self, driver, generated_person: Person):
        """Test the functionality of updating a person's information in the web
        tables.

        This test selects a random person from the table, opens the edit
        form, updates the person's information with new data generated
        by the specified factory, and verifies that the updated
        information matches the input data in the table.

        """
        page = WebTablesPage(driver, url=self.page_url).open()

        person_to_edit, person_index = page.get_random_person()
        page.open_edit_form(person_to_edit)

        p: Person = generated_person

        page.update_person_by_edit_form(
            **{
                "first_name": p.first_name,
                "last_name": p.last_name,
                "email": p.email,
                "age": p.age,
                "salary": p.salary,
                "department": p.department,
            },
        )

        updated_person: WebElement = page.get_person_by_index(person_index)
        updated_person: Person = page.get_person_data(updated_person)

        assert updated_person.first_name == p.first_name
        assert updated_person.last_name == p.last_name
        assert updated_person.email == p.email
        assert updated_person.age == p.age
        assert updated_person.salary == p.salary
        assert updated_person.department == p.department
