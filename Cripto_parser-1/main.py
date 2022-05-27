import requests
from bs4 import BeautifulSoup
import re


URL = "https://coinmarketcap.com"

crypto_list = []

def send_request(link):
	request = requests.get(link)
	return request

def get_soup(content):
	soup = BeautifulSoup(content, "html.parser")
	return soup

def do_parse(soup):
	data = soup.find("tbody")
	rows = data.find_all("tr")
	dictionary = {}

	for index, item in enumerate(rows, 1):
		columns = item.find_all("td")
		dictionary["position"] = index
		try:
			dictionary["title"] = columns[2].find("p", class_="sc-1eb5slv-0 iJjGCS").text
		except:
			dictionary["title"] = columns[2].find("span", class_="crypto-symbol").text
	
		dictionary["link"] = URL + columns[2].find("a")["href"]
		
		page_soup = get_soup(send_request(dictionary["link"]).text)
		# print(page_soup)
		try:
			dictionary["cost"] = page_soup.find("div", class_="priceValue___11gHJ").text
			# print(dictionary["cost"])
		except:
			dictionary["cost"] = None
			# print(dictionary["cost"])

		print(f"{dictionary['position']}) {dictionary['title']} -----> {dictionary['cost']} \
				\n{dictionary['link']}\n")

		crypto_list.append(dictionary)
	# print(crypto_list)

do_parse(get_soup(send_request(URL).text))
