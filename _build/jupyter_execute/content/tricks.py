#!/usr/bin/env python
# coding: utf-8

# (tricks)=
# # Useful Tricks for Ipython / Data Science

# (shifttab)=
# ## Shift + Tab in method parentheses

# In a python method call that has optional arguments, i.e. `object.method()`, you can place the cursor inside the parantheses and press `Shift + Tab` to pull up documentation on the method.  
# 
# You can repeat this `Shift + Tab` operation up to 4 times each subsequent call modifying the information displayed with increasing duration, size, info....

# (multiplefilter)=
# ## Applying multiple filter criteria to a DataFrame

# In a dataframe with multiple columns you can use bitwise logical operators (`&`, `|`, `~`, `^`) to chain the filtering conditions together:   
# 
# For example:
# 
# ```python
# df[(df.column1 > value1) | (df.column2 == value1)]
# ```

# Another nice trick for filtering a df based on certain values in a Series/columnd is to use `.isin()`
# 
# ```python
# df[df.column.isin([value1, value2, value3])
# ```   

# In[ ]:




