---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(commonpandas)=

# Common Pandas Operations

These are just some general coding fragments that I feel are used frequently enough to warrant annotating, 
but also infrequently enough that they are not generally immediately recallable.  

They are roughly organized around what specific pandas object or operation is invoked.


(pdindex)=
## Index 

```python3
df.reindex()      #Pass a new index to this to create a new index for datafrane
df.reset_index()  #Just resetting the index 
df.set_index()    #Can set index based on columns (useful for multiindexing)
df.reindex_like() #Uses index of another dataframe
```

(pdvalues)=
## Values in a DF or Series

```python3
df.column.value_counts() #Returns a Series with values and their associated counts of a column
```


(pdmerging)=
## Merging DFs, Series, columns

```python3
df = pd.concat([df, column], axis=1) #Adds a new column to the df
```

