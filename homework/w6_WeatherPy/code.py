# %%
import os, sys
import numpy as np
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
from cycler import cycler
import time
from citipy import citipy
import requests
from pprint import pprint

# office
path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/homework/w6_WeatherPy'
# laptop
# path = '/Users/major_minor1982/Documents/code/Python/wu_data_bootcamp_code/homework/w6_WeatherPy'
os.chdir(path)

import api_keys
import imp
imp.reload(api_keys)

# %%
# output file path
outpath = "output/cities.csv"

# function creates random city coordinates
def randomcitycoor(lat_range, lng_range, samplesize, seed = None):
    lat_lngs = []
    # Create a set of random lat and lng combination
    lats = scipy.stats.uniform.rvs(loc = lat_range[0], scale = (lat_range[1] - lat_range[0]), size = samplesize, random_state=seed)
    lngs = scipy.stats.uniform.rvs(loc = lng_range[0], scale = (lng_range[1] - lng_range[0]), size = samplesize, random_state=seed +1)

    lat_lngs = list(zip(lats, lngs))
    return (lat_lngs, lats, lngs)
# %%
# range of latitudes and longitude
seed = 1999
lat_range = (-90, 90)
lng_range = (-180, 180)
samplesize = 1500

# print(len(lat_lngs))

# %%
cities = []
i = 0
maxsize = 1000
while i < maxsize:
    lat_lngs, lats, lngs = randomcitycoor(lat_range, lng_range, samplesize, seed)
    
    for lat_lng in lat_lngs:
        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
        if city not in cities:
            cities.append(city)
    
    i = len(cities)
    seed = seed + 1
    print(i)
    
len(cities)
cities = cities[0:200]
len(cities)

# %%
print(cities[0]) 

# %%
# OpenWeatherMap API Key
# Starting URL for Weather Map API Call
api_key = api_keys.api_key
units = 'imperial'
url = "http://api.openweathermap.org/data/2.5/weather?"
query_url = '{}appid={}&units={}&q='.format(url, api_key, units)
print(query_url)

# %%
test_cities = cities[0]
print(query_url + test_cities)
response = requests.get(query_url + test_cities).json()
pprint(response)

# %%
# set up lists for latitude, 
# Temperature (F) 
# Humidity (%) 
# Cloudiness (%)
# Wind Speed (mph)
lat = []
temp = []
humd = []
cloud = []
windspd  = []

# request cities information
for city in cities:
    response = requests.get(query_url + city).json()
    if response['cod'] != '404':
        lat.append(response['coord']['lat'])
        temp.append(response['main']['temp'])
        humd.append(response['main']['humidity'])
        cloud.append(response['clouds']['all'])
        windspd.append(response['wind']['speed'])
    else:
        lat.append(np.nan)
        temp.append(np.nan)
        humd.append(np.nan)
        cloud.append(np.nan)
        windspd.append(np.nan)
# %%
# construct data to dataframe
data = pd.DataFrame({
                    'City Name': cities,
                    'Latitude': lat,
                    'Temperature (F)': temp, 
                    'Humidity (%)': humd,
                    'Cloudiess (%)': cloud,
                    'Wind Speed (mph)': windspd 
                    })

data = data.dropna()
data = data.reset_index(drop = True)
data

# %%
p1 = plt.figure()
plt.scatter(data['Latitude'], data['Temperature (F)'])
p1.show()

# %%
p2 = plt.figure()
plt.scatter(data['Latitude'], data['Humidity (%)'])
p2.show()

# %%
p3 = plt.figure()
plt.scatter(data['Latitude'], data['Cloudiess (%)'])
p3.show()

# %%
p4 = plt.figure()
plt.scatter(data['Latitude'], data['Wind Speed (mph)'])
p4.show()