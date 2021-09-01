from selenium import webdriver

chrome_driver = 'devSelenium\chromedriver.exe'
url = 'http://secure-retreat-92358.herokuapp.com/'


driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get(url)

top_form = driver.find_element_by_class_name('top')
mid_form = driver.find_element_by_class_name('middle')
bot_form = driver.find_element_by_class_name('bottom')
sign= driver.find_element_by_class_name('btn-block')

top_form.send_keys('Ruben')
mid_form.send_keys('Silva')
bot_form.send_keys('rubenfamalicao@live.com.pt')
sign.click()

driver.quit()
