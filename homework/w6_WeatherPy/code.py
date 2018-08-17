'''
# Unit 6: Assignment - What's the Weather Like?
## Project: WeatherPy

Your objective is to build a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude
'''

# %%
# Dependency
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
import tqdm

# Specify directory and set the workspace
# office
# path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/homework/w6_WeatherPy'
# laptop
path = '/Users/major_minor1982/Documents/code/Python/wu_data_bootcamp_code/homework/w6_WeatherPy'
os.chdir(path)

# import api keys and use imp module to reload
import api_keys
import imp
imp.reload(api_keys)

# %%
'''
# Create random coordinates:
* Instead of using np.random.uniform, use scipy.stats.uniform
* Randomization is controlled by defined seed. 
'''

# %%
# create a fundtion for generating coordinates
def randomcitycoor(lat_range, lng_range, samplesize, seed = None):
    lat_lngs = []
    # Create a set of random lat and lng combination
    lats = scipy.stats.uniform.rvs(loc = lat_range[0], scale = (lat_range[1] - lat_range[0]), size = samplesize, random_state=seed)
    lngs = scipy.stats.uniform.rvs(loc = lng_range[0], scale = (lng_range[1] - lng_range[0]), size = samplesize, random_state=seed +1)

    lat_lngs = list(zip(lats, lngs))
    return (lat_lngs, lats, lngs)

# %%
'''
# Generate the list of cities according to the coordinates.
'''
# %%
seed = 1999

# define the range of latitudes and longitude and samplesize
lat_range = (-90, 90)
lng_range = (-180, 180)
samplesize = 1500

# Create the amount of cities based on the maxsize for each round
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
    
# trim down to the target size
target_size = 600
cities = cities[0:target_size]
len(cities)

# %%
'''
# Pull city information from Open Weather Map
* http://www.openweathermap.org
'''

# %%
# OpenWeatherMap API Key
# Starting URL for Weather Map API Call
api_key = api_keys.api_key
units = 'imperial'
url = "http://api.openweathermap.org/data/2.5/weather?"
query_url = '{}appid={}&units={}&q='.format(url, api_key, units)
print(query_url)

# %%
# print the first city for checking the procedure
# the parameter returned form the API
# https://openweathermap.org/current 
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
dataid = []
lat = []
lng = []
date = []
temp = []
humd = []
cloud = []
windspd  = []

# request cities information
for i in tqdm.trange(len(cities)):
# for city in cities:
    response = requests.get(query_url + cities[i]).json()
    if response['cod'] != '404':
        dataid.append(response['id'])
        lat.append(response['coord']['lat'])
        lng.append(response['coord']['lon'])
        date.append(response['dt'])
        temp.append(response['main']['temp'])
        humd.append(response['main']['humidity'])
        cloud.append(response['clouds']['all'])
        windspd.append(response['wind']['speed'])
    else:
        dataid.append(np.nan)
        lat.append(np.nan)
        lng.append(np.nan)
        date.append(np.nan)
        temp.append(np.nan)
        humd.append(np.nan)
        cloud.append(np.nan)
        windspd.append(np.nan)
# %%
# construct data to dataframe
data = pd.DataFrame({
                    'Data ID': dataid,
                    'City Name': cities,
                    'Latitude': lat,
                    'Longitude': lng,
                    'Date': date,
                    'Temperature (F)': temp, 
                    'Humidity (%)': humd,
                    'Cloudiess (%)': cloud,
                    'Wind Speed (mph)': windspd 
                    })

data = data.dropna()
data = data.reset_index(drop = True)
data

# %%
# save data to csv file
# output file path
outpath = "output/cities_weather_data.csv"
data.to_csv(outpath, index_label = None)

# %%
'''
# Make scatter plot:
* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude
'''

# %% 
# Retrive current date from sytem datetime
import datetime
now = datetime.datetime.now()
datatime = now.strftime("%m/%d/%y")
print(datatime)

# %%
p1 = plt.figure()
plt.scatter(x = data['Latitude'], y = data['Temperature (F)'], alpha = 0.3)
plt.title('City Latitude vs. Temperature ' + datatime)
plt.xlabel('Latitude')
plt.ylabel('Temperature ($^\circ$F)')
p1.show()

# %%
p2 = plt.figure()
plt.scatter(x = data['Latitude'], y = data['Humidity (%)'], alpha = 0.3)
plt.title('City Latitude vs. Humidity ' + datatime)
plt.xlabel('Latitude')
plt.ylabel('Humidity (%)')
p2.show()

# %%
p3 = plt.figure()
plt.scatter(x = data['Latitude'], y = data['Cloudiess (%)'], alpha = 0.3)
plt.title('City Latitude vs. Cloudiess ' + datatime)
plt.xlabel('Latitude')
plt.ylabel('Cloudiess (%)')
p3.show()

# %%
p4 = plt.figure()
plt.scatter(data['Latitude'], data['Wind Speed (mph)'], alpha = 0.3)
plt.title('City Latitude vs. Wind Speed ' + datatime)
plt.xlabel('Latitude')
plt.ylabel('Wind Speed (mph)')
p4.show()