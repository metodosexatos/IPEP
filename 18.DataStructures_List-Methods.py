#!/usr/bin/env python
# coding: utf-8

# # List Methods

# In[1]:


# append(x)
# Adds an item to the end of the list. It's equivalent to var[len(var):] = [x]

var = ['car','bicycle']
print(var)
var.append('train')
print(var)


# In[2]:


# extend(iterable)
# Extends the lis by appendingall the items from iterable. This allows you to join two lists together.
# ... It's equivalent to var[len(var):] = iterable

var = ['car','bicycle']
print(var)
var.extend(['airplane', 'motorcicle'])
print(var)


# In[3]:


# insert(i, x)
# Inserts an item at a given position. The first argument is the index of the element before which to insert.

var = ['car','bicycle']
print(var)
var.insert(0,'skate')
print(var)
var.insert(2,'boat')
print(var)


# In[4]:


# remove(x)
# Removes the first item from the list that has a value of x. Returns an error if there is no such item.

var = ['car','bicycle', 'train', 'bicycle']
print(var)
var.remove('bicycle')
print(var)


# In[5]:


# pop([i])
# Removes the item at the given position in the list, and returns it.If no index is specified, pop() removes and returns the
# ... last item in the list.

# Example 1: No index specified:
var = ['car','bicycle', 'train']
print(var)
var.pop()
print(var)

# Example 2: Index specified
var = ['car','bicycle', 'train']
print(var)
var.pop(1)
print(var)


# In[6]:


# clear()
# Removes all items from the list. Equivalent to del a[:].

var = ['car','bicycle', 'train']
print(var)
var.clear()
print(var)


# In[7]:


# index(x[, start[, end]])
# Returns the position of the first list item that has a value of x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a
# ... particular subsequenc of list. The returned index is computed relatie to the beginning of the full sequence rather
# ... than the start argument.

var = ['car','bicycle', 'train', 'skate', 'car', 'bicycle', 'airplane', 'boat', 'car']
print(var.index('car'))
print(var.index('car', 1))
print(var.index('car', 5))


# In[8]:


# count(x)
# Returns the number of times x appears in the list.

var = ['car','bicycle','train','car']
print(var.count('car'))
print(var.count('bicycle'))


# In[9]:


# sort(key=None, reverse=False)
# Sorts the items of the list in place. The arguments can be used to customize the operation.
# key:
#     Specifies a function of one argument that is used to extract a comparison key from each list element.
#     ... The default value is none (compares the elements directly)
# Reverse:
#     Boolean value. If set to true, then the list elements are sorted as if each comparison were reversed.

# Example 1:
var = [3, 6, 5, 2, 4, 1]
var.sort()
print(var)

# Example 2:
var = [3, 6, 5, 2, 4, 1]
var.sort(reverse=True)
print(var)

# Example 3:
var = ['car','bicycle', 'train', 'skate', 'airplane', 'boat']
var.sort()
print(var)

# Example 4:
var = ['car','bicycle', 'train', 'skate', 'airplane', 'boat']
var.sort(key=len)
print(var)

# Example 5:
var = ['car','bicycle', 'train', 'skate', 'airplane', 'boat']
var.sort(key=len, reverse=True)
print(var)


# In[10]:


# reverse()
# Reverses the elements of the list in place.

# Example 1:
var = [3, 6, 5, 2, 4, 1]
var.reverse()
print(var)

# Example 2:
var = ['car','bicycle', 'train', 'skate']
var.reverse()
print(var)


# In[11]:


# copy()
# Returns a shallow copy of the list. Equivalent to a[:].
# Attention: Use the copy() method when you need to update the copy without affecting the original list. If you don't
# ... use this method(eg, if you do something like list2 = list1), then any updates you do to list2 will also affect list1.

# Without copy()
var = ['car','train']
var1 = var
var1.append('truck')
print(var)
print(var1)

# With copy()
var = ['car','train']
var1 = var.copy()
var1.append('truck')
print(var)
print(var1)


# ###### source: python-ds
