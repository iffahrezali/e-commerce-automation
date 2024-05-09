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
    driver.implicitly_wait(15)

def loginWebsite(username, password):
    try:
       username_box = driver.findElement(By.id("username"))
       username_box.sendKeys(username)
    
       password_box = driver.findElement(By.id("password"))
       password_box.sendKeys(password)
    
       login_button = driver.findElement(By.id("login-button"))
       login_box.click()
       print("Login successful")
    except:
       print("Login failed")

#Verify the website loads to the homepage
def homePage():
    website_title = driver.findElement(By.Id("Swag Labs"))
    
#Add items into shopping cart
def addItems():
    while 
       item1 = driver.findElement(By.id("Sauce Labs Backpack"))
       driver.execute_script("arguments[0].scrollIntoView()", item1)
       price1 = driver.find_element_by_class_name("price1")
       add_to_cart = driver.findElement(By.id("Add to Cart")
       add_to_cart.click()
    
       item2 = driver.findElement(By.id("Sauce Labs Bolt T-shirt"))
       driver.execute_script("arguments[0].scrollIntoView()", item2)
       price2 = driver.find_element_by_class_name("price2")
       add_to_cart = driver.findElement(By.id("Add to Cart")
       add_to_cart.click()

#Verify numbers of items added to cart matched
def verifyItems():
    #Scroll all the way to top
    driver.execute_script("window.scrollTo(0,0)")

    try:
       cart_icon = driver.findElement(By.id("cart-icon")
       cart_icon.click()
    except:
       loginWebsite(username, password)

#Check out the items from shopping cart
def checkoutItems():
    checkout_button = driver.findElement(By.id("Checkout")
    checkout_button.click()

#Proceed for payment
def payItems():
    first_name = driver.findElement(By.id("First Name"))
    first_name.sendKeys(user_first_name)
    last_name = driver.findElement(By.id("Last Name"))
    last_name.sendKeys(user_last_name)
    postcode = driver.findElement(By.id("Post code"))
    postcode.sendKeys(user_postcode)
    
    continue_button = driver.findElement(By.id("Continue")).click()   

def finalizeItems():
    checkout_overview = driver.findElement(By.id("Sauce Bolt T-Shirt")
    price_total = driver.findElements(By.id(items_total_price))
    finish_button = driver.findElement(By.id("Finish"))
    driver.execute_script("arguments[0].scrollIntoView()", finish_button)
    
    finish_button.click()
    driver.implicitly_wait(30)
    
    complete_message = driver.findElement(By.id("Thank you for your order"))
    
if __name__ == "__main__":
    input_link = 'https://www.saucedemo.com'
    username = abc@example.com
    password = PassWord@123
    user_first_name = "Sarsaparila"
    user_last_name = "binti Sarsi"
    user_postcode = "19900"
