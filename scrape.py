import requests
from bs4 import BeautifulSoup
import pprint
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")


links = soup.select(".storylink ")
votes = soup.select(".score")

# Making a function to sort votes from highes to lowest
def sort_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k["votes"], reverse= True)

# Making a function with two parameted
def hackernews(links, votes):
    hn = []
    for idx, item in enumerate(links):
        # more_link = soup.select(".morelink")
        title = links[idx].getText()
        href = links[idx].get("href", None)
        points = int(votes[idx].getText().replace(" points", ""))
        if points > 100:
            hn.append({"title": title, "link": href, "votes": points})
    return sort_by_votes(hn)

pprint.pprint(hackernews(links, votes))