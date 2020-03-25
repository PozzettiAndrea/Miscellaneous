#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# In[3]:


df = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)


# In[4]:


df


# In[71]:


dataset = df.values


# In[72]:


dataset


# In[73]:


X = dataset[:,0:13]


# In[74]:


Y = dataset[:,13]


# In[75]:


model = Sequential()
model.add(Dense(13, activation='relu'))
model.add(Dense(13, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])


# In[81]:


hist = model.fit(X, Y, epochs=10000)


# In[82]:


example = dataset[0:5,0:13]


# In[83]:


example


# In[84]:


model.predict(example)


# In[ ]:




