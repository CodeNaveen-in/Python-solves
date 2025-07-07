from bs4 import BeautifulSoup
import lxml
import requests

header = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
date = input("Enter your required date to search in YYYY-MM-DD :\t")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date, headers=header)
#working without the header, but header added because sites deny requests without header (i.e. bot use on site)
#Special thanks to Billboard for letting me use code

billy_page = response.text
songlist = BeautifulSoup(billy_page, "lxml")
list_name = songlist.select("li.o-chart-results-list__item > h3")

print(f"\nThe top 100 songs of the {date} are: ")
num = 1
for i in list_name:
    print(f"{num}.",i.getText().strip())
    num+=1