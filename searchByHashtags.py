from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logininfo as user
import time

browser = webdriver.Chrome(# Enter the location of your chromedriver file)
browser.get("https://twitter.com/")
time.sleep(3)

# loginTwitter
sign_in = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
sign_in.click()
time.sleep(5)

usernameInput = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
passwordInput = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

usernameInput.send_keys(user.username)
passwordInput.send_keys(user.password)
time.sleep(3)

loginButton = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
loginButton.click()
time.sleep(10)
# Now we are logged in to twitter (We are in Main Page or Timeline)

# READY FOR SEARCH ANY HASHTAG IN TWITTER
# Get Search Input Area First
searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
# Send (set hashtag to search input area) any hashtag you specify
searchArea.send_keys("#BigData")
time.sleep(3)

# Press Enter after typed a hashtag to start searching
searchArea.send_keys(Keys.ENTER)
time.sleep(8)

# Navigating History in Browser use - driver.forward() / driver.back()
# To return previous page (TimeLine)
browser.back()
time.sleep(5)

browser.close()