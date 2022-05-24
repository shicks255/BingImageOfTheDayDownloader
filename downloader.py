# !python3

import time

import selenium
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from config import downloadLocation

url = 'https://www.bing.com/'

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": downloadLocation}
chromeOptions.add_experimental_option("prefs", prefs)

# Create Selenium WebDriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)
browser.get(url)

# wait a second
time.sleep(2)

# Scroll down a bit
html = browser.find_element(by=By.TAG_NAME, value="html");
html.send_keys(Keys.DOWN)
time.sleep(2)

try:
    action = ActionChains(browser)

    hoverDiv = browser.find_element(by=By.CLASS_NAME, value='musCard')
    downloadLink = browser.find_element(by=By.CLASS_NAME, value='downloadLink')
    action.move_to_element(hoverDiv).move_to_element(downloadLink).click(downloadLink).perform()

except selenium.common.exceptions.NoSuchElementException as e:
    print('element not found')
    browser.close()
    browser.quit()
    sys.exit()

# sleep for ten seconds before closing browser stuff
# just to make sure picture was finished downloading
time.sleep(10)

browser.close()
browser.quit()
sys.exit()
