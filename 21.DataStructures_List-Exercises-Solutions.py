#!/usr/bin/env python
# coding: utf-8

# # List [Exercises::Solutions]

# In[1]:


# Datasets

year2014 = ('10/04/2014','16/04/2014','09/05/2014','24/05/2014','13/06/2014','16/06/2014','12/07/2014','10/08/2014',
            '16/08/2014','18/08/2014','09/09/2014','12/09/2014','30/09/2014','09/10/2014','10/10/2014','31/10/2014',
            '09/11/2014','11/11/2014','30/11/2014','09/12/2014','31/12/2014')

year2015 = ('09/01/2015','09/02/2015','28/02/2015','09/03/2015','09/04/2015','10/04/2015','30/04/2015','09/05/2015',
            '31/05/2015','09/06/2015','30/06/2015','12/07/2015','31/07/2015','09/08/2015','31/08/2015','09/09/2015',
            '10/09/2015','10/09/2015','30/09/2015','09/10/2015','31/10/2015','10/11/2015','13/11/2015','30/11/2015',
            '09/12/2015','10/12/2015','31/12/2015')

year2016 = ('09/01/2016','10/01/2016','31/01/2016','31/01/2016','09/02/2016','10/02/2016','29/02/2016','09/03/2016',
            '10/03/2016','10/03/2016','10/03/2016','31/03/2016','31/03/2016','05/04/2016','09/04/2016','10/04/2016',
            '12/04/2016','30/04/2016','06/05/2016','06/05/2016','09/05/2016','12/05/2016','12/05/2016','19/05/2016',
            '19/05/2016','21/05/2016','23/05/2016','31/05/2016','31/05/2016','01/06/2016','03/06/2016','03/06/2016',
            '04/06/2016','04/06/2016','04/06/2016','08/06/2016','24/06/2016','24/06/2016','03/07/2016','03/07/2016',
            '04/07/2016','09/07/2016','11/07/2016','11/07/2016','11/07/2016','12/07/2016','12/07/2016','13/07/2016',
            '15/07/2016','04/08/2016','04/08/2016','04/08/2016','09/08/2016','11/08/2016','13/08/2016','31/08/2016',
            '31/08/2016','03/09/2016','04/09/2016','04/09/2016','26/09/2016','26/09/2016','26/09/2016','30/09/2016',
            '05/10/2016','07/10/2016','07/10/2016','12/10/2016','27/10/2016','01/11/2016','02/11/2016','07/11/2016',
            '12/11/2016','16/11/2016','16/11/2016','05/12/2016','07/12/2016','09/12/2016','12/12/2016','15/12/2016')

year2017 = ('01/01/2017','02/01/2017','05/01/2017','07/01/2017','07/01/2017','08/01/2017','15/01/2017','04/02/2017',
            '09/02/2017','09/02/2017','14/02/2017','01/03/2017','16/03/2017','06/05/2017','13/05/2017','05/06/2017')

year2018 = ('24/02/2018','26/03/2018','25/04/2018','15/12/2018')

year2019 = ('15/01/2019','15/01/2019','24/01/2019','25/01/2019','25/01/2019','25/01/2019','26/01/2019','26/01/2019',
            '28/01/2019','28/01/2019','29/01/2019','31/01/2019','05/02/2019','13/02/2019','15/02/2019','20/02/2019',
            '28/02/2019','15/03/2019','20/03/2019','26/03/2019','29/03/2019','02/04/2019','02/04/2019','05/04/2019',
            '05/04/2019','05/04/2019','09/04/2019','10/04/2019','11/04/2019','13/04/2019','13/04/2019','22/04/2019',
            '28/04/2019','29/04/2019','30/04/2019','02/05/2019','08/05/2019','09/05/2019','10/05/2019','10/05/2019',
            '11/05/2019','15/05/2019','17/05/2019','20/05/2019','22/05/2019','28/05/2019','30/05/2019','30/05/2019',
            '30/05/2019','31/05/2019','05/06/2019','05/06/2019','07/06/2019','08/06/2019','12/06/2019','13/06/2019',
            '14/06/2019','15/06/2019','16/06/2019','18/06/2019','30/06/2019','05/07/2019','17/07/2019','30/07/2019',
            '31/07/2019','05/08/2019','14/08/2019','15/08/2019','16/08/2019','30/08/2019','05/09/2019','12/09/2019',
            '15/09/2019','16/09/2019','16/09/2019','20/09/2019','26/09/2019','30/09/2019','30/09/2019','05/10/2019',
            '20/10/2019','30/10/2019','15/11/2019','30/11/2019','06/12/2019','16/12/2019','31/12/2019')


