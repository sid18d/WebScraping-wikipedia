#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/sid18d/WebScraping-wikipedia/blob/main/wiki_library.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


get_ipython().system('pip install wikipedia')
# Installing required Library


# In[13]:


import wikipedia
from pprint import pprint
# Loading required Libraries


# In[27]:


wikipedia.search('Machine learning')
# Searching pages on wikipedia with title - machine learning


# In[34]:


wikipedia.page(wikipedia.search('Machine learning')[1])
 


# In[29]:


ml = wikipedia.page(wikipedia.search('Machine learning')[1])


# In[30]:


dir(ml)

# Checking the directory


# In[31]:


ml.title
# Loading Title


# In[32]:


ml.summary
#Loading the summary


# In[35]:


ml.content
# Loading all the content on the page


# In[36]:


ml.images
#Loading all the images

