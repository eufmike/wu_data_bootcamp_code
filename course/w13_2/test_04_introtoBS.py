# %%
# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
import re
from pprint import pprint
import pymongo
import pandas as pd

# %%
html_string = """
<html>
<head>
<title>
A Simple HTML Document
</title>
</head>
<body>
<p>This is a very simple HTML document</p>
<p>It only has two paragraphs</p>
</body>
</html>
"""

# %%
# Create a Beautiful Soup object
soup = bs(html_string, 'html.parser')
type(soup)

# Print formatted version of the soup
print(soup.prettify())

# %%
# Extract the title of the HTML document
soup.title

# %%
# Extract the text of the title
soup.title.text

# %%
# Clean up the text
soup.title.text.strip()
# %%
# Extract the contents of the HTML body
soup.body

# %%
# Extract the text of the body
soup.body.text

# %%
# Text of the first paragraph
soup.body.p.text

# %%
# Extract all paragraph elements
soup.body.find_all('p')

# %%
# The text of the first paragraph
soup.body.find('p').text