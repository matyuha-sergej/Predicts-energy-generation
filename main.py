import tensorflow as tf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

weather = pd.read_csv("weather.csv")
power = pd.read_csv("power.csv")
df = weather.merge(power[['datetime','power']], on='datetime')
# df = df.iloc[start:end]
print(df.head(5))
