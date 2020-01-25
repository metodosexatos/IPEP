#!/usr/bin/env python
# coding: utf-8

# # Data Frames [Activity 1::Solution]

# In[1]:


#******************************* Dataset ********************************#
# ---------------------------------------------------------------------  #
#              Computers  Tablets  Smartphones  Softwares  Total  Goals  #
# ---------------------------------------------------------------------  #
# January         40        96         98           234     468   True   #
# February        33        99         --           200     332   False  #
# March           41        62         80           226     409   True   #
# April           40        97         52           206     395   False  #
# May             39        84         61           290     474   True   #
# June            27        --         --           245     272   False  #
# July            29        --         77           206     312   False  #
# August          29        92         94           264     479   True   #
# September       14        96         77           236     423   True   #
# October         15        96         88           240     439   True   #
# November        32        64         77           216     389   False  #
# December        --        56         67           238     361   False  #
# ---------------------------------------------------------------------  #
#************************************************************************#


# In[2]:


# Structures
Computers = [40, 33, 41, 40, 39, 27, 29, 29, 14, 15, 32]
Tablets = [96, 99, 62, 97, 84, 92, 96, 96, 64, 56]
Smartphones = [98, 80, 52, 61, 77, 94, 77, 88, 77, 67]
Softwares = [234, 200, 226, 206, 290, 245, 206, 264, 236, 240, 216, 238]
Total = [468, 332, 409, 395, 474, 272, 312, 479, 423, 424, 389, 361]
Goals = [True, False, True, False, True, False, False, True, True, True, False, False]


# In[3]:


# Structures copies
com = Computers.copy()
tab = Tablets.copy()
sma = Smartphones.copy()
sof = Softwares.copy()
tot = Total.copy()
goa = Goals.copy()


# In[4]:


# Index
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
m_com = ['January','February','March','April','May','June','July','August','September','October','November']
m_tab = ['January','February','March','April','May','August','September','October','November','December']
m_sma = ['January','March','April','May','July','August','September','October','November','December']


# In[5]:


# Checking structures and indexes lenghts
print(len(com) == len(m_com))
print(len(tab) == len(m_tab))
print(len(sma) == len(m_sma))
print(len(sof) == len(months))
print(len(tot) == len(months))
print(len(goa) == len(months))


# In[6]:


# Creating series with index
import pandas as pd
com_s = pd.Series(com, index = m_com)
tab_s = pd.Series(tab, index = m_tab)
sma_s = pd.Series(sma, index = m_sma)
sof_s = pd.Series(sof, index = months)
tot_s = pd.Series(tot, index = months)
goa_s = pd.Series(goa, index = months)


# In[7]:


# Creating a Dictionary
dict = {'Computers': com_s, 'Tablets':tab_s, 'Smartphones': sma_s, 'Softwares': sof_s, 'Total': tot_s, 'Goals': goa_s}


# In[8]:


# Data Frame (without index)
pd.DataFrame(dict)


# In[9]:


# Data Frame (with index)
pd.DataFrame(dict, index = months)

