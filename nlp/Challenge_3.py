#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt    


# #####  read the csv for the red wines

# In[7]:


df_red_wine = pd.read_csv("winequality-red.csv" , header=None ) 

df_red_wine = pd.DataFrame(df_red_wine[0].str.split(';',12).tolist() )
df_red_wine_col_nm = df_red_wine.iloc[0,:].str.replace('"', '').tolist()
Temp_col_nm = df_red_wine.columns
Correct_col_nm = df_red_wine_col_nm

df_red_wine.rename(columns= dict(zip(Temp_col_nm,Correct_col_nm )) , inplace=True)
df_red_wine = df_red_wine.iloc[1:]


# #####  read the csv for the white wines

# In[4]:


df_white_wine = pd.read_csv("winequality-white.csv" , header=None ) 

df_white_wine = pd.DataFrame(df_white_wine[0].str.split(';',12).tolist() )

df_white_wine_col_nm = df_white_wine.iloc[0,:].str.replace('"', '').tolist()
Temp_col_nm_1 = df_white_wine.columns
Correct_col_nm_1 = df_red_wine_col_nm

df_white_wine.rename(columns= dict(zip(Temp_col_nm_1,Correct_col_nm_1 )) , inplace=True)
df_white_wine = df_white_wine.iloc[1:]


# #### prepare the dataset for test and training

# In[5]:


df_wine_final = pd.concat([df_red_wine,df_white_wine], axis=0)
df_X_wine = df_wine_final[df_wine_final.columns.tolist()[:-1]]
df_Y_wine = df_wine_final[df_wine_final.columns.tolist()[-1]]


# #### split data into train and test sets , apply random forest and make prediction

# In[8]:


df_X_train_wine, df_X_test_wine, df_y_train_wine, df_y_test_wine  = train_test_split(df_X_wine, df_Y_wine, test_size=0.25)   


# In[9]:


clf=RandomForestClassifier(n_estimators=100)
clf.fit(df_X_train_wine,df_y_train_wine)


# In[10]:


y_pred_wine = clf.predict(df_X_test_wine)


# #### calculate mean squared error and mean absolute error

# In[12]:


mean_sqrd_err = metrics.mean_squared_error(df_y_test_wine, y_pred_wine)
mean_abs_err = metrics.mean_absolute_error(df_y_test_wine, y_pred_wine)


# #### save the results into metrics.txt

# In[13]:


with open('metrics.txt', 'a') as f:
    print("Challenge 3 / Mean squared error is: \n" + str(round(mean_sqrd_err , 4)) , file=f)
    print('Challenge 3 / Mean absolute error is: \n' + str(round(mean_abs_err , 4)) ,  file=f)


# ----------------------------------------------------
