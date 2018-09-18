# %%
# Dependencies
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
from pprint import pprint

# %%
param = {'sort':'rel', 'query':'guitar'}
url = 'https://newjersey.craigslist.org/search/sss'
response = requests.get(url, params = param)
print(response.url)

# %%
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# %%
results = soup.find_all('li', class_='result-row')
print(results[0].prettify())

# %%
for result in results:
    try:
        title = result.find('a', class_ = 'result-title').text
        title2 = result.find('a', class_ = 'result-title')
        title3 = result.a.text
        price = result.a.span.text
        price2 = result.a.find('span', class_ = 'result-price').text
        link = result.a['href']
        
        if (title and price and link):
            print('==========')
            print(title)
            print(title2)
            #print(title3)
            print(price)
            print(price2)
            print(link)
    except AttributeError as e:
        print(e)

    break





