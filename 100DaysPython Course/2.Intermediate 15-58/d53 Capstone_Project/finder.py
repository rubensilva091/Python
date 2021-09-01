from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

docs_form = 'https://docs.google.com/forms/d/e/1FAIpQLSckBRPBQMrhDVmSKfBnMuSzf60WWop2u34NxpEm0ZskHyH9Yg/viewform?usp=sf_link'
docs_form_sheet='https://docs.google.com/forms/d/1eyH8c464Qw01_yujDs9E2mqtn0WYn3mub0Dx4Z4CCGc/edit#responses'
chrome_driver = 'devSelenium\chromedriver.exe'
website = 'https://www.zillow.com/homes/for_rent/'


class Finder():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def param(self, location, price, number_beds):
        self.driver.get(website)
        time.sleep(3)

        # procurar na search box
        search_box = self.driver.find_element_by_xpath(
            '//*[@id="srp-search-box"]/form/div[1]/input')
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        search_box.send_keys(location)
        time.sleep(1)  # se for instaneo sou considerado bot
        search_box.send_keys(Keys.ENTER)

        # price
        time.sleep(1)
        price_box = self.driver.find_element_by_xpath('//*[@id="price"]')
        price_box.click()
        time.sleep(0.5)
        price_box_max = self.driver.find_element_by_xpath(
            '//*[@id="price-exposed-max"]')
        price_box_max.click()
        price_box_max.send_keys(price)
        price_box_max.send_keys(Keys.ENTER)

        # number_beds
        time.sleep(1)
        attach = '['+str(number_beds)+']'
        xpath_variable = '//*[@id="beds-form"]/fieldset[1]/div[1]/button'+attach
        bed_box = self.driver.find_element_by_xpath('//*[@id="beds"]')
        bed_box.click()
        time.sleep(0.5)
        bed_box_quant = self.driver.find_element_by_xpath(xpath_variable)
        bed_box_quant.click()
        bed_box_quant.send_keys(Keys.ENTER)
        time.sleep(0.4)
        # clickar no botao done
        self.driver.find_element_by_xpath(
            '//*[@id="search-page-react-content"]/section/div[2]/div/div[3]/div/div/div/button').click()

        # new url
        self.new_url = self.driver.current_url

    def get_rentals(self):
        time.sleep(1.5)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        response = requests.get(self.new_url, headers=header)
        rentals = BeautifulSoup(response.text, 'html.parser')

        # Rental price
        self.rentals_result_price = rentals.find_all(
            name="div", class_="list-card-price")
        self.rentals_result_price = self.filter_list_price(
            self.rentals_result_price)

        # Rental address
        self.rentals_result_adress = rentals.find_all(
            name="address", class_="list-card-addr")
        self.rentals_result_adress = self.filter_list_address(
            self.rentals_result_adress)

        # links
        self.rentals_result_link = rentals.find_all(
            name="a", class_="list-card-link list-card-link-top-margin list-card-img")
        self.rentals_result_link = self.filter_list_link(
            self.rentals_result_link)

        self.number = len(self.rentals_result_price)
        # tests
        # self.print_list(self.rentals_result_price)
        # self.print_list(self.rentals_result_adress)
        # self.print_list(self.rentals_result_link)

    def fill_forms(self):
        inicial_url = 'https://www.zillow.com/'
        counter = len(self.rentals_result_link)
        for i in range(0, self.number):
            self.driver.get(docs_form)
            time.sleep(2)
            address = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
            address.send_keys(self.rentals_result_adress[i])
            price.send_keys(self.rentals_result_price[i])

            # evitar um bug, o site da zillow de vez em quando muda o html
            # entao mais vale ignorar
            if(counter > 0):
                if(self.rentals_result_link[i][0] == '/'):
                    link.send_keys(inicial_url)
                link.send_keys(self.rentals_result_link[i])
                counter -= 1

            time.sleep(1)
            submit_button.click()
            time.sleep(1)


    def create_sheets(self, location):
        self.driver.get(docs_form_sheet)
        time.sleep(2)
        create_sheet = self.driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span')
        create_sheet.click()

        create_title_sheet = self.driver.find_element_by_xpath('//*[@id="wizViewportRootId"]/div[10]/div/div[2]/span/div/div/span/div[1]/div/div/div[1]/div/div[1]/input')
        create_title_sheet.send_keys(location)

        create_button = self.driver.find_element_by_xpath('//*[@id="wizViewportRootId"]/div[10]/div/div[2]/div[3]/div[2]/span/span')
        create_button.click()

        options_button =self.driver.find_element_by_xpath('//*[@id="wizViewportRootId"]/div[10]/div/div[2]/div[3]/div[2]/span/span')
        options_button.click()

        time.sleep(2)
        sheet_url = self.driver.current_url
        self.driver.get(sheet_url)


    # filtrar a informacao principal

    def filter_list_price(self, list):
        new_list = []
        for elem in list:
            if(elem.text.find('+') != -1):
                new_list.append(elem.text.split('+')[0])
            elif(elem.text.find('/') != -1):
                new_list.append(elem.text.split('/')[0])
            elif(elem.text.find(' ') != -1):
                new_list.append(elem.text.split(' ')[0])
            else:
                new_list.append(elem.text)
        return new_list

    def filter_list_address(self, list):
        new_list = []
        for elem in list:
            new_list.append(elem.text)
        return new_list

    def filter_list_link(self, list):
        new_list = []
        for elem in list:
            new_list.append(elem['href'])
        return new_list

    # debugging

    def print_list(self, list):
        for elem in list:
            print(elem)
        print(len(list))
        print('\n\n')

    def close(self):
        self.driver.quit()
