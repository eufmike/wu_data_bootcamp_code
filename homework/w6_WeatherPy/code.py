# %%
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler
import time
from citipy import citipy

# office
# path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/homework/w6_WeatherPy'
# laptop
path = '/Users/major_minor1982/Documents/code/Python/wu_data_bootcamp_code/homework/w6_WeatherPy'
os.chdir(path)

import api_keys
import imp
imp.reload(api_keys)

# %%
outpath = "output/cities.csv"




