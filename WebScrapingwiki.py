#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/sid18d/WebScraping-wikipedia/blob/main/WebScrapingwiki.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[3]:


get_ipython().system('pip install requests')
# Installing required packages


# In[4]:


get_ipython().system('pip install bs4')
# Installing required packages


# In[2]:


import requests

import bs4

import pandas

# Loading required packages


# In[5]:


webdata=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
# Getting data from webpage

webdata.text 
# Loading the data


# In[6]:


bsdata=bs4.BeautifulSoup(webdata.text,'xml')
# Converting data using BeautifulSoup


# In[7]:


bsdata
# Loading the data


# In[8]:


titles=bsdata.select('title')
# Seleting title from the Data

titles
# Loading data


# In[9]:


titles[0].getText()
# Loading specific data 


# In[10]:


titles_new=bsdata.select('h3')
# Seleting h3 from the Data

titles_new
# Loading data


# In[11]:


for i in titles_new:
  print(i.text)
# Loading all data 


# In[12]:


titles_new[4].getText()
# Loading specific data 


# In[13]:


bsdata.select('img')
# Loading all Images   


# In[ ]:




