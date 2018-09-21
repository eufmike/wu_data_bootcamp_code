# %%
# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
import re
from pprint import pprint
import pymongo
import pandas as pd
from splinter import Browser

# ================================================================

# Step 1 - Scraping
# ----------------------------------------------------------------
# 01 Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) 
# and collect the latest News Title and Paragraph Text. Assign the 
# text to variables that you can reference later.

# %%
# Beautifulsoup does not work
'''
url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
# param = {'page':'0', 'per_page':'40'}
# response = requests.get(url, params = param)
print(response.url)

soup = bs(response.text, 'html5lib')
print(soup.prettify())
'''

# %%
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "/Users/michaelshih/anaconda3/envs/wudata/bin/chromedriver")
url ='https://mars.nasa.gov/news/'
driver.get(url)
html = driver.page_source
driver.quit()
# print(html)
soup = bs(html, 'lxml')
print(soup.prettify())

# %%
news_title = soup.find('div', 'content_title', 'a').text
news_p = soup.find('div', 'rollover_description_inner').text

print(news_title)
print(news_p)

# ----------------------------------------------------------------
# 02 
# * Visit the url for JPL Featured Space Image [here]
# (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use splinter to navigate the site and find the image url for 
#   the current Featured Mars Image and assign the url string to a 
#   variable called `featured_image_url`.
# * Make sure to find the image url to the full size `.jpg` image.
# * Make sure to save a complete url string for this image.

# %%
executable_path = {"executable_path": "/Users/michaelshih/anaconda3/envs/wudata/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
html = browser.html
browser.quit()
soup = bs(html, "lxml")
print(soup.prettify())

# %%
# a = soup.findAll('li', class_='slide')

image_url = soup.findAll('a', class_="fancybox")
addresslist = []
for address in image_url:
    addresslist.append(address['data-fancybox-href'])
    
# print(addresslist)
matching = [s for s in addresslist if "largesize" in s]
print(matching[0])

featured_image_url = "https://www.jpl.nasa.gov" + matching[0]
print(featured_image_url)

# ----------------------------------------------------------------
# 03
# Mars Weather
# * Visit the Mars Weather twitter account [here]
# (https://twitter.com/marswxreport?lang=en) and scrape the latest 
# Mars weather tweet from the page. Save the tweet text for the weather 
# report as a variable called `mars_weather`.

# %%
url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
# print(response.url)
soup = bs(response.text, 'lxml')
# print(soup.prettify())

mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
print(mars_weather)

# %%
# ----------------------------------------------------------------
# 04
# * Visit the Mars Facts webpage [here](http://space-facts.com/mars/) 
# and use Pandas to scrape the table containing facts about the planet 
# including Diameter, Mass, etc.
# * Use Pandas to convert the data to a HTML table string.

# %%
url = 'http://space-facts.com/mars/'
tables = pd.read_html(url)[0]
tables.columns = ['description', 'value']
tables.set_index('description', inplace=True)
tables




# %%
# ----------------------------------------------------------------
# 05
# * Visit the USGS Astrogeology site [here]
# (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
# to obtain high resolution images for each of Mar's hemispheres.
# * You will need to click each of the links to the hemispheres in order 
# to find the image url to the full resolution image.

# * Save both the image url string for the full resolution hemisphere image, 
# and the Hemisphere title containing the hemisphere name. Use a Python 
# dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title 
# to a list. This list will contain one dictionary for each hemisphere.
# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
response = requests.get(url)
soup = bs(response.text, 'lxml')

# %%
imgname = []
pageurls = []
for a in soup.find_all('a', class_= 'itemLink product-item'):
    if a.find('h3') != None:
        imgname.append(a.h3.text)
        pageurls.append('https://astrogeology.usgs.gov' + a['href'])
print(imgname)
print(pageurls)

# %%
imgurls = []
for url in pageurls:
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    # print(soup.prettify())
    for a in soup.find_all('a', {'target': '_blank'}, href =True):
        if a.text == 'Original':
            # print(a['href'])
            imgurls.append(a['href'])
print(imgurls)

# %%
hemisphere_image_urls = []
for i in range(len(imgurls)):
    hemisphere_image_urls.append({
        "title":imgname[i], "img_url":imgurls[i]
    })
print(hemisphere_image_urls)


# ================================================================


# Step 2 - MongoDB and Flask Application
# ----------------------------------------------------------------
# Use MongoDB with Flask templating to create a new HTML page that 
# displays all of the information that was scraped from the URLs above.

# * Start by converting your Jupyter notebook into a Python script 
# called `scrape_mars.py` with a function called `scrape` that will 
# execute all of your scraping code from above and return one Python 
# dictionary containing all of the scraped data.

# * Next, create a route called `/scrape` that will import your 
# `scrape_mars.py` script and call your `scrape` function.

# * Store the return value in Mongo as a Python dictionary.
# * Create a root route `/` that will query your Mongo database and 
# pass the mars data into an HTML template to display the data.

# * Create a template HTML file called `index.html` that will take 
# the mars data dictionary and display all of the data in the appropriate 
# HTML elements. Use the following as a guide for what the final product 
# should look like, but feel free to create your own design.

