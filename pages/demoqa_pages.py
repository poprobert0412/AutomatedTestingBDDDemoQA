from selenium.webdriver.common.by import By
from pages.base_pages import BasePage

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


