from bs4 import BeautifulSoup
import requests
import json

resp = requests.get("http://quotes.toscrape.com/author/Albert-Einstein/?fbclid=IwAR3l8clfWDfPSMeWsjVONJswz_fQL2kfPwgHrzn-5Q6OSJo6LriSO1b2H3Q")
soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)
name = soup.find("h3", class_="author-title").text.split("\n")[0]
birth_date = soup.find("span", class_="author-born-date").text.strip()
description = soup.find("div", class_="author-description").text.strip()

albert_json = {"name": name, "born_date": birth_date, "description": description}

with open("Einstein.json", "w") as wj:
    json.dump(albert_json, wj)

