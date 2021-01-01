#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\iris.csv")
df.head(5)


# In[5]:


df.columns


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


df['species'].unique()


# In[9]:


df['species'].nunique()


# In[11]:


sns.pairplot(df,hue='species',height=3)


# In[12]:


df1=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\Sal.csv")
df1


# In[17]:


plt.figure(figsize=(10,5))
sns.barplot(df1['F_name'],df1['Sal'])


# In[20]:


plt.figure(figsize=(10,5))
sns.barplot(df1['L_Name'],df1['Sal'])


# In[21]:


plt.figure(figsize=(10,5))
sns.barplot(df1['L_Name'],df1['Age'])


# In[22]:


plt.figure(figsize=(10,5))
sns.barplot(df1['F_name'],df1['Age'])


# In[25]:


df2=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\seaborn tip-30.10.2020.csv")
df2


# In[26]:


df2.info()


# In[28]:


df2.describe()


# In[29]:


df2.columns


# In[35]:


#Box Plot
plt.figure(figsize=(10,5))
sns.boxplot(x=df2['Gender'],y=df2['Total_bill'])


# In[36]:


df2['Total_bill'].min()


# In[37]:


print(type(df2))


# In[43]:


#3D plot
plt.figure(figsize=(10,5))
from  mpl_toolkits import mplot3d
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(df['sepal_length'],df['sepal_width'],df['petal_length'],c='r',marker='o')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
ax.set_zlabel('petal_length')


# In[44]:


sns.scatterplot(df['sepal_length'],df['petal_length'],hue=df['species'])
#from given graph it is observed that: if Pl is in range 1-2 then 
#100% flower species is setosa


# In[45]:


sns.scatterplot(df['sepal_length'],df['petal_width'],hue=df['species'])


# In[46]:


#student task
#plot a scatter plot with each possible pair of two col in iris dataset
sns.scatterplot(df['sepal_width'],df['petal_width'],hue=df['species'])


# In[47]:


sns.scatterplot(df['petal_length'],df['petal_width'],hue=df['species'])


# In[48]:


sns.scatterplot(df['petal_length'],df['sepal_width'],hue=df['species'])


# In[49]:


sns.scatterplot(df['sepal_length'],df['sepal_width'],hue=df['species'])


# In[50]:


sns.scatterplot(df['petal_length'],df['sepal_length'],hue=df['species'])

