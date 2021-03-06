#!/usr/bin/env python
# coding: utf-8

# (matplotlib)=
# # Matplotlib

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# (styles)=
# ## Styles in Matplotlib

# In[2]:


plt.style.available


# In[3]:


#Selecting popular 'ggplot' style from R language
plt.style.use('ggplot')


# (plotting)=
# ## Plotting in a Jupyter Notebook

# `%matplotlib notebook` for interactive plots embedded in the notebook.  
# 
# `%matplotlib inline` for static plots.

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ### Quick plot example

# In[5]:


x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x), 'r--')
plt.plot(x, np.cos(x), 'b-');


# (savingfig)=
# ### Saving a Figure to a File

# In[6]:


#Extension inferred from one given in name.
fig.savefig('ex_fig.png')


# In[7]:


#Here are the available extension types in this notebook.
fig.canvas.get_supported_filetypes()


# ### Using Ipython's `Image` object to display our saved figure

# In[8]:


from IPython.display import Image
Image('ex_fig.png')


# (twointerfaces)=
# ## The Two Interfaces of Matplotlib. Object-Oriented is more powerful

# (matlab)=
# ### MATLAB style (stateful) Interface

# In[9]:


plt.figure() # create a plot figure
# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));


# (OOstyle)=
# ### More precise OO Style

# In this styles figures and axes object are treated as objects with references. Modifications to the objects
# are as you would expect with other python objects - made through method and function calls.

# In[10]:


# Create a figure object (think of this as a blank canvas/container in which to work)
# Also create an axes object. This provides the structure on the canvas (grid lines, layout) and dictates the actual visuals
fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object. Here we specificy which of the axes we want using 0-indexing.
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x));


# (stackedplot)=
# ### An Example of Multiple Axes on the Same Figure

# In[11]:


plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()

x = np.linspace(-10, 10, 50)
ax.plot(x, np.sin(x))
ax.plot(x, np.sin(x)-1)
ax.plot(x, np.sin(x)-2)
ax.plot(x, np.sin(x)-3)
ax.plot(x, np.sin(x)-4);

plt.close(fig) # Useful for not having the output of figure display!


# In[12]:


fig


# (axis_limits)=
# ### How to Set Different Axis Limits

# It is important to note that the order of the limits matters, ie you can change the direction of the axes (proper) by inputting
# a backwards order.

# In[13]:


ax.set_xlim(-4*np.pi, 4*np.pi)
ax.set_ylim(-4*np.pi, 4*np.pi)


# In[14]:


fig


# (axismethod)=
# #### Here is Another Method to Change Axis Limits.

# There are string type arguments that can be used for a more automatic type of axis formatting. These arguments include:
# 
# 'equal', 'scaled', 'tight', 'auto', 'normal', 'image', and 'square' . `Shift + Tab` inside parenthesis pulls up documentation.

# In[15]:


ax.axis('tight')


# In[16]:


fig


# (plotlabels)= 
# ### Labelling Your Plots

# Using the `ax.set_<ax_object>` method lets you add context to various ax objects in a plot

# In[17]:


ax.set_title('Family of Sins')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')


# In[18]:


fig


# In[ ]:




