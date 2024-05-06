import time
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

def loginWebsite(username, password):

#Verify the website loads to the homepage
def homePage():
    
#Add items into shopping cart
def addItems():

#Verify numbers of items added to cart matched
def verifyItems():

#Check out the items from shopping cart
def checkoutItems():

#Proceed for payment
def payItems():
    

if __name__ == "__main__":
    input_link = 'https://www.saucedemo.com'
