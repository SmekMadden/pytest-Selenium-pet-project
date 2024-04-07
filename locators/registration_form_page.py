class FormLocators:
    FIRST_NAME = ("xpath", '//input[@id="firstName"]')
    LAST_NAME = ("xpath", '//input[@id="lastName"]')
    EMAIL = ("xpath", '//input[@id="userEmail"]')

    # Gender radio buttons divs
    MALE = ("xpath", '//input[@value="Male"]/..')
    FEMAIL = ("xpath", '//input[@value="Female"]/..')
    OTHER = ("xpath", '//input[@value="Other"]/..')

    MOBILE = ("xpath", '//input[@id="userNumber"]')
    DATE_OF_BIRTH = ("xpath", '//input[@id="dateOfBirthInput"]')
    SUBJECT = ("xpath", '//input[@id="subjectsInput"]')

    # Hobbies radio buttons divs
    SPORTS = ("xpath", '//input[@id="hobbies-checkbox-1"]/..')
    READING = ("xpath", '//input[@id="hobbies-checkbox-2"]/..')
    MUSIC = ("xpath", '//input[@id="hobbies-checkbox-3"]/..')

    UPLOAD_PICTURE = ("xpath", '//input[@id="uploadPicture"]')
    CURRENT_ADDRESS = ("xpath", '//textarea[@id="currentAddress"]')
    STATE = ("xpath", '//div[@id="state"]')
    STATE_INPUT = ("xpath", '//div[@id="state"]//input')
    STATE_MENU_ELEMENTS = (
        "xpath",
        '//div[@id="state"]//div[contains(@class, "menu")]/div/div',
    )
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')

    # Modal windows after form submit
    MODAL = ("xpath", '//div[@class="modal-content"]')
    MODAL_TITLE = ("xpath", '//div[contains(@class, "modal-title")]')
    MODAL_BODY = ("xpath", '//div[@class="modal-body"]')
    MODAL_CLOSE_BTN = ("xpath", '//button[@id="closeLargeModal"]')
