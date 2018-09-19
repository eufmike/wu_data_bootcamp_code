# %%
# Dependencies
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
from pprint import pprint
import pymongo
import pandas as pd

# %%
url = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'
tables = pd.read_html(url)
tables

# %%
type(tables)

# %%
df = tables[0]
type(df)

# %%
df.iloc[0]

# %%
df['State']

# %%
html_table = df.to_html()
html_table