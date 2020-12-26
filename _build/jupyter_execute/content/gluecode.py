#!/usr/bin/env python
# coding: utf-8

# (glue_code)=
# # GlueCode

# In[1]:


from myst_nb import glue


# In[2]:


c0 = []
t_insert = get_ipython().run_line_magic('timeit', "-o -n3000 -r100 c0.insert(0, 'a')")


# In[3]:


glue('t_insert', t_insert)


# In[4]:


c1 = []
t_append = get_ipython().run_line_magic('timeit', "-o -n3000 -r100 c1.append('a')")


# In[5]:


glue('t_append', t_append)


# In[6]:


#Verify that both lists are the same
assert all([a == b for a, b in zip(c0, c1)]), "Answers differed?"

# Report the ratio of execution times
print(f"\n==> (insert time) / (append time) for 300,000 ops: ~ {t_insert.average/t_append.average}x")


# In[7]:


glue('t_ratio', (t_insert.average/t_append.average))


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot') # Displays graph in the style of R's ggplot


# In[9]:


x = np.linspace(0,10)
y = np.sin(x)
fig = plt.plot(x,y)


# In[10]:


glue('basic_sin', fig, display=False)


# In[ ]:




