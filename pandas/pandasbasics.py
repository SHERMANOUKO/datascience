#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

#read csv file into datafarame
df = pd.read_csv('titanic.csv')

#print first 10 values
print(df.head(10))

#print last 10 values
df.tail(10)


# In[27]:


#print no of rows and columns
df.shape

#print columns
df.columns

#print datatypes
df.dtypes


# In[9]:


#create a subset with only given columns
subset = df[['Sex', 'Age']]

#print only first 5 of the subset
print(subset.head(5))

#print only last 5 of the subset
print(subset.tail(5))


# In[11]:


#print first row on dataset
print(df.loc[0])

#print last row on dataset
print(df.tail(n=1))


# In[13]:


#print data in 1st 10th and 100th position
print(df.loc[[0, 9, 99]])


# In[20]:


#print out a subset of a row and column simultaneously
print(df.loc[0, 'Age'])

#subset of multiple rows and multiple columns using column names
print(df.loc[[0, 9, 99], ['Name', 'Sex', 'Age']])

#subset of multiple rows and multiple columns using column index
print(df.iloc[[0, 9, 99], [3, 4, 5]])


# In[24]:


#group by age count (no of passengers by their age)
df.groupby("Age").PassengerId.count()


# In[32]:


#check the percentage of those who survived per passenger class
df.groupby('Pclass')['Survived'].mean()


# In[38]:


#check the mean age of passengers per class
df.groupby('Pclass')['Age'].mean()


# In[54]:


df.groupby('Age')['Pclass'].nunique()


# In[37]:


df.groupby('Age')['Sex'].nunique()


# In[4]:


#take statistics summarry
df.Age.describe() #could also be df['Age'].describe()


# In[11]:


ages = df['Age']
ages[ages < ages.mean()]


# In[13]:


df.Age + df.Age


# In[16]:


#rename column headers
df.rename(columns={'Age' : 'age'}, inplace=True)
df


# In[19]:


#sort by age (ascending)
df.sort_values(by='age', ascending=1)


# In[22]:


#sort by multiple columns
df.sort_values(by=['Pclass', 'age'])


# In[26]:


#binning data
bins = [0, 10, 25, 50, 75, 100]
group_names = ['Toddler', 'Young', 'Adult', 'Senior', 'GrandParent']

df['categories'] = pd.cut(df['age'], bins, labels=group_names)
df.categories


# In[28]:


#count group by created categories
pd.value_counts(df['categories'])


# In[5]:


#concatenating a dataframe
df1 = pd.read_csv('titanic.csv')
df2 = pd.read_csv('titanic.csv')

#notice that the number of rows doubles from 891 to 1782 after concatenation
concat = pd.concat([df1, df2])
concat


# In[8]:


#row concatenation
f1 = df1.iloc[[1,2,3]]
f2 = df2.iloc[[1,2,3]]

row_concat = pd.concat([f1,f2])
row_concat


# In[11]:


#merging and joining
data = {
    'subject_id': ['1','2','3','4','5'],
    'first_name': ['Ezra', 'Sherman', 'Martin', 'Ray', 'Joseph'],
    'last_name': ['Odhiambo', 'Ochieng', 'Omondi', 'Odero', 'Onyango']
}

dfa = pd.DataFrame(data, columns=['subject_id', 'first_name', 'last_name'])

data = {
    'subject_id': ['1','2','3','4','5'],
    'first_name': ['Ezra', 'Man', 'Min', 'Ray', 'Jeph'],
    'last_name': ['Odhiambo', 'Ochieng', 'Omondi', 'Odero', 'Onyango']
}

dfb = pd.DataFrame(data, columns=['subject_id', 'first_name', 'last_name'])

#inner join. Displays matching records
merged = pd.merge(dfa,dfb, on='first_name', how='inner')
merged


# In[12]:


#full outer join. Displays all records. UNmatching records shows by NaNs
merged = pd.merge(dfa,dfb, on='first_name', how='outer')
merged


# In[13]:


#right outer join. Displays rows where there is a match and rows from right table
merged = pd.merge(dfa,dfb, on='first_name', how='right')
merged


# In[14]:


#left outer join. Displays rows where there is a match and rows from left table
merged = pd.merge(dfa,dfb, on='first_name', how='left')
merged


# In[ ]:




