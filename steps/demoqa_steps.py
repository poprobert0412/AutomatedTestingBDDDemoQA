from behave import * #De fiecare data importam asta 

@given(u'I am on the main page')
def step_impl(context):
    print(u'STEP: Given I am on the main page')
    context.base_pages.navigate_to_main_page()

@when(u'I press the "Text Box" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Text Box" button under "Elements"')
    context.demoqa_pages.press_text_box()

@when(u'I enter "{fullname}" in the Full Name field')
def step_impl(context, fullname):
    print(u'STEP: When I enter "{fullname}" in the Full Name field')
    context.demoqa_pages.enter_fullname(fullname)

@when(u'I enter "{email}" in the Email field')
def step_impl(context, email):
    print(u'STEP: When I enter "{email}" in the Email field')
    context.demoqa_pages.enter_email(email)

@when(u'I enter "{currentaddress}" in the Current Address field')
def step_impl(context, currentaddress):
    print(u'STEP: When I enter "{currentaddress}" in the Current Address field')
    context.demoqa_pages.enter_currentaddress(currentaddress)

@when(u'I enter "{permanentaddress}" in the Permanent Address field')
def step_impl(context, permanentaddress):
    print(u'STEP: When I enter "{permanentaddress}" in the Permanent Address field')
    context.demoqa_pages.enter_permanentaddress(permanentaddress)

@when(u'I press the Submit button')
def step_impl(context):
    print(u'STEP: When I press the Submit button')
    context.demoqa_pages.press_submit_button()

@then(u'I should see my entered information displayed below "{fullname}" "{email}" "{currentaddress}" "{permanentaddress}"')
def step_impl(context, fullname, email, currentaddress, permanentaddress):
    print(u'STEP: Then I should see my entered information displayed below "{fullname}" "{email}" "{currentaddress}" "{permanentaddress}"')
    context.demoqa_pages.entered_information(fullname, email, currentaddress, permanentaddress)

@when(u'I press the "Check Box" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Check Box" button under "Elements"')
    context.demoqa_pages.press_check_box()

@when(u'I press the Expand Button near the "Home" section')
def step_impl(context):
    print(u'STEP: When I press the Expand Button near the "Home" section')
    context.demoqa_pages.press_expand_checkbox_home()

@when(u'I press the checkbox labeled "Desktop"')
def step_impl(context):
    print(u'STEP: When I press the checkbox labeled "Desktop"')
    context.demoqa_pages.press_desktop_checkbox()

@then(u'I should see the message: "You have selected : desktop notes commands"')
def step_impl(context):
    print(u'STEP: Then I should see the message: "You have selected : desktop notes  commands"')
    context.demoqa_pages.checkbox_assert()

@when(u'I press the "Radio Button" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Radio Button" button under "Elements"')
    context.demoqa_pages.press_radio_button()

@when(u'I select the "Yes" radio button')
def step_impl(context):
    print(u'STEP: When I select the "Yes" radio button')
    context.demoqa_pages.selecting_yes()

@then(u'I should see the message "You have selected Yes"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have selected Yes"')
    context.demoqa_pages.assert_yes_radio_button()

@when(u'I select the "Impressive" radio button')
def step_impl(context):
    print(u'STEP: When I select the "Impressive" radio button')
    context.demoqa_pages.selecting_impressive()

@then(u'I should see the message "You have selected Impressive"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have selected Impressive"')
    context.demoqa_pages.assert_impressive_radio_button()

@when(u'I attempt to select the "No" radio button')
def step_impl(context):
    print(u'STEP: When I attempt to select the "No" radio button')
    context.demoqa_pages.click_no_button()

@then(u'the "No" radio button should be disabled')
def step_impl(context):
    print(u'STEP: Then the "No" radio button should be disabled')
    context.demoqa_pages.no_radio_button_disabled()

@when(u'I press the "Buttons" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Buttons" button under "Elements"')
    context.demoqa_pages.press_buttons_button()

@when(u'I double click the "Double Click Me" button')
def step_impl(context):
    print(u'STEP: When I double click the "Double Click Me" button')
    context.demoqa_pages.press_double_click()

@then(u'I should see the message "You have done a double click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a double click"')
    context.demoqa_pages.assert_double_click()

@when(u'I click the "Right Click Me" button')
def step_impl(context):
    print(u'STEP: When I click the "Right Click Me" button')
    context.demoqa_pages.press_right_click()

@then(u'I should see the message "You have done a right click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a right click"')
    context.demoqa_pages.assert_right_click()

@when(u'I click the "Click Me" button')
def step_impl(context):
    print(u'STEP: When I click the "Click Me" button')
    context.demoqa_pages.press_click_me()

@then(u'I should see the message "You have done a dynamic click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a dynamic click"')
    context.demoqa_pages.assert_click_me()

@when(u'I click the "Home" link button')
def step_impl(context):
    print(u'STEP: When I click the "Home" link button')
    context.demoqa_pages.press_home_button()

@then(u'I should be redirected to the Home page')
def step_impl(context):
    print(u'STEP: Then I should be redirected to the Home page')
    context.demoqa_pages.verify_new_home_page()

@when(u'I click the dynamic home link button')
def step_impl(context):
    print(u'STEP: When I click the dynamic home link button')
    context.demoqa_pages.dynamic_link_text_click()
@when(u'I press the "Links" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Links" button under "Elements"')
    context.demoqa_pages.press_links_button()
@when('I click on the "{link}" link')
def step_impl(context, link):
    context.demoqa_pages.click_on_the_link_api(link)
@then('I should receive a response with status code "{statuscode}" and status text "{statustext}"')
def step_impl(context, statuscode, statustext):
    context.demoqa_pages.message_from_api(statuscode, statustext)

