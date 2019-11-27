#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np

#create a dictionary array
dictData = {
    'subjects':['english','swahili','chem','physics','maths'],
    'pass':[12,13,34,23,1],
    'fails':[1,3,1,4,7]
}

#add labels for index
labels = [1,2,3,4,5]
df = pd.DataFrame(dictData,index=labels)
print(df)


# In[86]:


#Describing to have a general overview
df.describe()


# In[87]:


#Transposing
df.T


# In[88]:


#Sorting data using no of pass
df.sort_values(by='pass')


# In[89]:


#Slicing by getting first 2
df[:2]


# In[90]:


#Getting top 2 by no of fails
df.sort_values(by='fails')[:2]


# In[91]:


#Getting pass only
df[['fails']]


# In[92]:


#Checking if there are any null values
df.isnull()


# In[93]:


#finding means
print(df.mean())
print(df[['pass']].mean())
print(df[['fails']].mean())


# In[82]:


#Finding sum
print(df.sum())


# In[95]:


#working with missing values
df2 = [1,2,3,np.nan,4,5]
df2 = pd.DataFrame(df2)
df1 = df2.copy()
print(df2)


# In[97]:


#replace the null values with zero
df2 = df2.fillna(0)
print(df2)


# In[99]:


#DRopping all null rows
df1 = df1.dropna(how='any')
print(df1)


# In[103]:


#saving and reading data using files
df1.to_csv('data.csv')
df1.to_excel('data.xlsx',sheet_name='sheet1')
df_readData=pd.read_csv('data.csv')


# In[101]:


df_readData.head(5)


# In[ ]:




