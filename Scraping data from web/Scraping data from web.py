import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
links  = soup.select('.storylink')
print(type(links))
subtext  = soup.select('.subtext')

soup2= BeautifulSoup(res2.text, 'html.parser')
links2  = soup2.select('.storylink')
subtext2  = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(collection):
    return sorted(collection, key = lambda k:k['votes'], reverse=True )
        

def create_customer_hn_news(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = votes[index].select('.score')
        if len(vote)>0:
            points = int(vote[0].getText().replace(" points",''))
            if points >= 100:
                hn.append({'title':title, 'Link': href, 'votes': points})
    return sort_stories_by_votes(hn) 

pprint.pprint(create_customer_hn_news(mega_links,mega_subtext))