# ### 1. Print structures type

# In[2]:


# Print structures type
print('2014:', type(year2014))
print('2015:', type(year2015))
print('2016:', type(year2016))
print('2017:', type(year2017))
print('2018:', type(year2018))
print('2019:', type(year2019))


# ### 2. Convert the structures to list ("rename: y2011")

# In[3]:


# Convert the structures to list ("rename: y2011")

y2014 = list(year2014)
y2015 = list(year2015)
y2016 = list(year2016)
y2017 = list(year2017)
y2018 = list(year2018)
y2019 = list(year2019)


# ### 3. check new and old structures

# In[4]:


# Ceck new and old structures

print('year2014:', type(year2014))
print('y2014:', type(y2014))
print('year2015:', type(year2015))
print('y2015:', type(y2015))
print('year2016:', type(year2016))
print('y2016:', type(y2016))
print('year2017:', type(year2017))
print('y2017:', type(y2017))
print('year2018:', type(year2018))
print('y2018:', type(y2018))
print('year2019:', type(year2019))
print('y2019:', type(y2019))


# ### 4. Create single document (call "years")

# In[7]:


# Create single document (call "years")

# Example 1:
years = y2014 + y2015 + y2016 + y2017 + y2018 + y2019
print(type)
print(years)

# Example 2:
years2 = []
print(years2)
years2.extend(y2014)
years2.extend(y2015)
years2.extend(y2016)
years2.extend(y2017)
years2.extend(y2018)
years2.extend(y2019)
print(years2)


# ### 5. Count number of occurrences of 2017 in years

# In[8]:


# 2017 number of occurrences:

string = str(years)
string2017 = '2017'
count2017 = string.count(string2017)
print('The count is:', count2017)


# ### 6. Calculate the relative frequency for 2017

# In[11]:


# 2017 relative frequency:

print(round(count2017/len(years),4))            # decimal
print(round(count2017/len(years)*100,2), '%')   # percentage


# ### 7. Calculate the relative frequency for months (%)

# In[17]:


# Relative frequency for months:

# define months strings
jan = "/01/"
feb = "/02/"
mar = "/03/"
apr = "/04/"
may = "/05/"
jun = "/06/"
jul = "/07/"
aug = "/08/"
sep = "/09/"
ocb = "/10/"
nov = "/11/"
dec = "/12/"

count_jan = string.count(jan)
count_feb = string.count(feb)
count_mar = string.count(mar)
count_apr = string.count(apr)
count_may = string.count(may)
count_jun = string.count(jun)
count_jul = string.count(jul)
count_aug = string.count(aug)
count_sep = string.count(sep)
count_ocb = string.count(ocb)
count_nov = string.count(nov)
count_dec = string.count(dec)

print('January:  ', round(count_jan/len(years)*100,2),"%")
print('February: ', round(count_feb/len(years)*100,2),"%")
print('March:    ', round(count_mar/len(years)*100,2),"%")
print('April:    ', round(count_apr/len(years)*100,2),"%")
print('May:      ', round(count_jan/len(years)*100,2),"%")
print('June:     ', round(count_jan/len(years)*100,2),"%")
print('July:     ', round(count_jan/len(years)*100,2),"%")
print('August:   ', round(count_jan/len(years)*100,2),"%")
print('September:', round(count_jan/len(years)*100,2),"%")
print('October:  ', round(count_jan/len(years)*100,2),"%")
print('November: ', round(count_jan/len(years)*100,2),"%")
print('December: ', round(count_jan/len(years)*100,2),"%")


# ### 8. Check if months relative frequency (sum) is 100%

# In[18]:


