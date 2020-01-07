#!/usr/bin/env python
# coding: utf-8

# Finding the roots of a quadratic equation
# In[14]:
a = 1
b = 2
c = 1

# In[15]:
x_1 = (-b+(b**2-4*a*c)**0.5)/(2*a) # It is a root of a quadratic equation
x_2 = (-b-(b**2-4*a*c)**0.5)/(2*a) # It is a root of a quadratic equation

# In[16]:
print(x_1, x_2)
