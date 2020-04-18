from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random

browser = webdriver.Chrome('./chromedriver')


def login():
    browser.get('https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%3Fie%3DUTF8%26app-nav-type%3Dnone%26dc%3Ddf%26dc%3Ddf%26path%3D%252Fgp%252Fcart%252Fview.html%253Fapp-nav-type%253Dnone%26ref_%3Dcart_empty_sign_in%26useRedirectOnSuccess%3D1')

    input('Please login in the Web Browser and then press Enter here.')


def proceed_to_checkout():
    print('Proceed To Checkout')

    browser.get('https://www.amazon.com/')

    browser.find_element_by_id("nav-cart").click()

    time.sleep(random.randint(3, 7))

    browser.find_element_by_class_name('a-button-input').click()

    time.sleep(random.randint(3, 7))

    browser.find_element_by_name('proceedToCheckout').click()


def check():
    print("\n=======")
    print("Checking ...")

    browser.get('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')

    time.sleep(random.randint(3, 7))

    if browser.current_url != 'https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1':
        seconds = random.randint(30, 60)

        print('Page Error!', "Will try again in {} seconds.".format(seconds))

        time.sleep(seconds)

        proceed_to_checkout()

        return False

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    availabilities = soup.find_all(class_='ufss-date-select-toggle-text-availability')

    result = False

    for availability in availabilities:
        if 'Not' not in availability.text:
            result = True

    if result:
        print('Found One!!!')

    else:
        print("Cannot find one.")

    return result


if __name__ == '__main__':
    login()
    proceed_to_checkout()

    while not check():
        seconds = random.randint(60, 120)

        print("Will check again in {} seconds.".format(seconds))

        time.sleep(seconds)
