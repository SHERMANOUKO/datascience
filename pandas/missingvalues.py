#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.arange(0,15).reshape(5,3),
    index=['a','b','c','d','e'],
    columns=['c1','c2','c3']
)
df


# In[28]:


df['c4'] = np.nan
df.loc['f'] = np.arange(15,19)
df.loc['g'] = np.nan
df['c5'] = np.nan
df['c4']['a'] = 20
df


# In[30]:


#find missing values
df.isnull()


# In[31]:


#total number of missing values per column
df.isnull().sum()


# In[32]:


#total no of missing values in dataset
df.isnull().sum().sum()


# In[33]:


#count non null values per column
df.count()


# In[34]:


#count total non null values
df.count().sum()


# In[37]:


#another way to find no of nans per column
(len(df)-df.count())


# In[38]:


#another way to find total no of nans
(len(df)-df.count()).sum()


# In[40]:


#retrieve values that are not nans
df.c4[df.c4.notnull()]


# In[41]:


#drop only rowa with all nan values
x = df.dropna(how='all')
x


# In[42]:


#drop only columns with all nan values
x = df.dropna(how='all', axis=1)
x


# In[44]:


#fill nan values
df2 = df.copy()
fill = df2.fillna(0)
fill


# In[47]:


#filling using index values
fill_values = pd.Series(
    [100,101,102],
    index=['a','e','g']
)
fill_values


# In[48]:


df2.c4.fillna(fill_values)


# In[49]:


#filling with column mean values
df2.fillna(df.mean())


# In[50]:


#interpolation (estimating uknown values that fall between known values)
s = pd.Series([1,np.nan,np.nan,np.nan,2])
s.interpolate()


# In[52]:


#duplicate data
df3 = pd.DataFrame({'a':['x']*3 + ['y']*4, 'b':[1,1,2,3,3,4,4]})
df3


# In[53]:


#find duplicates
df3.duplicated()


# In[54]:


#drop duplicates
df3.drop_duplicates()


# In[57]:


#mapping
data = {
    'first_name': ['Ezra', 'Sherman', 'Martin', 'Ray', 'Joseph'],
    'last_name': ['Odhiambo', 'Ochieng', 'Omondi', 'Odero', 'Onyango'],
    'age': ['10','20','30','40','50'],
    'town': ['Ahero','Eldoret','Kasarani','Mtwapa','Juja']
}

df3 = pd.DataFrame(data, columns=['first_name','last_name','age','town'])
df3


# In[58]:


#mapping town to county
town_to_county = {
    'Ahero' : 'Kisumu',
    'Eldoret': 'Uasin Gishu',
    'Kasarani': 'Nairobi',
    'Mtwapa': 'Mombasa',
    'Juja': 'Kiambu'
}

df3['county'] = df3['town'].map(town_to_county)
df3


# In[62]:


#simple replace
s = pd.Series([0,1,2,3,4,5])
print(s)
s = s.replace(3,7)
print(s)


# In[63]:


#create a column using a function
raw_data = {
    'student_id':[1,2,3,4,5,6,7,8,9,10],
    'marks': [10,20,30,40,50,60,70,80,90,100],
}

df3 = pd.DataFrame(raw_data,columns=['student_id','marks'])
df3


# In[ ]:





# In[ ]:




