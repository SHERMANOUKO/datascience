#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
print(pd.__version__)


# In[43]:


#Basics for series
myList = [10,20,30,40,50]

#Coverting list to a series
myLstSeries = pd.Series(myArr)
print(myLstSeries)


# In[44]:


#Series from dictionary
myDict = {'a':10,'b':20,'c':30,'d':40,'e':50}
myDictSeries = pd.Series(myDict)
print(myDictSeries)


# In[45]:


#slicing a series
print(myDictSeries[2:]) #ignoring first 2
print(myDictSeries[:3]) #first 3
print(myDictSeries[:-2]) #ignoring last two


# In[46]:


#Appending serieses
print(myLstSeries.append(myDictSeries))


# In[47]:


#deleting a series element
myLstSeries = myLstSeries.drop(1)
print(myLstSeries)


# In[48]:


s1 = [1,2,3,4,5,6,7]
s2 = [1,2,3,4,5]


# In[49]:


s1 = pd.Series(s1)
s2 = pd.Series(s2)
s1.add(s2)


# In[50]:


s1.sub(s2)


# In[51]:


s1.mul(s2)


# In[52]:


s1.div(s2)


# In[53]:


s1.median()


# In[54]:


s1.max()


# In[ ]:




