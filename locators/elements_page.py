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
    SEARCH_INPUT = ("xpath", '//input[@id="searchBox"]')
    EDIT_BUTTONS = ("xpath", './/span[@title="Edit"]')
    DELETE_BUTTONS = ("xpath", './/span[@title="Delete"]')

    # registration form popup
    FIRST_NAME_INPUT = ("xpath", '//input[@id="firstName"]')
    LAST_NAME_INPUT = ("xpath", '//input[@id="lastName"]')
    EMAIL_INPUT = ("xpath", '//input[@id="userEmail"]')
    AGE_INPUT = ("xpath", '//input[@id="age"]')
    SALARY_INPUT = ("xpath", '//input[@id="salary"]')
    DEPARTMENT_INPUT = ("xpath", '//input[@id="department"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BTN = ("xpath", '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BTN = ("xpath", '//button[@id="rightClickBtn"]')
    CLICK_ME_BTN = ("xpath", '//button[text()="Click Me"]')

    # Messages
    DOUBLE_CLICK_MSG = ("xpath", '//p[@id="doubleClickMessage"]')
    RIGHT_CLICK_MSG = ("xpath", '//p[@id="rightClickMessage"]')
    CLICK_ME_MSG = ("xpath", '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:
    HOME_LINK = ("xpath", '//a[@id="simpleLink"]')
    DYNAMIC_LINK = ("xpath", '//a[@id="dynamicLink"]')
    CREATED_LINK = ("xpath", '//a[@id="created"]')
    NO_CONTENT_LINK = ("xpath", '//a[@id="no-content"]')
    MOVED_LINK = ("xpath", '//a[@id="moved"]')
    BAD_REQUEST_LINK = ("xpath", '//a[@id="bad-request"]')
    UNAUTHORIZED_LINK = ("xpath", '//a[@id="unauthorized"]')
    FORBIDDEN_LINK = ("xpath", '//a[@id="forbidden"]')
    NOT_FOUND_LINK = ("xpath", '//a[@id="invalid-url"]')

    RESPONSE_MSG = ("xpath", '//p[@id="linkResponse"]')


class UploadDownloadPageLocators:
    DOWNLOAD_BTN = ("xpath", '//a[@id="downloadButton"]')
    CHOOSE_FILE_BTN = ("xpath", '//input[@id="uploadFile"]')
    MESSAGE = ("xpath", '//p[@id="uploadedFilePath"]')


class DynamicPropertiesPageLocators:
    ENABLE_BTN = ("xpath", '//button[@id="enableAfter"]')
    COLOR_CHANGE_BTN = ("xpath", '//button[@id="colorChange"]')
    VISIBLE_BTN = ("xpath", '//button[@id="visibleAfter"]')
