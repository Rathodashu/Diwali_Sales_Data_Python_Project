#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[10]:


df = pd.read_csv("C:Diwali Sales Data.csv", encoding= 'unicode_escape')


# In[11]:


df.shape


# In[14]:


df.head(10)


# In[15]:


df.info()


# In[16]:


# drop unrelated/blank columns
df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[17]:


df.info()


# In[18]:


# check for null values
pd.isnull(df)


# In[19]:


# how many null values in data than you can use sum() function.
pd.isnull(df).sum()


# In[20]:


df.shape


# In[21]:


# drop null values
df.dropna(inplace=True)


# In[22]:


# if you want to change data type than use astype function.
df['Amount'] = df['Amount'].astype('int')


# In[23]:


df['Amount'].dtypes


# In[24]:


df.columns


# In[25]:


# rename column name
df.rename(columns={'Marital_Status':'Shadi'})


# In[26]:


# describe()method returns description of the data in the DataFrame(i.e. count, mean, std, etc.)
df.describe()


# In[27]:


# use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# ### Exploratory Data Analysis
# 
# * Gender

# In[28]:


df.columns


# In[29]:


sns.countplot(x = 'Gender',data = df)


# In[31]:


ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[42]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_Gender)


# ### Age

# In[38]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# ### State

# In[43]:


df.columns


# In[44]:


# total number of orders from top 5 or 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data = sales_state, x = 'State' ,y= 'Orders')


# In[45]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(5)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data = sales_state, x = 'State' ,y= 'Amount')


# ### Marital Status

# In[48]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[50]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(data = sales_state, x = 'Marital_Status' ,y= 'Amount', hue='Gender')


# ### Occupation 

# In[51]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[52]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation' ,y= 'Amount')


# ### Product Category

# In[54]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category' ,y= 'Amount')


# In[56]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID' ,y= 'Orders')


# In[59]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ### Conclusion

# In[61]:


# * Married women age group 26-35 yrs from UP, Maharashtra and karnataka working in IT, healthcare and aviation are more likely 
# buy products from food, clothing and electronics category*


# In[ ]:




