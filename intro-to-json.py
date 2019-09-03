#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# From http://localhost:8888/notebooks/intro-to-json.ipynb


# In[13]:


import json
import requests
import pandas as pd
import numpy as np


# In[2]:


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


# In[9]:


# Storing json as file
with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file)
print(write_file)


# In[8]:


# Writing json to native Python string object
json_string = json.dumps(data)
print(json_string)


# In[21]:


# Only works when hotspotting
response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response)


# In[24]:


todos = json.loads(response.text)
print(todos)

