#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#%%
df = pd.read_csv("medical_examination.csv")
df
#%%
df.head() 
df["BMI"] = df["weight"]/((df["height"]/100)**2)
df["overweight"] = df["BMI"].apply([lambda x: 1 if x > 25.0 else 0])
df["cholesterol"] = df["cholesterol"].apply([lambda x: 0 if x == 1 else 1])
df["gluc"] = df["gluc"].apply([lambda x: 0 if x == 1 else 1])
df.head()
#%%
df_dropped = df.drop(["ap_hi", "ap_lo", "height", "weight", "age", "BMI", "gender"], axis = 1)
df_long = pd.melt(df_dropped, id_vars = ["id","cardio"], var_name = "variable", value_name = "value")
df_long
#%%
ax =sns.catplot(x = "variable", hue = "value", data= df_long, col ="cardio", kind = "count", order = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
ax.set_xlabels("variable")
ax.set_ylabels("total")
ax.savefig('catplot.png')

# %%
df_bp_h_w = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) & (df["weight"] <= df["weight"].quantile(0.975))]

df_bp_h_w = df_bp_h_w.drop("BMI", axis = 1)
df_bp_h_w
#%%
df_corr = df_bp_h_w.corr()
df_corr

mask = np.zeros_like(df_corr)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(16, 12))
ax = sns.heatmap(df_corr, mask=mask, square=True, annot = True, annot_kws={'size': 8}, vmax= .24, fmt='0.1f')
plt.show()

mask