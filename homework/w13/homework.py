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
driver = webdriver.Chrome(executable_path = "/anaconda3/envs/wudata/bin/chromedriver")
url ='https://mars.nasa.gov/news/'
driver.get(url)
html = driver.page_source
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
# %%
# * Visit the url for JPL Featured Space Image [here]
# (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use splinter to navigate the site and find the image url for 
#   the current Featured Mars Image and assign the url string to a 
#   variable called `featured_image_url`.
# * Make sure to find the image url to the full size `.jpg` image.
# * Make sure to save a complete url string for this image.


executable_path = {"executable_path": "/anaconda3/envs/wudata/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
html = browser.html
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

