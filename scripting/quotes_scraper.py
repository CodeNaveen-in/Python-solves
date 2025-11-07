import requests
from bs4 import BeautifulSoup

# Customize this URL to your target site
URL = "https://quotes.toscrape.com/page/1/"

def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Failed to retrieve page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        print(f"💬 {text} — {author}")

if __name__ == "__main__":
    scrape_quotes(URL)