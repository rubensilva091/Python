from selenium import webdriver

chrome_driver = 'devSelenium\chromedriver.exe'

twitter_url = 'https://twitter.com/i/flow/signup'

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get(twitter_url)

