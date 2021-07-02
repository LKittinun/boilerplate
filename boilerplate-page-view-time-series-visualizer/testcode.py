#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#%%
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ["date"], index_col = "date")
df = df.loc[(df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]
#%%
# isinstance(df.index, pd.DatetimeIndex)
df.value_counts
#%%
fig, ax = plt.subplots(figsize = (12,6))
ax = plt.plot(df.index, df["value"],       
        linestyle='solid', color = "red")
fig.savefig('line_plot.png')
#%%
df["Month"] = df.index.strftime("%B")
df["Year"] = df.index.year
df_barplot = df.groupby(["Year", "Month"]).mean()
df_barplot = df_barplot.reset_index()
df_barplot["Year"] = df_barplot["Year"].astype("category")
df_barplot.dtypes
#%%
fig, ax = plt.subplots(figsize = (12,12))
ax = sns.barplot(x ="Year",y = "value",data = df_barplot, hue = "Month", hue_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
ax.set_ylabel("Average Page Views")
ax.set_xlabel("Years")
fig.savefig('bar_plot.png')
#%%
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
df_box
#%%
fig, ax = plt.subplots(1, 2, figsize = (14,6))
ax[0] = sns.boxplot(x = "year", y = "value", data = df_box, ax = ax[0])
ax[1] = sns.boxplot(x = "month", y = "value", data = df_box, ax = ax[1], order = ["Jan", "Feb", "Mar", "April", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
ax[0].set_ylabel("Page Views")
ax[1].set_ylabel("Page Views")
ax[0].set_xlabel("Year")
ax[1].set_xlabel("Month")
fig.savefig('box_plot.png')