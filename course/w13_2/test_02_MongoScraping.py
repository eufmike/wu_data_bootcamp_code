# %%
# Dependencies
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
from pprint import pprint
import pymongo

# %%
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
# These code will just create database and collection
db = client.craigslist_db
collection = db.items

# %%
param = {'sort':'rel', 'query':'guitar'}
url = 'https://newjersey.craigslist.org/search/sss'
response = requests.get(url, params = param)
print(response.url)
soup = BeautifulSoup(response.text, 'lxml')

# %%
results = soup.find_all('li', class_='result-row')
for result in results:
    try:
        title = result.find('a', class_ = 'result-title').text
        price = result.a.span.text
        link = result.a['href']
        
        if (title and price and link):
            print('==========')
            print(title)
            print(price)
            print(link)

            post = {
                'title': title,
                'price': price,
                'url':link
            }
            collection.insert_one(post)

    except AttributeError as e:
        print(e)

# %%
# Display items in MongoDB collection
listings = db.items.find()

for listing in listings:
    print(listing)