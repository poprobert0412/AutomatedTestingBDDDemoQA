from pages.demoqa_pages import DemoQa
from pages.base_pages import BasePage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.base_pages = BasePage()
    context.demoqa_pages = DemoQa()

def after_all(context):
    context.browser.close()




