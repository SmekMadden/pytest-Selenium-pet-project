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
