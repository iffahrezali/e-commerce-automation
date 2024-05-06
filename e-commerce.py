import time
import travel_info
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Initialize the browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

def openBrowser(input_link):
    driver.get(input_link)
    driver.maximize_window()

if __name__ == "__main__":
    input_link = 'https://www.saucedemo.com'
