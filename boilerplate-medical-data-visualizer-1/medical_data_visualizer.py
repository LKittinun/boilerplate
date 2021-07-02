import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["BMI"] = df["weight"]/((df["height"]/100)**2)
df["overweight"] = df["BMI"].apply([lambda x: 1 if x > 25.0 else 0])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply([lambda x: 0 if x == 1 else 1])
df["gluc"] = df["gluc"].apply([lambda x: 0 if x == 1 else 1])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_dropped = df.drop(["ap_hi", "ap_lo", "height", "weight", "age", "BMI", "gender"], axis = 1)
    df_cat = pd.melt(df_dropped, id_vars = ["id","cardio"], var_name = "variable", value_name = "value")
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().rename(columns={"size": "total"})
    # Draw the catplot with 'sns.catplot()'
    ax = sns.catplot(x = "variable", hue = "value", data= df_cat, col ="cardio", kind = "count", 
                    order = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
    # ax.set_xlabels("variable")
    ax.set_ylabels("total")
    # ax.legend
    fig = ax.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_bp_h_w = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) & (df["weight"] <= df["weight"].quantile(0.975))]

    df_bp_h_w = df_bp_h_w.drop("BMI", axis = 1)
    
    df_heat = df_bp_h_w
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square= True, annot = True, annot_kws={'size': 8}, vmax= .24, fmt='0.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
