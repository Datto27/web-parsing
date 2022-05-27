import requests 
from bs4 import BeautifulSoup


URL = "https://www.worldometers.info/coronavirus/"
# Show top 10 countryes by covid statistic (www.worldometers.info)

def send_request(link):
	request = requests.get(URL)
	return request

def get_soup(content):
	soup = BeautifulSoup(content, "html.parser")
	return soup

def do_parse(soup):
	table = soup.find("table", {"id":"main_table_countries_today"}).find_all("tbody")[0]
	rows = table.find_all("tr")

	for item in rows:

		country = item.find("a", class_="mt_a")
		if country is not None:
			position = int(item.find_all("td")[0].text)
			if position > 10: break
			# print(position)
			tot_recov = item.find_all("td")[6].text
			# print(tot_recov)
			print(f"{position}. {country.text} - {tot_recov}")
		else:
			continue

do_parse(get_soup(send_request(URL).text))
