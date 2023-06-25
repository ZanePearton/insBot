# Selenium Website Automator

This Python script is a simple example of web automation using the Selenium WebDriver. It navigates to a specific website, logs in with the provided credentials, dismisses popups by clicking on 'Not Now' buttons and attempts to follow users.

## Project Structure

The script comprises of a single Python file and operates as follows:

1. Navigates to the desired URL using a Chrome WebDriver.
2. Waits for the page to load.
3. Locates the username and password fields and populates them with provided credentials.
4. Submits the form.
5. Dismisses any popup notifications.
6. Repeats the action of clicking the 'Follow' button five times.

## Getting Started

### Prerequisites

- Python 3
- Selenium (`pip install selenium`)
- ChromeDriver (compatible version with your Chrome browser)

### Setting Up

1. Clone this repository.
2. Install the prerequisites.
3. Replace the placeholder for the ChromeDriver path (`executable_path=r'C:\Users\....\source\repos\drivers\chromedriver86.exe'`) with the correct path to your downloaded ChromeDriver.
4. Replace the email and password placeholder values with your actual credentials or environmental variables.

### Running the Script

1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Run `python filename.py`, replacing 'filename' with the name of the Python script.

## Note

Please use this script responsibly. Automated actions may be against the terms of service of some websites. Always ensure that your actions respect the rules and policies of the website you are interacting with. 

## Author

[Zane Pearton](https://www.linkedin.com/in/zane-pearton/)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
