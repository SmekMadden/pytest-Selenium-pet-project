import pytest

from data.data_generator_factories import (
    DataGeneratorFactory,
    FakerGeneratorFactory,
)
from data.object_generators import generate_person
from pages.elements_page import TextBoxPage, CheckBoxPage
from urls import ElementsPageUrls


class TestElementsPage:
    class TestTextBoxPage:
        page_url = ElementsPageUrls.TEXT_BOX

        @pytest.mark.parametrize("factory", [FakerGeneratorFactory()])
        def test_text_box(self, driver, factory: DataGeneratorFactory):
            person = generate_person(data_generator=factory.create_generator())

            page = TextBoxPage(driver, url=self.page_url).open()
            page.fill_out_form_and_send(
                full_name=person.fullname,
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
            page = CheckBoxPage(driver, url=self.page_url).open()
            page.expand_all_list()

            clicked_names = page.click_random_leafs_of_checkbox_tree()
            result_names = page.get_checkbox_name_from_success_list()

            for name in clicked_names:
                assert name in result_names
