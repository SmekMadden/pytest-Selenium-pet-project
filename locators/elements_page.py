class TextBoxPageLocators:
    # Input
    FULL_NAME = ("xpath", '//input[@id="userName"]')
    EMAIL = ("xpath", '//input[@id="userEmail"]')
    CURRENT_ADDRESS = ("xpath", '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = ("xpath", '//textarea[@id="permanentAddress"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')

    # Output
    CREATED_NAME = ("xpath", '//p[@id="name"]')
    CREATED_EMAIL = ("xpath", '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = ("xpath", '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = ("xpath", '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:
    CHECKBOX_LEAFS_LIST = ("xpath", '//li[@class="rct-node rct-node-leaf"]//label')
    RESULT_CHECKBOX_NAMES = ("xpath", '//span[@class="text-success"]')
    EXPAND_BUTTON = ("xpath", '//button[@title="Expand all"]')


class RadioButtonPageLocators:
    YES_LABEL = ("xpath", '//input[@id="yesRadio"]/../label')
    IMPRESSIVE_BUTTON_W_LABEL = ("xpath", '//input[@id="impressiveRadio"]/..')
    NO_BUTTON_W_LABEL = ("xpath", '//input[@id="noRadio"]/..')

    SUCCESS_TEXT = ("xpath", '//span[@class="text-success"]')


class WebTablesPageLocators:
    ADD_BUTTON = ("xpath", '//button[@id="addNewRecordButton"]')
    PEOPLE_LIST = ("xpath", '//div[@class="rt-tr-group"]')

    # registration form popup
    FIRST_NAME_INPUT = ("xpath", '//input[@id="firstName"]')
    LAST_NAME_INPUT = ("xpath", '//input[@id="lastName"]')
    EMAIL_INPUT = ("xpath", '//input[@id="userEmail"]')
    AGE_INPUT = ("xpath", '//input[@id="age"]')
    SALARY_INPUT = ("xpath", '//input[@id="salary"]')
    DEPARTMENT_INPUT = ("xpath", '//input[@id="department"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')
