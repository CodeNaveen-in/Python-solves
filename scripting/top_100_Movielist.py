from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://collider.com/best-movies-of-all-time/")
col_wp = response.text

soup = BeautifulSoup(col_wp, "lxml")

movielist = soup.select("h2")

for movie in movielist:
    print(movie.getText().strip())