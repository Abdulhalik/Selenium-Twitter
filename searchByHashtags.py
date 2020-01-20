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
searchArea.send_keys("#SakirKocabas")
time.sleep(3)

# Press Enter after typed a hashtag to start searching
searchArea.send_keys(Keys.ENTER)
time.sleep(5)

tweetList = []
# Tweet Text Selectors
selectors = ".css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0"
tweetTexts = browser.find_elements_by_css_selector(selectors)

for tweet in tweetTexts:
    tweetList.append(tweet.text)

# To run the JavaScript in Selenium use execute.script()
# To get all tweets browser must be scrolled, and this'll load another tweets so, to do this we have to run a simple script
# -- Suana dek sadece yuklenen tweetleri alabiliyoruz. Daha fazla tweet icin browseri scroll edip yeni tweetler yuklemeliyiz.
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage = document.body.scrollHeight;return lenOfPage;")
print(lenOfPage)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(3)
    # While scroll ends, do new scroll in every step
    # -- Sayfanin sonuna gelene kadar surekli scroll et.
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage = document.body.scrollHeight;return lenOfPage;")
    print(lenOfPage)
    if lastCount == lenOfPage:
        match = True

tweetTexts = browser.find_elements_by_css_selector(selectors)

tweetList.pop()
for tweet in tweetTexts:
    tweetList.append(tweet.text)

time.sleep(5)

# Write all tweets into the Txt File
tweetCount = 1
with open("tweets.txt", "w", encoding= "UTF-8") as file:
    file.write("TWITTER - TWEETS ABOUT 'SAKIR KOCABAS' - #sakirkocabas \n")
    file.write("\n------------------------------------------------------\n")
    for tweet in tweetList:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("*****************************************************\n")
        tweetCount += 1

# Navigating History in Browser use - driver.forward() / driver.back()
# To return previous page (TimeLine)
browser.back()
time.sleep(5)

browser.close()
