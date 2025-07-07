from bs4 import BeautifulSoup
import lxml
import requests

#All list belong to the Collider site people, I just made the code to practice as a student
response = requests.get("https://collider.com/best-movies-of-all-time/")
col_wp = response.text

soup = BeautifulSoup(col_wp, "lxml")

movielist = soup.select("h2")

for movie in movielist:
    print(movie.getText().strip())