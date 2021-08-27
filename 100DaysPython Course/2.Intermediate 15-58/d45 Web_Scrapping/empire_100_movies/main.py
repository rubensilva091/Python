import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find_all(name="h3", class_="title"))


#CAN'T CONTINUE, THIS WEBSITE IS RENDERED WITH JS AND NOT WITH HTML AT FIRST HAND; SO BS4 DOESNT WORK