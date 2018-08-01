# %%
import os, sys
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from cycler import cycler
import time
from citipy import citipy

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

# range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)
samplesize = 1500

lat_lngs = []
cities = []
# Create a set of random lat and lng combination
'''
lats = np.random.uniform(low = lat_range[0], high = lat_range[1], size = samplesize)
lngs = np.random.uniform(low = lng_range[0], high = lng_range[1], size = samplesize)
'''

lats = scipy.stats.uniform.rvs(loc = 0, scale = Dx, size = ((N, 1)), random_state=seed)
lngs = scipy.stats.uniform.rvs(loc = 0, scale = Dx, size = ((N, 1)), random_state=seed)

lat_lngs = zip(lats, lngs)

for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    if city not in cities:
         cities.append(city)

len(cities)

