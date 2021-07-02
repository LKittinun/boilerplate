#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
#%%
df = pd.read_csv("epa-sea-level.csv")
#%%
df.describe()
#%%
res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
intercepts = res.intercept
coef = res.slope
year_range = list(range(1880, 2051))
sea_level = []

for year in year_range:
    sea_level.append(intercepts + coef*year)
#%%
df2 = df[df["Year"] >= 2000]
res2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
intercepts2 = res2.intercept
coef2 = res2.slope
year_range2 = list(range(2000, 2051))
sea_level2 = []

for year in year_range2:
    sea_level2.append(intercepts2 + coef2*year)
#%%
fig, ax = plt.subplots()

ax.scatter(x = "Year", y = "CSIRO Adjusted Sea Level", data = df, label = 'Data')
ax.plot(year_range, sea_level,c ='r', label = 'Fit1')
ax.plot(year_range2,sea_level2,c ='g', label = 'Fit2')

ax.set_xlabel("Year")
ax.set_ylabel("Sea Level (inches)")
ax.set_title("Rise in Sea Level")
ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

plt.show()
fig.savefig('sea_level_plot.png')