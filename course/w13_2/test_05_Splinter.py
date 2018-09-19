# %%
from splinter import Browser
from bs4 import BeautifulSoup as bs

# %%
# for mac
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
!which chromedriver

# %%
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# %%
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# %%
for x in range(1, 6):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('span', class_='text')

    for quote in quotes:
        print('page:', x, '-------------')
        print(quote.text)

    browser.click_link_by_partial_text('Next')