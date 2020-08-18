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
        href = links[idx].get("href", None)
        points = int(votes[idx].getText().replace(" points", ""))
        if points > 100:
            hn.append({"title": title, "link": href, "votes": points})
    return hn

print(hackernews(links, votes))