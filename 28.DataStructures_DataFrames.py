#!/usr/bin/env python
# coding: utf-8

# # Data Frames

# ### 1. Creating Data Frames from a Dict of Series

# In[1]:


import pandas as pd
s_13 = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])
s_14 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
dict1 = {'one': s_13, 'two': s_14}
df = pd.DataFrame(dict1)
print(df)


# ### 2. Creating Data Frames from Dict of Lists

# In[2]:


# Creatinga Data Frame from an List
# without index
l_14 = [1, 2, 3, 4]
l_58 = [5, 6, 7, 8]
dict2 = {'one': l_14, 'two': l_58}
pd.DataFrame(dict2)


# In[3]:


# Assign index
pd.DataFrame(dict2, index = ['a', 'b', 'c', 'd'])


# In[4]:


# Set index for the Data Frame
pd.DataFrame(dict2, index = ['a', 'b', 'c', 'd'], columns = ['two','three','one'])


# ### 3. Creating Data Frames from a List of Dicts

# In[5]:


# without index
data1 = [{'A':1, 'B':2}, {'A':5, 'B':10, 'C':20}]
pd.DataFrame(data1)


# In[6]:


# with index
pd.DataFrame(data1, index = ['First', 'Second'])

