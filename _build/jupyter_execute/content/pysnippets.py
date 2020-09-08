(snippets)=
# Python Coding Snippets

**Quick References to Page Content**

- {ref}`Basic Python <basic_python>`
  -  {ref}`List Operations <list_ops>`
  -  {ref}`Dictionary Operations <dict_ops>`
  -  {ref}`Random Package <random_package>`
- {ref}`Slick Sorting and Other Tricks <sorting>` 

(basic_python)=
## Basic Python

(list_ops)= 
### List Operations

<br />

**Quick Ref**
- {ref}`List of Consecutive Integers <list_consec>`
- {ref}`Merging a List with its Reverse <list_merge>`
- {ref}`Performance of Append vs Insert <list_perform>`

(list_consec)=
#### Creating a list of consecutive integers

list(range(10))
[i for i in range(10)]

(list_merge)=
#### Merging a list with its reverse

name = 'SeanCahill'
merge = [(f,b) for f,b in zip(name, name[::-1])]
print(merge)

(list_perform)=
#### Checking the Performance of Insert Vs Append. 

**Appending is generally a much faster operation than arbitrary insertion.** 

````{margin}
```{note}
Although inserting at the `[-1]`
is of a comparable runtime.
```
````

c0 = []
t_insert = %timeit -o -n1000 -r100 c0.insert(0, 'a')

c1 = []
t_append = %timeit -o -n1000 -r100 c1.append('a')

<br />
Let us see the the ratio of execution times for these two cell blocks:  

<br />

#Asserting that both lists are equivalent
assert all([a == b for a, b in zip(c0, c1)]), "Answers differed?"

print(f'==> (insert time)/(append time) for 1000 operations: ~{t_insert.average/t_append.average}x')

<br />
Here is the same thing with more loops to demonstrate scaling. That is
as the number of ops grows, so will execution time.

<br />

```python
#Same experiment as above, but triple the ops
c0 = []
t_insert = %timeit -o -n3000 -r100 c0.insert(0, 'a')
```

```{glue:} t_insert
```

```python
# Append the same 100,000 values at the end of the list
c1 = []
t_append = %timeit -o -n3000 -r100 c1.append('a')
```

```{glue:} t_append
```

```python
# Verify that the outputs of the above are the same
assert all([a == b for a, b in zip(c0, c1)]), "Answers differed?"

# Report the ratio of execution times
print(f"\n==> (insert time) / (append time) for 3,000 ops: ~ {t_insert.average/t_append.average}x")
```

(insert time) / (append time) for 3,000 ops: ~ {glue:text}`t_ratio`x

(dict_ops)=
### Dictionary Operations

#### Creating a Dictionary using enumerate() iterator

D = {k: v for v, k in enumerate('abcdefghijk')}
print(D)

(random_package)=
### Random Package

(basic_perm)=
#### Basic permutations on a list

from random import shuffle
g = [i for i in range(10)]
shuffle(g)
print(g)

(sorting)=
### Slick Tricks Involving Sorting and Parsing

(sort_dic_by_key)=
#### Sorting a Dictionary by a Specific Key

data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]

sorted(data, key=lambda x: x['YOB'])