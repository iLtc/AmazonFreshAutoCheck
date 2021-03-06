# Amazon Fresh Auto Check

This script helps you to find available delivery slots on Amazon Fresh.

It uses selenium to drive the browser to do the check automatically. It supports Chrome and Firefox (I have not check yet) on macOS, Windows, and Linux (I have not check yet).

## Instructions

1. [Download](https://github.com/iLtc/AmazonFreshAutoCheck/archive/master.zip) this project.

2. Unzip the project file, go to the project folder, and run `pip install -r requirements.txt` to install dependencies.

3. Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome or [geckodriver](https://github.com/mozilla/geckodriver/) for Firefox. Rename the file to `chromedriver` and put it in the project folder.

4. Run `python amazon_fresh.py` to start the script. It will open a web browser in automated test mode and ask you to enter your Amazon login credentials. After you login and see the shopping cart page, go back to the script and hit enter to continue. The script will start to check.

## Known Issues

1. The web browser in automated test mode will not save anything after closing. That means every time you run the script, you have to enter your Amazon login credentials again. And if you rerun the script too frequently and enter your Amazon login credentials too frequently, Amazon may mark your account as a suspecius account and ask you to enter a code during the login procedure.
