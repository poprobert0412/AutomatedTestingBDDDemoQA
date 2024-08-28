from browser import Browser

class BasePage(Browser):
    def navigate_to_main_page(self):
        self.chrome.get("https://demoqa.com/elements")

