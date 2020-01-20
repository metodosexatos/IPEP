#!/usr/bin/env python
# coding: utf-8

# # Built-in Dictionary Methods{Solutions}

# In[1]:


# Structures
food = {'Breads':['Baguette','Croissant','Donuts','Loaf','Pretzel','White Bread'],
        'Desserts':['Cake','Cheescake','Chocolate','Gelatine','Pudding','Tiramisu'],
        'Fruits':['Apple','Banana','Orange','Papaya', 'Tangerine','Tomato','Watermelon'],
        'Meats':['Beef','Chicken','Fish','Pork'],
        'Vegetables':['Asparagus','Bean','Broccoli','Carrot','Onion']}

soup = ['Tortilla','Cream','Noodle','Pork','Bean','Curry','Tomato']

drink = ['Beer','Wine','Coffee','Milk','Tea','Juice']
#********************************************************************************************#
# Solution:
# pantry = {'Breads':['Baguette', 'Croissant', 'Donuts', 'Loaf', 'Pretzel', 'White Bread'],
#           'Desserts':['Cake', 'Cheescake' 'Chocolate', 'Gelatine', 'Pudding', 'Tiramisu'],
#          'Drinks':['Beer', 'Coffee', 'Juice', 'Milk', 'Tea', 'Wine'],
#          'Fruits':['Apple', 'Banana', 'Orange', 'Papaya', 'Tangerine', 'Watermelon'],
#          'Meats':['Beef', 'Chicken', 'Fish','Pork'],
#          'Soups':['Bean', 'Cream', 'Curry', 'Noodle', 'Pork', 'Tortilla', 'Tomato'], 
#          'Vegetables':['Asparagus', 'Bean','Broccoli', 'Carrot','Onion', 'Tomato']}


# ### 1. Check structures

# In[2]:


print('Food: ', type(food))
print('Soup: ', type(soup))
print('Drink:', type(drink))


# ### 2. Copy structures (call: 'food_copy', 'soup_copy', 'drink_copy')

# In[3]:


food_copy = food.copy()
soup_copy = soup.copy()
drink_copy= drink.copy()


# ### 3. Calculate copies length (food copy step 1: lenght for single key; step 2: sum step 1). Variable names: 'breads_length'

# In[4]:


# soup_copy length
print('Soup length:  ', len(soup_copy))
# drink_copy length
print('Drink length: ', len(drink_copy))
# food_copy length:
breads_length = len(food_copy['Breads'])
desserts_length = len(food_copy['Desserts'])
fruits_length = len(food_copy['Fruits'])
meats_length = len(food_copy['Meats'])
vegetables_length = len(food_copy['Vegetables'])
print('Breads:       ',breads_length)
print('Desserts:     ',desserts_length)
print('Fruits:       ',fruits_length)
print('Meats:        ',meats_length)
print('Vegetables:   ',vegetables_length)
print('Food keys:    ',len(food_copy))
print('Food element:',breads_length + desserts_length + fruits_length + meats_length + vegetables_length)


# ### 4. For 'food_copy', update the 'Tomato' in the right place ('Vegetables')

# #### 4.1 Create a "fruit list no tomato" (call: fruits_no_tomato)

# In[5]:


fruits_no_tomato = food_copy['Fruits'].copy()
print(fruits_no_tomato)
fruits_no_tomato.remove('Tomato')
print(fruits_no_tomato)
print(food_copy['Fruits'])


# #### 4.2 Create a " vegetables list with tomato" (call: vegetables_with_tomato)

# In[6]:


vegetables_with_tomato = food_copy['Vegetables'].copy()
print(vegetables_with_tomato)
print(food_copy['Vegetables'])
vegetables_with_tomato.append(food_copy['Fruits'][food_copy['Fruits'].index('Tomato')])
print(vegetables_with_tomato)
print(food_copy['Vegetables'])


# #### 4.3 Delete 'Fruits' in "food_copy"

# In[7]:


print(food_copy.keys())
del food_copy['Fruits']
print(food_copy.keys())


# #### 4.4 Delete 'Vegetables' in "food_copy"

# In[8]:


print(food_copy.keys())
del food_copy['Vegetables']
print(food_copy.keys())


# #### 4.5 Update "food_copy" with "fruits_no_tomato" as 'Fruits' and "vegetables_with_tomato" as 'Vegetables'

# In[9]:


food_copy['Fruits'] = fruits_no_tomato
food_copy['Vegetables'] = vegetables_with_tomato
print(food_copy.keys())


# ### 5. Add "soup_copy" as 'Soups' and "drink_copy" as 'Drinks' in "food_copy"

# #### 5.1 Sort "soup_copy" and "drink_copy"

# In[10]:


print(soup_copy)
soup_copy.sort()
print(soup_copy)
print(drink_copy)
drink_copy.sort()
print(drink_copy)


# #### 5.2 Add sort "soup_copy" and "drink_copy"

# In[11]:


print(food_copy.keys())
food_copy['Soups'] = soup_copy
food_copy['Drinks'] = drink_copy
print(food_copy.keys())


# ### 6. Create final document with sorted keys (call: pantry)

# In[14]:


y = food_copy
l = list(y.items())
l.sort()
print('Ascending order is:', l)
pantry = dict(l)
print(type(pantry))
print('Pantry dictionary:', pantry)


# ### 7. Check the results: type(); len(); elements; keys

# In[15]:


print('pantry:   ',type(pantry))
print('food_copy:',type(food_copy))
print('---------------------------')
print('pantry:   ',len(pantry))
print('food_copy:',len(food_copy))
print('---------------------------')
print('Breads:    ',pantry['Breads'] == food_copy['Breads'])
print('Desserts:  ',pantry['Desserts'] == food_copy['Desserts'])
print('Drinks:    ',pantry['Drinks'] == food_copy['Drinks'])
print('Fruits:    ',pantry['Fruits'] == food_copy['Fruits'])
print('Meats:     ',pantry['Meats'] == food_copy['Meats'])
print('Soups:     ',pantry['Soups'] == food_copy['Soups'])
print('Vegetables:',pantry['Vegetables'] == food_copy['Vegetables'])
print('---------------------------')
print('pantry keys:   ', pantry.keys())
print('food_copy keys:', food_copy.keys())


# ### 8. Check the original food structure

# In[16]:


print('food - structure:', type(food))
print('food - length:', len(food))
print('food - keys:', food.keys())


# In[ ]:




