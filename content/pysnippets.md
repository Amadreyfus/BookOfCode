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

(snippets)=
# Python Coding Snippets

**Quick References to Page Content**

- {ref}`Basic Python <basic_python>`
  -  {ref}`List Operations <list_ops>`
  -  {ref}`Random Package <random_package>`

(basic_python)=
## Basic Python

(list_ops)= 
### List Operations

Creating a list of consecutive integers

```{code-cell} ipython
:tags: [hide-output]
[i for i in range(10)]
```

Merging a list with its reverse

```{code-cell} ipython
name = 'SeanCahill'
merge = [(f,b) for f,b in zip(name, name[::-1])]
print(merge)
```

(random_package)=
### Random Package

(basic_perm)=
#### Basic permutations on a list

```{code-cell} ipython
from random import shuffle
g = [i for i in range(10)]
shuffle(g)
print(g)
```
