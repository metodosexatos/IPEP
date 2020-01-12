#!/usr/bin/env python
# coding: utf-8

# # Complex Numbers

# ## Syntax

# In[1]:


# complex([real[, imag]])


# ## Creating a complex number

# In[2]:


c = 2 + 3j
print(type(c))


# In[3]:


c1 = complex(2, 3)
print(type(c1))


# In[4]:


print(c1)


# ## Atributes and Functions

# In[5]:


# Conjugate: 4 + 9j 
# real:      4
# imaginary: 9j


# In[6]:


# Complex Number
cn = (4+9j)


# In[7]:


# Real part of complex number
print(cn.real)


# In[8]:


# Imaginary part of complex number
print(cn.imag)


# In[9]:


# Conjugate of complex number
print(cn.conjugate())


# ## Mathematical calculations on complex numbers

# In[10]:


# Complex numbers:
z1 = (2 + 4j)
z2 = (1 + 2j)


# In[11]:


# Addition
print(z1 + z2)


# In[12]:


# Subtraction
print((z1-z2),(z2-z1))


# In[13]:


# Multiplication
print(z1*z2)


# In[14]:


# Division
print(z1/z2)


# ### Complex numbers don't support comparison operator like <, >, <=, =>

# In[15]:


z1 <= z2


# In[16]:


z1 == z2


# In[17]:


z1 != z2

