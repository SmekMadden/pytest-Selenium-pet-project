import pytest

from pages.registration_form_page import RegistrationFormPage
from urls import RegistrationFormPageUrls


class TestRegistrationForm:
    url = RegistrationFormPageUrls.REGISTRATION_FORM

    @pytest.fixture(scope="function")
    def page(self, driver):
        return RegistrationFormPage(driver, url=TestRegistrationForm.url).open()

    def test_registration_form(self, page, generated_person):
        """Tests the registration form by filling it with a generated person's
        data, verifying the presence of a success modal window, and checking
        the modal title."""
        page.fill_registration_form(person=generated_person)
        assert page.modal_window_presented(), "Modal window does not found"

        modal_title = page.get_modal_title()
        assert modal_title == "Thanks for submitting the form"

        page.close_modal_window()
