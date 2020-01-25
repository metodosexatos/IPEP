#!/usr/bin/env python
# coding: utf-8

# # Data Frames [Activity 1]

# In[ ]:


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


# In[ ]:


# Structures
Computers = [40, 33, 41, 40, 39, 27, 29, 29, 14, 15, 32]
Tablets = [96, 99, 62, 97, 84, 92, 96, 96, 64, 56]
Smartphones = [98, 80, 52, 61, 77, 94, 77, 88, 77, 67]
Softwares = [234, 200, 226, 206, 290, 245, 206, 264, 236, 240, 216, 238]
Total = [468, 332, 409, 395, 474, 272, 312, 479, 423, 424, 389, 361]
Goals = [True, False, True, False, True, False, False, True, True, True, False, False]

