#!/usr/bin/env python
# coding: utf-8

# # Tuples

# ### A tuple is a sequence just like a list of immutable objects. The differences between tuples and lists are that the tuples cannot be altered; also, tuples use parentheses, whereas lists use square brackets.

# ## Creating Tuples

# In[1]:


# Creating and displaying Tuples

name = ('André', 'Andrey', 'Arthur')
age = (42, 9, 6)
print(name)
print(age)


# In[2]:


# Altering a Tuple for Editing

age[1] = 10


# In[ ]:


# Sorting a Tuple

mark = [(88,65), (70,90,85), (55,88,44)]
print(mark)         # original tuples
print(sorted(mark)) # direct sorting


# ## Concatenating Tuples

# In[ ]:


# Concatenating Tuples

mark1 = (70, 85, 55)
mark2 = (90, 75, 60)
combind = mark1 + mark2
print(combind)


# ## Accessing Values in Tuples

# In[ ]:


# Accessing Values in Tuples

mark1 = (70, 85, 55)
mark2 = (90, 75, 60)
print('The third mark in mark1 is', mark1[2])
print('The maximum mark in mark2 is', max(mark2))


# In[ ]:


# Deleting a Tuple

mark3 = (15, 35, 43)
print(mark3)
del mark3
print(mark3)


# In[ ]:


# Slicing Tuple Values

# Forward index:  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]
#                 70   85   55   90   75   60   15   35   43
# Backward inex: [-9] [-8] [-7] [-6] [-5] [-4] [-3] [-2] [-1]

marks = (70, 85, 55, 90, 75, 60, 15, 35, 43)
print('Forward slicing:')
print(marks[2])
print(marks[1:4])
print(marks[:3])
print(marks[6:])
print(marks[5:7])
print('Backward slicing:')
print(marks[-7])
print(marks[-8:-5])
print(marks[-3:])
print(marks[:-3])


# ## Basic Tuples Operations

# In[ ]:


#----------------------------------------------------------------------------
#  Expression              Results                          Description
#----------------------------------------------------------------------------
#  len((5, 7, 2, 6))       4                                Length
#  (1, 2,) + (4, 5)        (1, 2, 4, 5)                     Conctenation
#  ('Hi!',) * 4            ('Hi!', 'Hi!','Hi!','Hi!',)       Repetition
#  10 in (10, 2, 3)        True                             Membership
#----------------------------------------------------------------------------

