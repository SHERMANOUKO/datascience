#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(6,5,7)
y = x**2

plt.plot(x,y,'b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('My first plot')


# In[10]:


plt.subplot(1,2,1)
plt.title('plot 1')
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.title('plot 2')
plt.plot(y,x)


# In[ ]:





# In[6]:


tips = sns.load_dataset('tips')


# In[17]:


tips.head()


# In[33]:


plt.figure(figsize=(8,6))
sns.barplot(x='sex',y='total_bill',data=tips)
plt.figure(figsize=(8,6))
sns.lineplot(x='size',y='total_bill',data=tips)


# In[38]:


sns.distplot(tips['total_bill'],kde=True,bins=30)


# In[39]:


sns.countplot(x='sex',data=tips)


# In[40]:


sns.countplot(x='day',data=tips)


# In[42]:


sns.boxplot(x='day',y='total_bill',data=tips,palette='hls')


# In[50]:


sns.scatterplot(x='total_bill',y='tip',hue='time',data=tips,palette='hls')


# In[51]:


sns.scatterplot(x='total_bill',y='tip',hue='sex',data=tips,palette='hls')


# In[52]:


sns.scatterplot(x='total_bill',y='tip',hue='day',data=tips,palette='hls')


# In[57]:


sns.violinplot(y='total_bill',x='day',hue='sex',data=tips,palette='hls',split=True)


# In[61]:


sns.stripplot(y='total_bill',x='day',hue='sex',data=tips,palette='hls',dodge=True)


# In[62]:


sns.swarmplot(y='total_bill',x='day',hue='sex',data=tips,palette='hls')


# In[65]:


sns.pairplot(tips,hue='sex')


# In[68]:


sns.jointplot(y='total_bill',x='tip',data=tips,kind='hex')


# In[70]:


corre = tips.corr()
sns.heatmap(corre)


# In[74]:


sns.lmplot(y='total_bill',x='tip',data=tips)


# In[7]:


tips.tail()


# In[ ]:




