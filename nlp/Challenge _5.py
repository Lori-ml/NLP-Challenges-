#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#get the start time here
start_time = time.time()

opener = urllib.request.FancyURLopener({})
url = "http://google.com/"
f = opener.open(url)
content = f.read()

#calculate total time 
print("Download completed in  %s seconds" % round((time.time() - start_time) ,4))


# ----------------------------------------------------
