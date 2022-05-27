import requests
from bs4 import BeautifulSoup

URL = "https://www.imovies.cc/ka/movies?page=2&countries_related=no&genres_related=no&type=movie&without_watched_movies=no&language=GEO&sort=-upload_date"
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}

request = requests.get(URL, headers=header)
content = request.text
# print(content)
soup = BeautifulSoup(content, "html.parser")
print(soup)




