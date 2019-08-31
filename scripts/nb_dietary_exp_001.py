## Dieatary analisys

#%% [markdown]
# # An Analisys on dietary information collect by MyFitnessPal on Iphone
# In this file just basic charts and general exploratory stuff.
#%% loading stuff

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

data_path = "/Users/jguszr/AnacondaProjects/tsStudy/data/apple_health_export/summaries/"
fname = "dietary.csv"

df = pd.read_csv(data_path+fname)
df.head()
#%% [markdown]
# ## Data preping
# First  Ill work with the log_date field, in order generate more information
# such as if it week days or weekends. and how the pattern changes


#%%

df.log_date = pd.to_datetime(df.log_date)
df["is_weekend"] = df.log_date.dt.dayofweek>=5

#%%
df.head()

#%%
by_day = df.groupby(df.log_date.dt.date).sum()
by_day.head()
#%%
by_day.describe()

#%% [markdown]
# ok, lets see some simple stuff first.
# how my protein intake is differente in week days from weekends.

#%%
df[df.is_weekend==False].groupby(df.log_date.dt.date).Protein_g.mean().hist()
df[df.is_weekend==True].groupby(df.log_date.dt.date).Protein_g.mean().hist()
#%%
