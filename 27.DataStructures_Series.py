#!/usr/bin/env python
# coding: utf-8

# # Series

# ### A series is defined as a one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, etc..)

# ### Creating a Series with index

# In[1]:


# Creating a series with labels
import pandas as pd
series1 = pd.Series([4, 3, 2, 9], index=['a', 'b', 'c', 'd'])
print(series1)
print(series1.index)


# In[2]:


# Creating a series with labels
numbers = [4, 3, 2, 9]
labels = ['a', 'b', 'c', 'd']
series2 = pd.Series(numbers, index = labels)
print(series2)
print(series2.index)


# In[3]:


# Creating a series without labels
numbers = [4, 3, 2, 9]
labels = ['a', 'b', 'c', 'd']
series3 = pd.Series(numbers)
print(series3)
print(series3.index)


# In[4]:


# Slicing data from a series
print('Series slicing:')
print(series1[:3])
print('Index accessing:')
print(series1[[3, 1, 0]])
print('Single index:')
x = series1[0]
print(x)


# ### Creating a Series from a Dictionary

# In[5]:


# Series of non declared index
print('Series of non declared index:')
dict = {'m': 2, 'y': 2018, 'd': 'Sunday'}
series4 = pd.Series(dict)
print(series4)
# Series of declared index
print('---------------------')
print('Series of declared index:')
series5 = pd.Series(dict, index = ['y','m','d'])
print(series5)


# In[6]:


# Altering a series and using the get() method
print('\n Use the get and set methods to access '
      'a series values by index label:\n')
series6 = pd.Series(dict,index=['y','m','d'])
print(series6['y'])     # display the year
series6['y'] = 1999     # change the year value
print(series6)          # display all dictionary values
print(series6.get('y')) # get specific value by its key


# ### Creating a Series from Scalar Value

# In[7]:


series7 = pd.Series(8.0, index = [labels])
print(series7)


# ### Vectorized Operations with Series

# In[8]:


# Vectorizing Operations on a Series
series8 = pd.Series([1,2,3,4], index = [labels])
series9 = pd.Series([10,12,14,17], index = [labels])
print(series8)
print(series9)
print('Addition:')
print(series8 + series9)
print(series8 + 100)
print('Multipication:')
print(series9 * 5)

