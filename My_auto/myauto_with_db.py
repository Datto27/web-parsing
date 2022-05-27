import requests
from bs4 import BeautifulSoup
import sqlite3


connection = sqlite3.connect("myauto.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
				cid INTEGER PRIMARY KEY AUTOINCREMENT,
				car_model VARCHAR,
				car_id VARCHAR,
				place VARCHAR,
				year INTEGER,
				engine VARCHAR,
				kilometrage VARCHAR,
				transmission VARCHAR,
				wheel VARCHAR,
				levy VARCHAR,
				price_usd VARCHAR,
				price_gel VARCHAR)''')

connection.commit()


# head = {"userAgent": "Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2909.25 Safari/537.36"}

# first_req = requests.get("https://www.myauto.ge/ka/s/0/0/25/ML-Klasse/2008/00/00/00/iyideba-mercedes-benz-ml-klasse-(%E1%83%A7%E1%83%95%E1%83%94%E1%83%9A%E1%83%90)-2008-geo?stype=0&for_rent=0&marka=25&model=ML-Klasse&year_from=2008&price_from=1000&currency_id=3&loc_id=1&det_search=0&ord=7&last_model=ML-Klasse&keyword=&category_id=m0&page=1")
# req_cont = first_req.text
# num_soup = BeautifulSoup(req_cont, "html.parser")
# last_page = num_soup.find("li", {"class":"pagination-li last-page"})
# a_number = last_page.find("a")["href"].split("=")[-1]

# BASE_URL = "https://www.myauto.ge/ka/s/0/0/25/ML-Klasse/2008/00/00/00/iyideba-mercedes-benz-ml-klasse-(%E1%83%A7%E1%83%95%E1%83%94%E1%83%9A%E1%83%90)-2008-geo?stype=0&for_rent=0&marka=25&model=ML-Klasse&year_from=2008&price_from=1000&currency_id=3&loc_id=1&det_search=0&ord=7&last_model=ML-Klasse&keyword=&category_id=m0&page="

# for page in range(1, int(a_number)):

# 	request = requests.get(BASE_URL+str(page), headers=head)
# 	content = request.text

# 	soup = BeautifulSoup(content, "html.parser")

# 	main_container = soup.find("div", {"class":"container-main"})

# 	cars_list = main_container.find_all("div", {"class":"car-short-info"})

# 	for item in cars_list:
# 		car_name_info = item.find("a").text.strip().split(" ")[1:]
# 		car_name = " ".join(car_name_info)

# 		car_id = item.find("div", {"class":"cr-vp-lbl"}).text

# 		year = item.find("p", {"class":"car-year"}).text.strip()

# 		try:
# 			levy = item.find("p", {"class":"car-levy passed"}).text.strip() 
# 		except: 
# 			levy = "განუბაჟებელი"

# 		engine = item.find("div", {"data-info":"ძრავი"}).text.strip()

# 		kilometrage = item.find("div", {"class":"cr-road"}).text.strip()

# 		transmission = item.find("div", {"class":"cr-wheel"}).text.strip()

# 		wheel = item.find("div", {"class":"cr-gas"}).text.strip()

# 		place = item.find("p", {"class":"car-list-row"}).text.strip().split()[0]

# 		prices = item.find("div", {"price-title-container"})
# 		price_gel = prices.find_all("label")[0].text.strip()
# 		price_usd = prices.find_all("label")[1].text.strip()


# 		cursor.execute('''INSERT INTO cars VALUES (
# 					NULL, ?,?,?,?,?,?,?,?,?,?,?)''',
# 					(car_name, car_id, place, year, engine, kilometrage, transmission, wheel, levy, price_usd, price_gel))
# 		connection.commit()

def get_db_cars():
	cursor.execute('''SELECT * FROM cars''')
	cars = cursor.fetchall()
	print(cars)


cursor.close()
connection.close()