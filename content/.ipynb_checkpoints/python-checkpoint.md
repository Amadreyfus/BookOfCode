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

(python)=
# Python 3

<br />

**Quick References to Page Contents**

- {ref}`Primitive Types <primitive>`
  - {ref}`Type Checking Operations <type_check>`
  - {ref}`Basic Mathematical Operations <basic_math>`
  - {ref}`Strings <strings>`
- {ref}`Collections <collections>`
  - {ref}`Lists <lists>`
  - {ref}`Tuples <tuples>`
  - {ref}`Dictionaries`
- {ref}`Control Flow <control_flow>`  
  


<br />

(primitive)=
## Primitive Types in Python

| Type        | Example        | Description                                                  |
|-------------|----------------|--------------------------------------------------------------|
| ``int``     | ``x = 1``      | integers (i.e., whole numbers)                               |
| ``float``   | ``x = 1.0``    | floating-point numbers (i.e., real numbers)                  |
| ``complex`` | ``x = 1 + 2j`` | Complex numbers (i.e., numbers with real and imaginary part) |
| ``bool``    | ``x = True``   | Boolean: True/False values                                   |
| ``str``     | ``x = 'abc'``  | String: characters or text                                   |
| ``NoneType``| ``x = None``   | Special object indicating nulls                              |

(type_check)=
### Type Checking Operations

`````{list-table}
:header-rows: 1

* - Syntax
  - Description
  
* - ```python
    type(<object>)
    ```
  - Returns type of the object. Useful syntax below:    
    ```python
    type([]) is list
    ```

* - ```python
    isinstance(<object>, <type>)
    ```    
  - Returns boolean value corresponding to truth of the statement
    
* - ```python
    <object> is None, <object> is not None
    ```    
  - This is the preferred idiom for checking if an object is `None` type
        
`````  


<br />

(basic_math)=
### Basic Mathematical Operations

These are sometimes called the 'natural operators'

| Operator     | Name           | Description                                            |
|--------------|----------------|--------------------------------------------------------|
| ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
| ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
| ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing any remainder    |
| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
| ``-a``       | Negation       | The negative of ``a``                                  |
| ``+a``       | Unary plus     | ``a`` unchanged                                        |

(strings)=
### Strings

(collections)=
## Collections

(lists)=
### Lists

 - A list is similar to arrays in other languages. It is a sequence of values contained within square brackets and separated by a comma: `[1, 2, 'a', ...]`

 - The list data structure facilitates fast random access and appends, but slow arbitrary insertions and searches. 
 
 - A list can contain heterogenous elements
 
 - A list is mutable
 
#### Constructing Lists

```{code-cell} ipython3

list1 = [] # empty list
list2 = list() # empty list
list3 = list('string') # creates a list from individual letters, str has __iter__ attribute
```

#### List Comprehensions

List comprehensions provide a unique way to generate list from iterable objects and some examples of this syntax are:

``` python
new_list = [expression for i in iterable] # applies the expression to each item in the iterable to generate new list   

upper = [x.upper() for x in 'string']
```

Here is the output of the second expression.
```{code-cell} ipython
upper = [x.upper() for x in 'string']
print(upper)
```

#### Zipper Iterations

`zip(list1, list2, ...) ` creates tuples of corresponding elements in various collections

(add_list)=
#### Adding Elements to a List

```{list-table}
:header-rows: 1

* - Sytnax
  - Description
  
* - `list.append(x)`
  - Adds element to the end of a list
  
* - `list.extend([x, y, z]) ` or ` list1 + list2`
  - Concatenates a current list with another
  
* - `list.insert(i, elem)`
  - inserts the new element at ` list[i] ` and shifts every element at [i,+) to the right one place

```





(tuples)=
### Tuples

A **Tuple** is a read-only "immutable" fixed-length sequence of values

```{code-cell} ipython3

tup = (1,'a', None)
for i in range(len(tup)):
    print(f'element at index i in tup is: {tup[i]}')
```

**Immutability** means that you cannot modify the object. Once set, it's size and values are permanently fixed. So,
in order to "change" the object, you must create a new one incorporating the old one.

(dictionaries)=
### Dictionaries

A dictionary is map of unique keys to values. Like set elements, keys must be unique.

(control_flow)=
## Control Flow

(assertions) = 
### Assertions

Assertions provide a way of checking if variables have certain values or objects meet certain conditions which
minimizes the risk of an error in the code. General form:


```python
assert <boolean condition>, <error string>
```

Specific examples:

```python 
assert n >= 0, f'n must be non-negative and is {n} instead'

assert isinstance(a, str) and isinstance(b, str), \
       f'One of a:{type(a)} or b:{type(b)} is not a string'
```

(lambda)=
### Lambda Functions (Anonymous Functions)

$\lambda\,$ Functions are functions that are specified by the keyword `lambda` and do not need to be 
named. They have the general form

```python
lambda x: <expression(x)>
```
where the variables on the left side of the colon are considered "bound" variables.  

Here are some concrete examples of lambda functions:

```python
lambda x: x + 1
(lambda x: x + 1)(2) # Applies lambda function to the argmuent (2)
add_one = lambda x: x + 1
full_name = lambda first, second: f'Full name: {first.title()} {second.title()}'
```
````{margin}
```{caution}
Because under the hood the lambda function has no name, it can be harder to debug since the 
traceback will not contain as much information
```
````

````{important}
Lambda functions can prove very useful by providing functionaly in normally tricky spots. A 
good example is working as a key to sort a dictionary by specific values. A more fleshed out example can 
be found {ref}`here <sort_dic_by_key>`.

```python
sorted(data, key= lambda x: x['key_value'])
```


  
  
  