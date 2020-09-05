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

[i for i in range(10)]

Merging a list with its reverse

name = 'SeanCahill'
merge = [(f,b) for f,b in zip(name, name[::-1])]
print(merge)

(random_package)=
### Random Package

(basic_perm)=
#### Basic permutations on a list

from random import shuffle
g = [i for i in range(10)]
shuffle(g)
print(g)