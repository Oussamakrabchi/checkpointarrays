#!/usr/bin/env python
# coding: utf-8

# In[7]:


# exo 1 :
import numpy as np
myarray = np.array([(1,2,4),(4,5,7),(2,12,1)])
mylist = myarray.tolist()
print(mylist)


# In[8]:


# exo 2 :
trace = np.trace(myarray)
print(trace)


# In[9]:


# exo 3 :
x = 5
for i in range (1, 3) :
    for j in range (1 , 3) :
        if (myarray[i][j] > x) :
            print (myarray[i][j])


# In[10]:


# exo 4 :
myarray2 = np.array([(2,4,5),(4,4,4),(12,22,3)])
addition = np.add(myarray , myarray2)
print(addition)


# In[11]:


# exo 5 :
mean1 = np.mean(myarray, axis = 1)
print(mean1)
addition = np.add(myarray , -mean1)
print(addition)


# In[ ]:





# In[ ]:




