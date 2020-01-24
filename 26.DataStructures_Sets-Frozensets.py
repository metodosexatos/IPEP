#!/usr/bin/env python
# coding: utf-8

# # Sets and Frozensets

# <ol>
#     <li> The set data type is the implementation of a mathematical set. </li>
#     <li> It is an unordered collection of objets. </li>
#     <li> Sets do not permity duplicity in the occurrence of an element. </li>
#     <li> A set is defined using the set() function. </li>
# </ol>

# ### 1. Creating sets and frozensets

# In[1]:


# Set structure
math_set = set([1, 2, 4, 2, 1, 4, 3, 3, 4])
# Frozenet structure
math_fset = frozenset([1, 2, 4, 2, 1])

# Type and elements
print('math_set type: ', type(math_set))
print('math_fset type:', type(math_fset))
print('math_set elements: ', math_set)
print('math_fset elements:', math_fset)


# ### 2. Basic Operations (Sets and Frozensets)

# In[2]:


#---------------------------------------------------------
#  Operation            Result
#---------------------------------------------------------
#  len(s)               cardinality of set s
#  x in s               test x for membership in s
#  x not in s           test x for non-membership in s
#  s.copy()             new set with a shallow copy of s
#---------------------------------------------------------


# #### 2.1. Basic

# In[3]:


# Length
print('math_set: ', len(math_set))
print('math_fset:', len(math_fset))


# In[4]:


# Membership
print('3 is in math_set:   ', 3 in math_set)
print("3 isn't in math_set:", 3 not in math_set)


# In[5]:


# Copy
math_set1 = math_set.copy()
print(math_set1)


# #### 2.2 Set Theory

# In[6]:


#-------------------------------------------------------------------------------------------------------------
#  Operation                         Equivalent     Result
#-------------------------------------------------------------------------------------------------------------
#  s.issubset(t)                     s <= t         test whether every element in s is in t   
#  s.issuperset(t)                   s >= t         test whether every element in t is in s
#  s.union(t)                        s | t          new set with elements from both s and t
#  s.intersection(t)                 s & t          new set with elements common to s and t       
#  s.difference(t)                   s - t          new set with elements in s but not in t           
#  s.symmetric_difference(t)         s ^ t          new set with elements in either s or t but not both
#-------------------------------------------------------------------------------------------------------------


# In[7]:


# Sets
math_10th = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
math_odd = set([1, 3, 5, 7, 9])
math_even = set([0, 2, 4, 6, 8])
math_prime = set([2, 3, 5, 7])
math_random = set([0, 7, 8, 2])


# In[8]:


# Subsets
print('Prime is subset 10th?',math_prime.issubset(math_10th))
print('Prime is superset 10th?',math_prime.issuperset(math_10th))


# In[9]:


# Union
math_union = math_odd.union(math_random)
print('Math Union:',math_union)


# In[10]:


# Intersection
math_inter = math_odd.intersection(math_random)
print('Math Intersection:',math_inter)


# In[11]:


# Difference
# Odd: 1, 3, 5, 7, 9
# Random: 0, 7, 8, 2
math_dif = math_odd.difference(math_random)
print('Odd - Random:', math_dif)
math_dif1 = math_random.difference(math_odd)
print('Random - Odd:', math_dif1)


# In[12]:


# Symmetric Difference


# In[13]:


math_sdif = math_odd.symmetric_difference(math_random)
print('Odd - Random:', math_sdif)
math_sdif1 = math_random.symmetric_difference(math_odd)
print('Random - Odd:', math_sdif1)


# ### 3. Basic Operation (not apply immutable instances of frozenset)

# In[14]:


#-------------------------------------------------------------------------------------------------------------
#  Operation                         Equivalent    Result
#-------------------------------------------------------------------------------------------------------------
#  s.update(t)                       s |= t        update set s, adding elements from t
#  s.intersection_update(t)          s &= t        update set s, keeping only elements found in both s and t
#  s.difference_update(t)            s -= t        update set s, removing elements found in t
#  s.symmetric_difference_update(t)  s ^= t        update set s, keeping only elements found in either s or t but not in both
#  s.add(x)                                        add element x to set s
#  s.remove(x)                                     remove x from set s; raises KeyError if not present
#  s.discard(x)                                    removes x from set s if present
#  s.pop()                                         remove and return an arbitrary element from s; raises KeyError if empty
#  s.clear()                                       remove all elements from set s
#-------------------------------------------------------------------------------------------------------------


# ### 4. Number Decomposition Algorithm

# In[15]:


# Decomposition
number = set('12345')
print(number)


# In[16]:


# Sum numerals in 12345
number_list = sorted(list(number))
print(number_list)
print('Number as string: ', number_list[0] + number_list[1] + number_list[2])
print('Number as integer:', int(number_list[0]) + int(number_list[1]) + int(number_list[2]))

