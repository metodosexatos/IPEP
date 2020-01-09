#!/usr/bin/env python
# coding: utf-8

# 1. A ball is thrown vertically up in the air from a height $h_0$ above the ground at an initial velocity $v_0$. Its subsequent height $h$ and velocity $v$ are given by the equations below. Write a script that finds the height $h$ and velocity $v$ at a time $t$ after the ball is thrown. Then use the script to find the height and velocity after 0.5 seconds. then modify your script to find them after 2.0 seconds.

# $h=h_0+v_0t-1/2gt^2$
# 
# $v=v_0-gt$
# 
# $h_0=1.6 m$; $v_0=14.2 m/s$; $g=9.8 m/s^2$

# In[4]:


h0 = 1.6  #(m)
v0 = 14.2 #(m/s)
g = 9.8   #(m/s²)
t = 2.0   #(s)


# In[5]:


h = h0 + v0*t - (1/2)*g*t**2
v = v0 - g*t
print(h, v)


# In[6]:


print(round(h,1), round(v,1))

