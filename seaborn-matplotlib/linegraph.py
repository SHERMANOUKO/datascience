#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

y = [81.23,78.45,72.80,74.67,79.45,67.34,63.75,68.42,75.67,74.65,67.78]
x = ['FIT1','F1T2', 'F1T3','F2T1','F2T2','F2T3','F3T1','F3T2','F3T3','F4T1','F4T2']
plt.plot(x,y,'--b')
plt.grid(color='#666666', linestyle='--')
plt.show()


# In[ ]:




