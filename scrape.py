import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")


links = soup.select(".storylink ")
votes = soup.select(".score")

# Making a function with two parameted
def hackernews(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn

print(hackernews(links, votes))