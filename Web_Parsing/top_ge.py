import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.top.ge/")
content = request.text

soup = BeautifulSoup(content, "html.parser")

table_body = soup.find("tbody")
rating_holder = table_body.find_all("tr")
# print(rating_holder)

# print(rating_holder[0].find_all("td")[2].find("a").text)
# print(rating_holder[0].find_all("span", {"class":"stat_now_big"})[2].text)
# print(rating_holder[0].find_all("span", {"class":"stat_now_big"})[-3].text)

for item in rating_holder:
	# saitis dasaxelebebi
	title = item.find_all("td")[2].find("a").text
	print(title)
	# dgis ganmavlobashi mnaxvelta sashualo raodenoba
	avg_visit = item.find_all("span", {"class":"stat_now_big"})[2].text
	print(f"Avarage visitors during the day: {avg_visit}")
	# momxmareblebis raodenoba tvis ganmavlobashi
	month_vis = item.find_all("span", {"class":"stat_now_big"})[-3].text
	print(f"Visistors during the month: {month_vis}\n")