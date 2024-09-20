Feature: Testing the Opencart website

  Background:
    Given I am on the main page
@text_box
  Scenario Outline: Filling and submitting the text box form
    When I press the "Text Box" button under "Elements"
    And I enter "<fullname>" in the Full Name field
    And I enter "<email>" in the Email field
    And I enter "<currentaddress>" in the Current Address field
    And I enter "<permanentaddress>" in the Permanent Address field
    And I press the Submit button
    Then I should see my entered information displayed below "<fullname>" "<email>" "<currentaddress>" "<permanentaddress>"
    Examples:
      | fullname    | email                   | currentaddress | permanentaddress |
      | Pop Robert  | poprobert1999@yahoo.com | Brasov         | Brasov          |
      | Pop Radu    | popradu1999@yahoo.com   | Bucuresti      | Brasov          |
      | Pop Roxana  | poproxana1999@yahoo.com | Iasi           | Brasov          |

@check_box
  Scenario: Selecting the Desktop checkbox
    When I press the "Check Box" button under "Elements"
    And I press the Expand Button near the "Home" section
    And I press the checkbox labeled "Desktop"
    Then I should see the message: "You have selected : desktop notes commands"

@yes_radio_button
  Scenario: Selecting the "Yes" radio button
    When I press the "Radio Button" button under "Elements"
    And I select the "Yes" radio button
    Then I should see the message "You have selected Yes"

@impressive_radio_button
  Scenario: Selecting the "Impressive" radio button
    When I press the "Radio Button" button under "Elements"
    And I select the "Impressive" radio button
    Then I should see the message "You have selected Impressive"

@no_radio_button
  Scenario: Trying to select the "No" radio button
    When I press the "Radio Button" button under "Elements"
    And I attempt to select the "No" radio button
    Then the "No" radio button should be disabled

@double_click_me_button
  Scenario: Pressing the "Double Click Me" button
    When I press the "Buttons" button under "Elements"
    And I double click the "Double Click Me" button
    Then I should see the message "You have done a double click"

@right_click_me_button
  Scenario: Pressing the "Right Click Me" button
    When I press the "Buttons" button under "Elements"
    And I click the "Right Click Me" button
    Then I should see the message "You have done a right click"

@click_me_button
  Scenario: Pressing the "Click Me" button
    When I press the "Buttons" button under "Elements"
    And I click the "Click Me" button
    Then I should see the message "You have done a dynamic click"

@home_link_button
  Scenario: Pressing the "Home" link button
    When I press the "Links" button under "Elements"
    And I click the "Home" link button
    Then I should be redirected to the Home page

@home_link_button_dynamic
  Scenario: Pressing the dynamic Home link button
    When I press the "Links" button under "Elements"
    And I click the dynamic home link button
    Then I should be redirected to the Home page


@api_links
  Scenario Outline: Verify link response and status code
    When I press the "Links" button under "Elements"
    And I click on the "<link>" link
    Then I should receive a response with status code "<statuscode>" and status text "<statustext>"

    Examples:
      | link          | statuscode | statustext  |
      | Created       | 201        | Created     |
      | No Content    | 204        | No Content  |
      | Moved         | 301        | Moved Permanently       |
      | Bad Request   | 400        | Bad Request |
      | Unauthorized  | 401        | Unauthorized|
      | Forbidden     | 403        | Forbidden   |
      | Not Found     | 404        | Not Found   |

@verify_valid_image
  Scenario: Verify Valid Image
    When I press the "Broken Links - Images" under "Elements"
    Then I should see a Valid Image


  Scenario: Verify Broken Image
    When I press the "Broken Links - Images" under "Elements"
    Then I should see a Broken Image


@verify_valid_link
  Scenario: Verify Valid Link
    When I press the "Broken Links - Images" under "Elements"
    And I see a blue link saying "Click Here for Valid Link" and click it
    Then I am redirected to the main page

@verify_broken_link
  Scenario: Verify Broken Link
    When I press the "Broken Links - Images" under "Elements"
    And I should see a blue link saying "Click Here for Broken Link" and click it
    Then I will be redirected to a page with status code 500

