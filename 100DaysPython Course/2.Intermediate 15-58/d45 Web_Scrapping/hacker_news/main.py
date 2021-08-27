from bs4 import BeautifulSoup
import requests

URL ="https://news.ycombinator.com/news"

response = requests.get(URL)
yc_web_page = response.text

soup= BeautifulSoup(yc_web_page, "html.parser")
final =soup.select_one(".storylink")
#final = soup.find(name="a", class_="storylink").text
top1_text =final.text
top1_link = final.get("href")
top1_upvote = soup.find(name="span", class_="score", id="score_28318972").text
print(top1_upvote)