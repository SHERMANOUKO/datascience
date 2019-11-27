#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


#create a numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)

#specify type float
a = np.array([1, 2, 3, 4], float)
print(a)


# In[4]:


#slicing and indexing of arrays
print(a[:2])
print(a[2])


# In[7]:


#multidiemansional array
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b)


# In[15]:


#using index for multidimensional array
print(b[0, 0])
print(b[0])
print(b[1])
print(b[1, 3])


# In[20]:


#find shape
print(b.shape)

#find length (gives length of first axis)
print(len(b))


# In[21]:


#test if value is present in array
print(2 in b)
print(11 in b)


# In[28]:


#transpose array
print(b.transpose())

#reshape array
print(b.reshape(5,2))


# In[24]:


#convert array to list
print(b.tolist())


# In[30]:


#concatenate arrays
c = np.array([1, 2, 3, 4])
d = np.array([5, 6, 7, 8])

np.concatenate((c, d))


# In[40]:


#create array using arrange
e = np.arange(5, dtype=float)
print(e)

f = np.arange(1, 6, 2, dtype=int)
print(f)


# In[41]:


#zero like and one like
print(np.zeros_like(b))
print(np.ones_like(b))


# In[42]:


#creating idenitity matrix
print(np.identity(2, dtype=int))
print(np.identity(3, dtype=int))
print(np.identity(1, dtype=int))


# In[44]:


#The eye function returns matrices with ones along the kth diagonal:
print(np.eye(4, k=1, dtype=int))
print(np.eye(4, k=2, dtype=int))
print(np.eye(4, k=0, dtype=int))


# In[11]:


#array iteration
for x in a:
    print(x)
    
for x in b:
    print(x)


# In[12]:


#summing
print(a.sum())
print(b.sum())


# In[13]:


#product
print(a.prod())
print(b.prod())


# In[21]:


#mean, varianze, std
print(a.mean())
print(b.mean())
print(b.mean(axis=1))
print(b.mean(axis=0))


# In[16]:


#maximum, minimum value
print(b.max())
print(b.min())


# In[18]:


#position of max and min values
print(b.argmax())
print(b.argmin())


# In[22]:


#sort array
print(sorted(a))


# In[23]:


#clip array values
print(b.clip(3, 8))


# In[25]:


#extract unique elements
x = np.array([1, 2, 3, 2, 4, 2, 1, 4, 5, 6, 7, 5])
print(np.unique(x))


# In[26]:


#etxract diagonoal from 2 dimensional array
print(b.diagonal())


# In[ ]:




