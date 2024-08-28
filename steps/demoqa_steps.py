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


@when(u'I press the Expand Button near the "Home" section')
def step_impl(context):
    print(u'STEP: When I press the Expand Button near the "Home" section')


@when(u'I press the checkbox labeled "Desktop"')
def step_impl(context):
    print(u'STEP: When I press the checkbox labeled "Desktop"')


@then(u'I should see the message: "You have selected : desktop notes commands"')
def step_impl(context):
    print(u'STEP: Then I should see the message: "You have selected : desktop notes commands"')


@when(u'I press the "Radio Button" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Radio Button" button under "Elements"')


@when(u'I select the "Yes" radio button')
def step_impl(context):
    print(u'STEP: When I select the "Yes" radio button')


@then(u'I should see the message "You have selected Yes"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have selected Yes"')


@when(u'I select the "Impressive" radio button')
def step_impl(context):
    print(u'STEP: When I select the "Impressive" radio button')


@then(u'I should see the message "You have selected Impressive"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have selected Impressive"')


@when(u'I attempt to select the "No" radio button')
def step_impl(context):
    print(u'STEP: When I attempt to select the "No" radio button')


@then(u'the "No" radio button should be disabled')
def step_impl(context):
    print(u'STEP: Then the "No" radio button should be disabled')


@when(u'I press the "Buttons" button under "Elements"')
def step_impl(context):
    print(u'STEP: When I press the "Buttons" button under "Elements"')


@when(u'I double click the "Double Click Me" button')
def step_impl(context):
    print(u'STEP: When I double click the "Double Click Me" button')


@then(u'I should see the message "You have done a double click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a double click"')


@when(u'I click the "Right Click Me" button')
def step_impl(context):
    print(u'STEP: When I click the "Right Click Me" button')


@then(u'I should see the message "You have done a right click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a right click"')


@when(u'I click the "Click Me" button')
def step_impl(context):
    print(u'STEP: When I click the "Click Me" button')


@then(u'I should see the message "You have done a dynamic click"')
def step_impl(context):
    print(u'STEP: Then I should see the message "You have done a dynamic click"')
