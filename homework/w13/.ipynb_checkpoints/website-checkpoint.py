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

# %%
# dependency
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup
import pymongo
from splinter import Browser
import pandas as pd
import datetime as dt
import scrape_mars

# %%

data = scrape_mars()


# %%
# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    
    return render_template('index.html', listings = listings)

@app.route('/scrape')
def scraper():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