# Check if months relative frequency (sum) is 100%

January = count_jan/len(years)*100
February = count_feb/len(years)*100
March = count_mar/len(years)*100
April = count_apr/len(years)*100
May = count_may/len(years)*100
June = count_jun/len(years)*100
July = count_jul/len(years)*100
August = count_aug/len(years)*100
September = count_sep/len(years)*100
October = count_ocb/len(years)*100
November = count_nov/len(years)*100
December = count_dec/len(years)*100

print(round(January+February+March+April+May+June+July+August+September+October+November+December,2))


# ### 9. Calculate the relative frequency for days(%)

# In[19]:


# Relative frequency for days(%)

# define days strings
d01, d02, d03, d04, d05, d06, d07, d08, d09, d10 = "01/", "02/", "03/", "04/", "05/", "06/", "07/", "08/", "09/", "10/"
d11, d12, d13, d14, d15, d16, d17, d18, d19, d20 = "11/", "12/", "13/", "14/", "15/", "16/", "17/", "18/", "19/", "20/"
d21, d22, d23, d24, d25, d26, d27, d28, d29, d30 = "21/", "22/", "23/", "24/", "25/", "26/", "27/", "28/", "29/", "30/"
d31 = "31/"
print(d01, d02, d03, d04, d05, d06, d07, d08, d09, d10, 
      d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, 
      d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, 
      d31)

# Count days
count_d01 = string.count(d01) - string.count(jan)
count_d02 = string.count(d02) - string.count(feb)
count_d03 = string.count(d03) - string.count(mar)
count_d04 = string.count(d04) - string.count(apr)
count_d05 = string.count(d05) - string.count(may)
count_d06 = string.count(d06) - string.count(jun)
count_d07 = string.count(d07) - string.count(jul)
count_d08 = string.count(d08) - string.count(aug)
count_d09 = string.count(d09) - string.count(sep)
count_d10 = string.count(d10) - string.count(ocb)
count_d11 = string.count(d11) - string.count(nov)
count_d12 = string.count(d12) - string.count(dec)
count_d13 = string.count(d13)
count_d14 = string.count(d14)
count_d15 = string.count(d15)
count_d16 = string.count(d16)
count_d17 = string.count(d17)
count_d18 = string.count(d18)
count_d19 = string.count(d19)
count_d20 = string.count(d20)
count_d21 = string.count(d21)
count_d22 = string.count(d22)
count_d23 = string.count(d23)
count_d24 = string.count(d24)
count_d25 = string.count(d25)
count_d26 = string.count(d26)
count_d27 = string.count(d27)
count_d28 = string.count(d28)
count_d29 = string.count(d29)
count_d30 = string.count(d30)
count_d31 = string.count(d31)

print(count_d01, count_d02, count_d03, count_d04, count_d05, count_d06 ,count_d07, count_d08, count_d09, count_d10,
      count_d11, count_d12, count_d13, count_d14, count_d15, count_d16, count_d17 ,count_d18, count_d19 ,count_d20,
      count_d21, count_d22, count_d23, count_d24, count_d25, count_d26, count_d27 ,count_d28, count_d29 ,count_d30,
      count_d31)

