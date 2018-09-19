# %%
from bs4 import BeautifulSoup
import requests
import webbrowser
from urllib.request import urlopen
import pymongo

# %%
url = 'https://newjersey.craigslist.org/search/sss'
param = {'sort': 'rel', 
        'query': 'guitar'}
response = requests.get(url, params=param)
print(response.url)

# %%
webbrowser.open(response.url)


# %%
response = requests.get(url)
print(response.status_code)

# %%
print(response.text, 'html.parser')
print(soup.prettify())

# %%
html = urlopen(url).read().decode('utf-8')
print(html)

# %%
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# %%
# Define database and collection
db = client.craigslist_db
collection = db.items

# %%
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')


# %%
# Examine the results, then determine element that contains sought info
# results are returned as an iterable list
results = soup.find_all('li', class_='result-row')

# Loop through returned results
for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.find('a', class_='result-title').text
        # Identify and return price of listing
        price = result.a.span.text
        # Identify and return link to listing
        link = result.a['href']

        # Run only if title, price, and link are available
        if (title and price and link):
            # Print results
            print('-------------')
            print(title)
            print(price)
            print(link)

            # Dictionary to be inserted as a MongoDB document
            post = {
                'title': title,
                'price': price,
                'url': link
            }

            collection.insert_one(post)

    except Exception as e:
        print(e)