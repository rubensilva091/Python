from selenium import webdriver
import time

driver_chrome = 'devSelenium\chromedriver.exe'
url_cookie = 'https://orteil.dashnet.org/cookieclicker/'


driver = webdriver.Chrome(executable_path=driver_chrome)

driver.get(url=url_cookie)

# drivers
click_cookie = driver.find_element_by_id('bigCookie')
cookies = driver.find_element_by_xpath('//*[@id="cookies"]')




def get_cookies():
    cokies_number = cookies.text.split('\n')
    cokies_number = cokies_number[0].split(' ')
    cokies_number = cokies_number[0]
    return cokies_number[0]


def buy_upgrade():
    upgrades = driver.find_elements_by_id('upgrades')
    for upg in upgrades:
        upg.click()

def buy_products():
    produtcs=driver.find_elements_by_id('products')
    for prod in produtcs:
        prod.click()


cookies_number = 0
k = 100
while(True):
    click_cookie.click()
    if(k==0):
        buy_upgrade()
        buy_products()
        k=100
    k -=1

driver.quit()
