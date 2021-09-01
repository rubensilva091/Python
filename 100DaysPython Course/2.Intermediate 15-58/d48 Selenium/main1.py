from selenium import webdriver


python_url = "https://www.python.org/"
chrome_driver = "devSelenium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get(python_url)

upcoming_time = driver.find_elements_by_class_name("event-widget time")
upcoming_event = driver.find_elements_by_class_name("event-widget a")

final_dict = {}

for i in range(0, len(upcoming_event)-1):
    aux_dict = {}
    aux_dict['time'] = upcoming_time[i].text
    aux_dict['name'] = upcoming_time[i].text
    final_dict[f'{i}'] = aux_dict

print(final_dict)
driver.quit()
