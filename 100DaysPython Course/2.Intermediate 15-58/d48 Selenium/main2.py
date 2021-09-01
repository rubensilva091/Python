from selenium import webdriver

chrome_driver ='devSelenium\chromedriver.exe'
wikipedia_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(wikipedia_url)

number =driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(number.text)


driver.quit()