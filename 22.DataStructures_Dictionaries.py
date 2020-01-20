#!/usr/bin/env python
# coding: utf-8

# # Dictionaries

# ### Creating Dictionaries

# In[1]:


# Brands: Honda, Suzuki, Mercedes
# Prices: 40000, 50000, 85000

cars = dict()
print(cars)
cars['Honda'] = 40000
cars['Suzuki'] = 50000
cars['Mercedes'] = 85000
print(cars)


# ### Updating and Accessing Values

# In[2]:


cars = {'Honda': 40000, 'Suzuki': 50000, 'Mercedes': 85000}

# Updating
cars['Mercedes'] = 75000 # update current value
print(cars)

# Accesing specif dictionary element
print(cars['Mercedes'])


# ### Deleting Dictionary Elements

# In[3]:


# Remove all entries
print(cars)
cars.clear()
print(cars)

# Remove entry
cars = {'Honda': 40000, 'Suzuki': 50000, 'Mercedes': 85000}
del cars['Mercedes']
print(cars)

