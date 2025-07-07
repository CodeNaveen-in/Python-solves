from bs4 import BeautifulSoup
import lxml

with open("web_development/bs4-start/website.html") as file: #Pathway seems weird because the terminal is open in the top most directory
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

# TODO: Testing of BeautifulSoup
# print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)

all_anchors= soup.find_all(name="a")
#print(all_anchors)

for tag in all_anchors:
    #print(tag.getText)
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings=soup.select(".heading")
print(headings)