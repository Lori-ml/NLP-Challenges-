#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# - The name of each column in sorted order
# - The total number of rows in the data frame

# In[2]:


df_NYPD_shooting_inc = pd.read_csv("NYPD_Shooting_Incident_Data__Historic_.csv")
col_names_lst_sorted = sorted( df_NYPD_shooting_inc.columns.tolist())

nr_of_rows = df_NYPD_shooting_inc.shape[0]
print("Number of rows in dataframe: "+str(nr_of_rows))


# In[3]:


df_NYPD_shooting_inc['X_Y_Cord'] = df_NYPD_shooting_inc['X_COORD_CD']  + ';' + df_NYPD_shooting_inc['Y_COORD_CD']


# In[4]:


df_NYPD_shooting_inc.to_csv("df_NYPD_shooting_inc.csv")


# ----------------------------------------------------

# In[ ]:




