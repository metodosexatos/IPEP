#!/usr/bin/env python
# coding: utf-8

# # Logical

# In[ ]:


# This type of data stores boolean values "True" or "False" and can be operated by boolean operators such as "AND" and "OR".

#**********************************************#
# Operator  Python Function  Symbolic Function #
#                                              #
#  And        and()           &                #
#  Or         or()            |                #
#  NOT        not()                            #
#**********************************************#


# In[1]:


True


# In[2]:


False


# In[3]:


not True


# In[4]:


True and False


# In[5]:


True and True


# In[6]:


False and False


# In[7]:


True & False


# In[8]:


True or False


# In[9]:


True|False


# ### Complex logical statements

# In[10]:


(True and True) or (not False)


# In[11]:


(True & True) | (not False)


# In[12]:


(True or True) or (True and False)


# In[13]:


(True | True) | (True and False)


# In[14]:


not((True or True) or (True and False))


# ### Examples:

# In[15]:


2 > 3          # greater than operator


# In[16]:


2 == 2         # equality operator


# In[17]:


2 == 2.0       # equality operator compares the value and not the type


# In[18]:


2 == 3         # equality operator


# In[19]:


(2+3) > (2-3)  # complex expression evaluated logically


# In[20]:


a = 4


# In[21]:


print(a)


# In[22]:


a == 4


# In[23]:


b == 4


# In[24]:


"b" == 4

