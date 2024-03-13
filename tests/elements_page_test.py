import pytest

from data.data_generator_factories import (
    DataGeneratorFactory,
    FakerGeneratorFactory,
)
from data.object_generators import generate_person
from pages.elements_page import TextBoxPage
from urls import ElementsPageUrls


class TestElementsPage:
    class TestTextBox:
        url = ElementsPageUrls.TEXT_BOX

        @pytest.mark.parametrize("factory", [FakerGeneratorFactory()])
        def test_text_box_page(self, driver, factory: DataGeneratorFactory):
            page = TextBoxPage(driver, url=self.url)
            page.open()
            person = generate_person(data_generator=factory.create_generator())

            page.fill_out_form_and_send(
                full_name=person.fullname,
                email=person.email,
                current_address=person.current_address,
                permanent_address=person.permanent_address,
            )

            output_data: dict = page.get_output_data()

            # TODO Singleton для ошибок, добавить пояснения ошибок в assertы
            assert person.fullname == output_data["name"]
            assert person.email == output_data["email"]
            assert person.current_address == output_data["current_address"]
            assert person.permanent_address == output_data["permanent_address"]
