#!/usr/bin/env python
# coding: utf-8

# In[7]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]

import numpy as np
x = np.array(x)
y = m*x + c 
print(y)


# In[14]:


import matplotlib.pyplot as plt 
plt.plot(x,y)
plt.show()


# In[15]:


import matplotlib.pyplot as plt 
plt.scatter(x,y)
plt.show()


# In[ ]:




