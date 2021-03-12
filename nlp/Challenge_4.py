#!/usr/bin/env python
# coding: utf-8

# In[3]:


import wmi
import pandas as pd


# In[7]:


#### call windows management instrumentation package save results into a list and then convert to dataframe

c = wmi.WMI()

lst_processes = []
for process in c.Win32_Process ():
    
    lst_processes.append({'Process Id': process.ProcessId , 
              'Process Name': process.Name , 
              'Memory used by W3SVC':process.WorkingSetSize}) 
    
    
    
    
df_processes = pd.DataFrame(lst_processes)    
df_processes.to_csv("df_processes.csv")


# ----------------------------------------------------
