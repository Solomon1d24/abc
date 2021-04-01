import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.reuters.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links =  soup.select('.article-heading')
Article_time = soup.select('.article-time')

def geturl(newslist):
    news = []
    for items in newslist:
        try:
            news.append(items.find('a')['href'])
        except:
            print('error')
    return news


def custom_reuters(links, time):
    news = []
    for index, items in enumerate(links):
        title = links[index].getText()
        url = geturl(links)
        href = url[index]
        href = 'https://www.reuters.com' + href
        t = time[index].select('.timestamp')
        times = t[0].getText()
        news.append({'Title': title, 'Link': href, 'Time': times})
    return news


pprint.pprint(custom_reuters(links, Article_time))