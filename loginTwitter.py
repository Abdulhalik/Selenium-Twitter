from selenium import webdriver
import logininfo as user # look at ReadMe file
import time

browser = webdriver.Chrome(# Enter the location of your chromedriver file)
browser.get("https://twitter.com/")
time.sleep(3)

# Get Sign In Button
sign_in = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")

sign_in.click()
# Redirected to login page
time.sleep(5)

# Get input areas
usernameInput = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
passwordInput = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

# Sending Data to Browser use send_keys()
usernameInput.send_keys(user.username)
passwordInput.send_keys(user.password)

time.sleep(3)

# Click Login
loginButton = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
loginButton.click()

time.sleep(10)

browser.close()
