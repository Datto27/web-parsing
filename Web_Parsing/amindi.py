import requests
from bs4 import BeautifulSoup

r = requests.get("https://amindi.ge")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data = soup.find("div", {"class":"weather-days-right"})
columns = data.find_all("div", {"class":"col px-0"})


for item in columns:

	print(item.find("div", {"class":"weekDay"}).text)
	print(item.find("p", {"class":"day"}).text)

	degrees = item.find_all("span")

	print(degrees[0].text, "-", degrees[1].text)
	print("\n")




