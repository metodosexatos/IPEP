#!/usr/bin/env python
# coding: utf-8

# # Lists

# 1. A list is a sequence of values of any data type.
# 2. A list can be created by storing a sequence of different types of values separated by commas.
# 3. A Python list is enclosed between a square brackets([]), and elementes are stored in the index based on a starting index of 0.

# In[1]:


[1, 'Métodos Exatos', 'a', True, (2+3j), 4.3]


# In[2]:


type([1, 'Métodos Exatos', 'a', True, (2+3j), 4.3])


# ### Creating Lists

# In[3]:


numbers = [1, 24, 76]
print(numbers)
type(numbers)


# In[4]:


colors = ['red', 'yellow', 'blue']
print(colors)
print(type(colors))


# In[5]:


mix = ['black', 15, 6]
print(mix)


# In[6]:


nested1 = [1, [5, 6], 7]
print(nested1)


# In[7]:


nested2 = [numbers, colors]
print(nested2)


# In[8]:


List1 = [1, 24, 76,'red', 'yellow', 'blue']


# In[9]:


print([])


# In[10]:


type([])


# ### Accessing values in lists

# In[11]:


# Lists:
list1 = ['Argentina', 'basketball', 2019, 2020]
list2 = [10, 20, 30, [40, 50]]
list3 = ['a', 15+7j, 330, 'Omar']
list4 = [23, 'Python', 2+3j, 34.5, 'abc']


# In[12]:


print(list1[0])
print(list2[1:])
print(list3[-3:-1])
print(list3[-3:])
print(list2[1:3])
print(list2[3][0])


# ### List lenght

# In[13]:


list5 = ['Brazil', 'basketball', 2019, 2020, 10, 20, 30, [40, 50], 23, ['Python', 2+3j, 34.5,], 'abc', 4*1/2+3**2]


# In[14]:


len(list5)


# In[15]:


half = len(list5)/2
print(half)
type(half)


# In[16]:


print(list5[:half])


# In[17]:


half = int(half)
print(half)
type(half)


# In[18]:


print(list5[:half])