print('D01:', round(count_d01/len(years)*100,2),"%")
print('D02:', round(count_d02/len(years)*100,2),"%")
print('D03:', round(count_d03/len(years)*100,2),"%")
print('D04:', round(count_d04/len(years)*100,2),"%")
print('D05:', round(count_d05/len(years)*100,2),"%")
print('D06:', round(count_d06/len(years)*100,2),"%")
print('D07:', round(count_d07/len(years)*100,2),"%")
print('D08:', round(count_d08/len(years)*100,2),"%")
print('D09:', round(count_d09/len(years)*100,2),"%")
print('D10:', round(count_d10/len(years)*100,2),"%")
print('D11:', round(count_d11/len(years)*100,2),"%")
print('D12:', round(count_d12/len(years)*100,2),"%")
print('D13:', round(count_d13/len(years)*100,2),"%")
print('D14:', round(count_d14/len(years)*100,2),"%")
print('D15:', round(count_d15/len(years)*100,2),"%")
print('D16:', round(count_d16/len(years)*100,2),"%")
print('D17:', round(count_d17/len(years)*100,2),"%")
print('D18:', round(count_d18/len(years)*100,2),"%")
print('D19:', round(count_d19/len(years)*100,2),"%")
print('D20:', round(count_d20/len(years)*100,2),"%")
print('D21:', round(count_d21/len(years)*100,2),"%")
print('D22:', round(count_d22/len(years)*100,2),"%")
print('D23:', round(count_d23/len(years)*100,2),"%")
print('D24:', round(count_d24/len(years)*100,2),"%")
print('D25:', round(count_d25/len(years)*100,2),"%")
print('D26:', round(count_d26/len(years)*100,2),"%")
print('D27:', round(count_d27/len(years)*100,2),"%")
print('D28:', round(count_d28/len(years)*100,2),"%")
print('D29:', round(count_d29/len(years)*100,2),"%")
print('D30:', round(count_d30/len(years)*100,2),"%")
print('D31:', round(count_d31/len(years)*100,2),"%")


# ### 10. Check if days relative frequency (sum) is 100%

# In[21]:


# Check if days relative frequency (sum) is 100%

D01 = count_d01/len(years)*100
D02 = count_d02/len(years)*100
D03 = count_d03/len(years)*100
D04 = count_d04/len(years)*100
D05 = count_d05/len(years)*100
D06 = count_d06/len(years)*100
D07 = count_d07/len(years)*100
D08 = count_d08/len(years)*100
D09 = count_d09/len(years)*100
D10 = count_d10/len(years)*100
D11 = count_d11/len(years)*100
D12 = count_d12/len(years)*100
D13 = count_d13/len(years)*100
D14 = count_d14/len(years)*100
D15 = count_d15/len(years)*100
D16 = count_d16/len(years)*100
D17 = count_d17/len(years)*100
D18 = count_d18/len(years)*100
D19 = count_d19/len(years)*100
D20 = count_d20/len(years)*100
D21 = count_d21/len(years)*100
D22 = count_d22/len(years)*100
D23 = count_d23/len(years)*100
D24 = count_d24/len(years)*100
D25 = count_d25/len(years)*100
D26 = count_d26/len(years)*100
D27 = count_d27/len(years)*100
D28 = count_d28/len(years)*100
D29 = count_d29/len(years)*100
D30 = count_d30/len(years)*100
D31 = count_d31/len(years)*100

print(round(D01+D02+D03+D04+D05+D06+D07+D08+D09+D10+
            D11+D12+D13+D14+D15+D16+D17+D18+D19+D20+
            D21+D22+D23+D24+D25+D26+D27+D28+D29+D30+
            D31,2))


# ### 11. Sorting #10 (days frequency)

# In[24]:


# Sorting:

days_freq = [D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, 
             D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, 
             D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, 
             D31]

days_freq.sort()
print(days_freq)

days_freq_list_round = [float(round(n,3)) for n in days_freq]
print(days_freq_list_round)


# ### 12. Most frequency day

# In[28]:


# Most frequency day

count_days = [count_d01, count_d02, count_d03, count_d04, count_d05, count_d06 ,count_d07, count_d08, count_d09, count_d10,
              count_d11, count_d12, count_d13, count_d14, count_d15, count_d16, count_d17 ,count_d18, count_d19 ,count_d20,
              count_d21, count_d22, count_d23, count_d24, count_d25, count_d26, count_d27 ,count_d28, count_d29 ,count_d30,
              count_d31]

string_count_days = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06','d07', 'd08', 'd09', 'd10',
                     'd11', 'd12', 'd13', 'd14', 'd15', 'd16','d17', 'd18', 'd19', 'd20',
                     'd21', 'd22', 'd23', 'd24', 'd25', 'd26','d27', 'd28', 'd29', 'd30',
                     'd31']

print('occurrences:', count_days)
count_max = max(count_days)
print('Maximum occurrence:', count_max)
max_day_index = count_days.index(count_max)
print('Maximum occurrence index:', max_day_index)
print('Most occurrence day:', string_count_days[max_day_index])

