# from bs4 import BeautifulSoup
#
# with open("index.html", "r") as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, "lxml")  # (content, "parser method")
#     # print(soup.prettify())
#     # tags = soup.find_all("h5")  # for find every <h5> tags
#     # # print(tags)
#     # for course in tags:
#     #     print(course.text)  # for show tags texts
#
#     course_cards = soup.find_all("div", class_="card")
#     for course in course_cards:
#         course_name = course.h5.text  # make variable course_name, courses tags are <h5>, end make this by text
#         course_price = course.a.text.split()[-1]  # make variable for course price
#         print(f"{course_name} costs: {course_price}")



# # REAL WEBSITE ///////////>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from bs4 import BeautifulSoup
# import requests
#
# html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# soup = BeautifulSoup(html_text, "lxml")
# # print(soup)
#
#
# # # take first job element, name of company
# # job = soup.find("li", class_="clearfix job-bx wht-shd-bx")
# # company_name = job.find("h3", class_="joblist-comp-name").text.strip()
# # skills = job.find("span", class_="srp-skills").text.strip().replace(" ", "")
# # published_date = job.find("span", class_="sim-posted").span.text
# #
# # print(f"Company name: {company_name} \nRequired skills: {skills}")
# # print(published_date)
#
#
# # # its take out only first page jobs
# # jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")  # (list element, class of list)
# # print(jobs)
# # for job in jobs:
# #     company_name = job.find("h3", class_="joblist-comp-name").text.strip()
# #     skills = job.find("span", class_="srp-skills").text.strip().replace(" ", "")
# #     published_date = job.find("span", class_="sim-posted").span.text
# #     location = job.find("span").text
# #
# #     print(f"Company name: {company_name} \nSkills: {skills}")
# #     print(published_date)
# #     print(f"Location: {location}\n")
# #
#
#
#
# its take out first page jobs, clear by published date, more info ....
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills which you are good")
familiar_skill = input(">>> ")
print(f"Filtering out {familiar_skill}...")

def find_job():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")  # (list element, class of list)
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            skills = job.find("span", class_="srp-skills").text.strip().replace(" ", "")
            location = job.find("span").text
            more_info = job.header.h2.a["href"]
            if familiar_skill in skills:
                with open(f"Posts/{index}.txt", "w") as f:
                    f.write(f"Company name: {company_name} \nSkills: {skills}\n")
                    f.write(published_date+"\n")
                    f.write(f"Location: {location}\n")
                    f.write(f"More info: {more_info}\n")
                print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        find_job()
        time_wait = 5
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)



