# Simple Example Appium script

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from time import sleep

if __name__ == "__main__":

    desired_caps = {
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'platformName': 'Android',
        'deviceName': 'device',
        'platformVersion': '10',
        'noReset': 'true',
        'fullReset': 'false'
    }
    try:
        # Start driver for chrome browser
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        sleep(1)

        # Find url bar and click it
        url_bar = driver.find_element_by_id('com.android.chrome:id/url_bar')
        url_bar.click()

        sleep(1)

        # Enter google address
        url_bar.send_keys('google.com')

        sleep(1)

        driver.press_keycode(66)

        sleep(1)

        # We wait for the presence of the google search bar before doing anything else
        # We use Selenium's to wait for some time until the search bard has loaded
        # There is no ID for the search box so we use a bit of XPath to look for it

        search_box_xpath = '//android.view.View/android.widget.EditText'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))

        search_box = driver.find_element_by_xpath(search_box_xpath)
        driver.set_value(search_box, "toptechtips.github.io")

        # After entering the text into the search bar we then click search and wait
        # for the next page to load

        # We look for a widget Button with the text value 'Google Search'
        search_button_xpath = "//android.widget.Button[contains(@text, 'Google Search')]"
        driver.find_element_by_xpath(search_button_xpath).click()

        # After we click the search button, we must wait for the search results container to appear
        search_results_container_xpath = "//*[contains(@resource-id, 'rso')]"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_results_container_xpath)))

        # To get each result item, we first look for the container with the resource-id "rso"
        # Then the 2nd part of the xpath string will anything that is "a view of a view of a view"
        search_result_items_xpath = "//*[contains(@resource-id, 'rso')]//android.view.View/android.view.View/android.view.View"

        # Note how we use "find_elements..." instead of the usual "find_element"
        search_results = driver.find_elements_by_xpath(search_result_items_xpath)

        # We then only want to click on the first result
        first_result = search_results[0].click()

        # We can then scroll, or even screenshot...

    except Exception as e:
        print("Script Error: {0}".format(e))
