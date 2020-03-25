#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd


# In[45]:


df = pd.read_csv('housepricedata.csv', delim_whitespace=True, header=None)


# In[46]:


df


# In[7]:


dataset = df.values


# In[8]:


dataset


# In[9]:


X = dataset[:,0:10]


# In[10]:


Y = dataset[:,10]


# In[11]:


from sklearn import preprocessing


# In[12]:


min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)


# In[13]:


X_scale


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)


# In[16]:


X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


# In[17]:


print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)


# In[22]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[48]:


model = Sequential([
    Dense(10, activation='relu'),
    Dense(1, kernel_initializer='normal'),
])


# In[49]:


model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])


# In[50]:


hist = model.fit(X_train, Y_train,
          batch_size=5, epochs=100,
          validation_data=(X_val, Y_val))


# In[26]:


model.evaluate(X_test, Y_test)[1]


# In[29]:


example = dataset[2,0:10]


# In[37]:


example


# In[36]:


model.predict(example)


# In[ ]:




