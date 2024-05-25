#!/usr/bin/env python
# coding: utf-8

# ## DTT Sale Analysis¶

# ## Objective: imporove customer experience by analysing sales data and increase Revenue.

# In[49]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[50]:


df = pd.read_csv(r"C:\My GiitHUB\Data Analysis Project\sales\DTT Sales Data.csv", encoding='unicode_escape')

print(df.shape)

df.info()
df.head()


# In[51]:


df.drop(['Status','Unnamed'], axis=1 , inplace=True)


# In[52]:


df.info()


# In[53]:


pd.isnull(df).sum()


# In[54]:


# which rows are having null values extracting that row
row_with_nulls=df[df.isnull().any(axis=1)]
print(row_with_nulls.to_string())


# In[55]:


df['Amount']=df.groupby('Product_Category')['Amount'].transform( lambda a : a.fillna(a.mean()))


# In[56]:


df.info()


# In[57]:


# to check the dta if null value filled with mean or not
chk=df[(df['Cust_name']=='Lakshmi') & (df['Product_ID']=='P00045842')]
chk
# as its fload value we moved to round 2
df['Amount']= df['Amount'].round(2)
chk


# In[58]:


df.columns


# In[59]:


df=df.rename(columns={'Marital_Status':'Married'})
df.columns


# In[60]:


# summary of the data
df.describe()


# In[61]:


df[['Age','Orders','Amount']].describe()


# In[62]:


# define function to make it categories in terms of age
def func(age):
     if age < 10 :
         return '0-10'
     if age < 20:
         return '10-20'
     if age < 30:
        return '20-30'
     if age < 40 :
        return '30-40'
     if age < 50:
        return '40-50'
     if age < 60:
        return '50-60'
     else:
        return '60+'
df['Age_group']=df['Age'].apply(func)
print(df)
    


# ## Exploratory_data Analysis

# ## Data Analysis  based on Gender

# In[63]:


ax=sns.countplot(x='Gender', data=df, color='g')
for bars in  ax.containers:
    ax.bar_label(bars)
ax.patches[0].set_facecolor('red')


# In[64]:


total_amount_of_orders= df.groupby('Gender')['Amount'].sum().reset_index(name='sum_of_total')
res=sns.barplot(x='Gender', y='sum_of_total', data =total_amount_of_orders, color='violet')
for bars in res.containers:
    res.bar_label(bars)
res.patches[1].set_facecolor('red')


# *from above graphs most of the buyers are female and purchasing power of female is also female*

#  ## Data Analysis based on Age group

# In[65]:


ax=sns.countplot(x='Age_group', data=df , hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[66]:


purchasing_power=df.groupby('Age_group') ['Amount'].sum().reset_index(name='total_amount_by_age')
purchase_rate=pd.DataFrame(purchasing_power)
pur=purchase_rate.sort_values(by='total_amount_by_age', ascending=False)
ax=sns.barplot(x=pur['Age_group'], y=pur['total_amount_by_age'],palette='muted')
for i in ax.containers:
    ax.bar_label(i)


# *from above graphs most of the buyers are of 30-40 years of age group*

# In[67]:


df.columns


# ##  Data Analysis based on married

# In[68]:


ax2= sns.countplot(x='Married',data=df , hue='Gender')
for i in ax2.containers:
    ax2.bar_label(i)


# In[69]:


## total count of orders   w.r.t married column:
sns.countplot(data=df,x='Married', palette='muted',hue='Gender')


# In[70]:


## total Amount of order based on married :
total_amount_by_married=df.groupby(['Married','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(5,5)})
sns.barplot(data=total_amount_by_married,x='Married' , y='Amount',palette='muted', hue='Gender')


# *from the above groups we can see unmarried women people are the most buyers and spends more amounts as well !*

# # State

# In[73]:


# total of orders in top 10 state
order_by_st = df.groupby('State')['Orders'].sum().sort_values(ascending=False).head(10)
order_by_st = pd.DataFrame(order_by_st).reset_index()  #
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data=order_by_st, x='State', y='Orders', palette='muted')



# In[77]:


# Total amount of orders in top 10 states
order_by_st = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
order_by_st = pd.DataFrame(order_by_st).reset_index()  # Resetting index for 'State'
sns.set(rc={'figure.figsize': (16, 5)})
sns.barplot(data=order_by_st, x='State', y='Amount', palette='muted')



# *here we can see that if the total  orders are hign in kerala but sum of amount is less its not present in  top 10*

# ## occupation

# In[78]:


## count of occupation for every buyer

sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation', palette='muted')
for i in ax.containers:
    ax.bar_label(i)


# In[82]:


## sum  of  amount of every  occupation for every buyer

order_by_st = df.groupby('Occupation')['Amount'].sum().sort_values(ascending=False).head(10)
order_by_st = pd.DataFrame(order_by_st)

sns.set(rc={'figure.figsize': (16, 5)})
ax = sns.barplot(data=order_by_st, x=order_by_st.index, y='Amount', palette='muted')

for p in ax.patches:
    ax.annotate(format(p.get_height(), '.2f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'center', 
                xytext = (0, 9), 
                textcoords = 'offset points')

plt.xticks(rotation=45) 
plt.show()


# *From the above graphs we can see that all the buyers are working on IT Sector, Healthcare, Aviation*

# ## product_category

# In[83]:


## count of Product_Category for every buyer

sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Product_Category', palette='muted')
for i in ax.containers:
    ax.bar_label(i)


# In[85]:


## sum of amount based on product_category

order_by_st = df.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False).head(10)
order_by_st = pd.DataFrame(order_by_st)
sns.set(rc={'figure.figsize':(16,5)})
ax = sns.barplot(data=order_by_st, x=order_by_st.index, y='Amount', palette='muted') 
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 10), 
                   textcoords = 'offset points')  


# *from the above graphs we can see most of the sold products from food, colthing, and foortwear category*

# *Married women with age group of 30-40 from UP,Maharastra, Karnataka are working in IT, helathCare,aviation are mostly buying food, clothing,Footwear Category!*

# In[ ]:


## Divan TT

