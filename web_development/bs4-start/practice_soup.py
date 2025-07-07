from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

link_text = []
link_upvote = []

# TODO: To fetch all the top news title and link
all_links = soup.select("span.titleline > a")
for link in all_links:
    a_text = link.getText()
    a_link = link['href']
    a_set=[]
    a_set.append(a_text)
    a_set.append(a_link)
    link_text.append(a_set)
    #print(f"{a_text} and the link is {a_link}")

# TODO: to fetch all the upvotes of top news
all_upvotes = soup.select("span.score")
for vote in all_upvotes:
    text = vote.getText()
    link_upvote.append(text)
    #print(text)

#print(link_text)
#print(link_upvote)

for i in range(len(link_text)):
    title,url = link_text[i]
    upvotes = link_upvote[i]
    print(f"\n{title} with {url} amd the upvotes are {link_upvote[i]}")

#At the end of any website if you add robots.txt - it gives you knowledge of what you can scrape