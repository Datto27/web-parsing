from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.jobs.ge/?page=1&q=&cid=6&lid=&jid=")
content = request.text

soup = BeautifulSoup(content, "html.parser")

data = soup.find("div", {"class":"regularEntries"})
jobs_list = data.find_all("tr")

# print(jobs_list[1].find_all("td")[1].find("a").text)
# print(jobs_list[1].find_all("td")[3].text)
# print(jobs_list[1].find_all("td")[-1].text)

for index in range(1, len(jobs_list)):
	# Gancxadebis mokle agtsera
	title = jobs_list[index].find_all("td")[1].find("a").text
	if "" in title.lower():
		print(f" {index}) {title}")
		# kompaniis dasaxeleba
		com_name = jobs_list[index].find_all("td")[3].text
		print(com_name.strip())
		# vakansiis bolo vada
		last_date = jobs_list[index].find_all("td")[-1].text
		print(f"ბოლო ვადა ==> {last_date}")
