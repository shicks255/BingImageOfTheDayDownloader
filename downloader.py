# !python3

import time
import selenium
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.bing.com/'

chromeOptions = webdriver.ChromeOptions()
downloadLocation = "F:/newBingBackgrounds"
prefs = {"download.default_directory" : downloadLocation}
chromeOptions.add_experimental_option("prefs", prefs)
webdriverPath = "C:/Python/chromedriver.exe"

# Create Selenium WebDriver
browser = webdriver.Chrome(executable_path = webdriverPath, chrome_options = chromeOptions)
browser.get(url)

# wait a second
time.sleep(2)

# Scroll down a bit
html = browser.find_element_by_tag_name("html");
html.send_keys(Keys.DOWN)
time.sleep(3)
html.send_keys(Keys.DOWN)
time.sleep(3)
html.send_keys(Keys.DOWN)
time.sleep(3)
html.send_keys(Keys.DOWN)
time.sleep(3)

# find button to download image of day
try:
    submit = browser.find_element_by_id('vs_bs_download')
    submit.click()
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


