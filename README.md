# AutomatedTestingBDDDemoQA

This project contains automated UI tests using **Behavior-Driven Development (BDD)** for [DemoQA](https://demoqa.com/). It's built with Python, Behave, and Selenium WebDriver.

## 🔧 Tech Stack

- Python 3
- Behave (BDD)
- Selenium WebDriver
- ChromeDriver (or any other WebDriver)
- Page Object Model (POM) design

## 🧪 Tested Features

- **Text Box**: Fill and submit forms
- **Check Box**: Expand and select Desktop
- **Radio Buttons**: Select Yes / Impressive, check No disabled
- **Buttons**: Double click, right click, and dynamic click
- **Links**: Normal and dynamic Home links
- **Broken Links & Images**: Detect broken vs valid images/links
- **API Response Links**: Test status codes like 201, 204, 301, 400, 401, 403, 404

## 📁 Project Structure

```

AutomatedTestingBDDDemoQA/
├── behave.ini               # Behave config file
├── browser.py               # Driver setup
├── demoqa\_report.html       # Test result export (manual)
├── environment.py           # Hooks (setup/teardown)
├── features/
│   ├── demoqa.feature       # Gherkin test scenarios
│   ├── steps/               # Step definitions
├── pages/                   # Page Object Models
├── README.md                # You're reading it

````

## ▶️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/poprobert0412/AutomatedTestingBDDDemoQA.git
cd AutomatedTestingBDDDemoQA
````

### 2. Install dependencies

If you don’t have a `requirements.txt`, run:

```bash
pip install selenium behave
```

### 3. Download the right ChromeDriver

Make sure your ChromeDriver version matches your browser:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Add it to your system `PATH`.

### 4. Run the tests

```bash
behave
```

## 📸 Example Scenario

```gherkin
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
  | Pop Robert  | poprobert1999@yahoo.com | Brasov         | Brasov           |
```

## 🧠 Notes

* Tests require an active internet connection.
* Works only if DemoQA site structure doesn't change.
* Page objects are under `/pages`, keeping logic clean.

## 👨‍💻 Author

**Pop Robert**
GitHub: [@poprobert0412](https://github.com/poprobert0412)
