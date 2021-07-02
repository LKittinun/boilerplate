import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ["date"], index_col = "date")

# Clean data
df = df.loc[(df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (12,6))
    #ax = sns.lineplot(df.index, df["value"],palette = "red")
    ax = plt.plot(df.index, df["value"],linestyle='solid', color = "red")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Month"] = df_bar.index.strftime("%B")
    df_bar["Year"] = df_bar.index.year
    df_barplot = df_bar.groupby(["Year", "Month"]).mean()
    df_barplot = df_barplot.reset_index()
    df_barplot["Year"] = df_barplot["Year"].astype("category")
    # Draw bar plot
    fig, ax = plt.subplots(figsize = (12,12))
    ax = sns.barplot(x ="Year",y = "value", data = df_barplot, hue = "Month", hue_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    ax.set_ylabel("Average Page Views")
    ax.set_xlabel("Years")
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (14,6))
    ax[0] = sns.boxplot(x = "year", y = "value", data = df_box, ax = ax[0])
    ax[1] = sns.boxplot(x = "month", y = "value", data = df_box, ax = ax[1], order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax[0].set_ylabel("Page Views")
    ax[1].set_ylabel("Page Views")
    ax[0].set_xlabel("Year")
    ax[1].set_xlabel("Month")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
