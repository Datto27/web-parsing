from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.flashscore.ge/football/spain/laliga/")
content = request.text

soup = BeautifulSoup(content, "html.parser")

table = soup.find("div", {"class":"tableWrapper___aKAh9PH"})
print(table)
