from selenium.webdriver.common.by import By
from pages.base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class DemoQa(BasePage):
    text_box = (By.ID, "item-0")
    check_box = (By.ID, "item-1")
    radio_button = (By.ID, "item-2")
    buttons_button = (By.ID, "item-4")
    user_name = (By.ID, "userName")
    user_email = (By.ID, "userEmail")
    user_currentaddress = (By.ID, "currentAddress")
    user_permanentaddress = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    expand_checkbox_home = (By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
    desktop_checkbox = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[1]')
    checkbox_result = (By.ID, 'result')
    radio_yes_button = (By.CLASS_NAME, 'custom-control-label')
    radio_result = (By.CLASS_NAME, 'mt-3')
    radio_impressive_button = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label')
    radio_no_button = (By.XPATH, '//input[@id="noRadio"]')
    double_click_button = (By.ID, 'doubleClickBtn')
    double_click_message = (By.ID, 'doubleClickMessage')
    right_click_button = (By.ID, 'rightClickBtn')
    right_click_message = (By.ID, 'rightClickMessage')
    click_me_button = (By.XPATH, '//button[text()="Click Me"]')
    click_me_button_message = (By.ID, 'dynamicClickMessage')

    def press_text_box(self):
        self.chrome.find_element(*self.text_box).click()

    def press_check_box(self):
        self.chrome.find_element(*self.check_box).click()

    def press_radio_button(self):
        self.chrome.find_element(*self.radio_button).click()

    def press_buttons_button(self):
        self.chrome.find_element(*self.buttons_button).click()

    def enter_fullname(self, fullname):
        self.chrome.find_element(*self.user_name).send_keys(fullname)

    def enter_email(self, email):
        self.chrome.find_element(*self.user_email).send_keys(email)

    def enter_currentaddress(self, currentaddress):
        self.chrome.find_element(*self.user_currentaddress).send_keys(currentaddress)

    def enter_permanentaddress(self, permanentaddress):
        self.chrome.find_element(*self.user_permanentaddress).send_keys(permanentaddress)

    def press_submit_button(self):
        self.chrome.find_element(*self.submit_button).click()

    def entered_information(self, fullname, email, currentaddress, permanentaddress):
        current_name = self.chrome.find_element(By.ID, "name").text
        assert current_name == f"Name:{fullname}"

        current_email = self.chrome.find_element(By.ID, "email").text
        assert current_email == f"Email:{email}"

        current_address = self.chrome.find_element(By.XPATH, '//*[@id="currentAddress"] [@class="mb-1"]').text
        assert current_address == f"Current Address :{currentaddress}"

        permanent_address = self.chrome.find_element(By.XPATH, '//*[@id="permanentAddress"] [@class="mb-1"]').text

        assert permanent_address == f"Permananet Address :{permanentaddress}"

    def press_expand_checkbox_home(self):
        self.chrome.find_element(*self.expand_checkbox_home).click()

    def press_desktop_checkbox(self):
        self.chrome.find_element(*self.desktop_checkbox).click()

    def checkbox_assert(self):
        desktop = self.chrome.find_element(*self.checkbox_result)
        assert desktop.text == "You have selected :\ndesktop\nnotes\ncommands"

    def selecting_yes(self):
        self.chrome.find_element(*self.radio_yes_button).click()

    def assert_yes_radio_button(self):
        text_yes = self.chrome.find_element(*self.radio_result)
        assert text_yes.text == "You have selected Yes"

    def selecting_impressive(self):
        self.chrome.find_element(*self.radio_impressive_button).click()

    def assert_impressive_radio_button(self):
        text_impressive = self.chrome.find_element(*self.radio_result)
        assert text_impressive.text == "You have selected Impressive"

    def click_no_button(self):
        WebDriverWait(self.chrome, 10).until(
            EC.presence_of_element_located(self.radio_no_button)
        )
        disabled_button = self.chrome.find_element(*self.radio_no_button)
        if disabled_button.is_enabled():
            raise Exception("I can click the 'NO' button! Test Failed")
        else:
            print("The 'NO' button is disabled as expected.")
    def no_radio_button_disabled(self):
        WebDriverWait(self.chrome, 10).until(
            EC.presence_of_element_located(self.radio_no_button)
        )
        disabled_button = self.chrome.find_element(*self.radio_no_button).is_enabled()
        if disabled_button:
            raise Exception("No button is enabled! The test failed")
        else:
            print("The 'NO' button is correctly disabled.")

    def press_double_click(self):
        actions = ActionChains(self.chrome)
        element = self.chrome.find_element(*self.double_click_button)
        actions.double_click(element).perform()

    def assert_double_click(self):
        message = self.chrome.find_element(*self.double_click_message)
        assert message.text == "You have done a double click"

    def press_right_click(self):
        actions = ActionChains(self.chrome)
        element = self.chrome.find_element(*self.right_click_button)
        #Cu ajutorul actionchain ului si elementului context click putem sa dam click dreapta
        actions.context_click(element).perform()

    def assert_right_click(self):
        message = self.chrome.find_element(*self.right_click_message)
        assert message.text == "You have done a right click"

    def press_click_me(self):
        element = self.chrome.find_element(*self.click_me_button)
        element.click()

    def assert_click_me(self):
        message = self.chrome.find_element(*self.click_me_button_message)
        assert message.text == "You have done a dynamic click"

