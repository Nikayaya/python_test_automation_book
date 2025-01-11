### Preconditions

You will need the following:
- Python 3.x installed on your system.
- The Playwright Python package.
- Browsers for Playwright (typically, the Chromium browser is used for tests).

### Installation

1. **Install Python**  
   If you haven't installed Python yet, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Playwright and Required Browsers**  
   Once Python is installed, you can use `pip` to install Playwright and download the necessary browser binaries. Run the following commands in your terminal or command prompt:
   ```bash
   pip install playwright
   playwright install
   
### Project Structure
This project includes the following files:

text_box_page.py: Contains the page object module used for handling UI interactions.
test_text_box.py: Contains the Python script that performs the automated tests using the constructs defined in the page object module.
README.md: Provides detailed information about the project setup and how to run the tests.

### Running the Tests
To run the tests, proceed as follows:

Open your terminal or command prompt.
Navigate to the directory containing your test script. For example:

cd /path/to/your/project

Execute the test script using Python:

python test_text_box.py

### Modifying the Tests
To modify the tests or adapt the page object to changes in the website's UI, edit the text_box_page.py file. Ensure that the locators (input, button, etc.) match those found in the HTML of the webpage.

### Troubleshooting
If you encounter issues with running Playwright tests, consider the following:

Ensure all Playwright dependencies were correctly installed using playwright install.
Make sure that your project's Python environment has access to Playwright (verify installed packages using pip list).
Check the browser console for errors if a test fails to interact with the UI as expected.

