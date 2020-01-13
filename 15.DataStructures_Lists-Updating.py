#!/usr/bin/env python
# coding: utf-8

# # Adding, updating and deleting lists elements

# In[1]:


courses = ['Eng', 'Mkt', 'Mat', 'Eco']
students = ['Ali', 'Julia', 'Salim', 'Ana', 'Mary']
Eng_marks = [65, 85, 92]


# ### 1. Adding

# In[2]:


Eng_marks.append(50)
print(Eng_marks)


# In[3]:


Eng_marks.append(77)
print(Eng_marks)


# In[4]:


list1 = [89, 65, 100]
Eng_marks.extend(list1)
print(Eng_marks)


# ### 2. Updating

# In[6]:


Eng_marks[0] = 70
Eng_marks[1] = 45
print(Eng_marks)


# ### 3. Deleting

# In[7]:


del Eng_marks[7]
print(Eng_marks)


# In[8]:


Eng_marks.remove (50)
print(Eng_marks)


# In[9]:


Eng_marks.pop (2)
print(Eng_marks)

