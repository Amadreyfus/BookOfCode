(MyST)=
# MyST Markdown
<br />
<br />

**Quick Links to Chapter Content**
- {ref}`Basic Markdown Syntax <basic_markdown>`
- {ref}`Basic Myst Syntax <basic_myst>`
- {ref}`Useful MyST Examples and Notes <myst_ex>`

## What is MyST?
<br />

```{margin} 
For more information on this style of markdown see
[The MyST Parser documentation][myst-parser]
```

**MyST** stands for Markedly Structured Text. It is a superset of CommonMark markdown 
(the kind used in Jupyter Notebooks, for instance) incorporating certain functionalities
of [**Sphinx**](https://www.sphinx-doc.org/en/master/), such as directives and roles.


**Sphinx** is a documentation generation framework written in Python
by George Brandl that uses reStructured Text as its markup language.


[myst-parser]: https://myst-parser.readthedocs.io/en/latest/

### Directives

````{margin}
```{note}
 You can also specify these key value pairs this way:
    
    ```{directive_name} 
    ---
    key1: val1
    key2: val2
    ---
    <content of block>
    ```
```
````

Directives serve as functions that provide the functionality necessary to customize your book. 
Since MyST is built on top of Sphinx any of the directives native to the Sphinx ecosystem work in MyST.

```{caution}
Sphinx uses reStructured Text as its markup language which will need to be modified slightly into MyST format, although the functionality remains the same.
```
<br />
Here are some links to directive documentation:

* [Sphinx Directives](https://www.sphinx-doc.org/en/2.0/usage/restructuredtext/directives.html)

* [reStructured Text Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

<br />

At its most basic the syntax for a directive looks like so:

````
```{directive_name} <directive arguments>
:key1: <value1>
:key2: <value2>
<content of directive block> 
```
````

### Roles
<br />

Roles are similar to directives with the exception that they are used in-line. This takes the following general form:

```
This is what using a {role_name}`<role content goes here>` would look like.
```
<br />

Here is an example that illustrates how roles can be used and also shows the power
of the ` :label: tag ` optional argument.




````
Then these commands:

```{math} \int^{\inf}_{-\inf}e^{-x}^{2}dx = \sqrt(\pi)
:label: gaussian 
```

The Guassian Integral, equation {math:numref}`gaussian`, is an important result for
computing the Error function in statistics.

Become:
````
<br />

```{math} \int^{\infty}_{-\infty}{e^{-x}}^{2}dx = \sqrt{\pi}
:label: gaussian 
```
<br />

The Guassian Integral, equation {math:numref}`gaussian`, is an important result for computing the Error Function in Statistics.

---
```{note}
The use of angle brackets such as \<content goes here> indicate that this is space where the user can
input plain text of their choice in this space that is otherwise not part of markdown syntax
```

(basic_markdown)= 
### Basic Markdown Syntax

`````{list-table}
:header-rows: 1
:widths: 25 205

* - Description
  - Syntax
  
* - Create a Heading (6 Levels) 
  - ```md
     # <Header 1 Text>
     ## <Header 2 Text>
     ``` 
 
* - Bold Text
  - ```md
    **<content>**
    ```
  
* - Italic Text (can be combined with bold)
  - ```md
    _<content>_
    ```
* - Create a line break, vertical space
  - ```html
    <br />
    ```    
  
* - Code Fence
  - ````
    ```<language>
    :tags:
    <code content>  
    ```
    ````

* - Thematic Break via horizontal line
  - ```md
    ---
     ```


* - Create a list (`'-' ` for unordered, ` '1.' ` for ordered)
  - ````
    -
     -
     -
    ````

* - Create a Link Definition
  - ```md
    [<reference_name>]: <https://...> "<optional_title>"
    ```

* - Display a web link in final output
  - ```md
    <https://...>
     ```

* - Link to an Image
  - ```md
    ![alt](<source> "<title>")
     ```
     
`````

---

<br />

(basic_myst)= 
### Basic MyST Syntax

`````{list-table}
:header-rows: 1
:widths: 25 25

* - Description
  - Syntax
  
* - Insert a comment 
  - `% <comment content>` 
  
* - Quick LateX shortcuts
  - `$ <inline math> $  ` or `  $$ <block math> $$`

* - Create a cross-reference target
  - `(<target_name>)=`

* - Use a role
  - ```md
     {<role_name>}`<text_content>`
     ```

* - Create a footnote reference
  - <content>`[<^name_of_footnote>]`
     

* - Use a directive
  - ````
    ```{<directive>}<arguments>
    ---
    key1: val1
    key2: val2
    ---
    <content>
    ```
    ````

* - Add a citation
  - ```
    {cite}`<citation_name>`
    ```
    
`````

---
<br />

(myst_ex)=
### Useful MyST Examples and Notes

<br />

**Using YAML frontmatter**. A block of YAML front-matter just after the
first line of the directive will be parsed as options for the directive. This needs to be
surrounded by `---` lines. Everything in between will be parsed by YAML and
passed as keyword arguments to your directive. For example{cite}`myst_doc`:

````md
```{code-block} python
---
lineno-start: 10
emphasize-lines: 1, 3
caption: |
    This is my
    multi-line caption. It is *pretty nifty* ;-)
---
a = 2
print('my 1st line')
print(f'my {a}nd line')
```
````

```{code-block} python
---
lineno-start: 10
emphasize-lines: 1, 3
caption: |
    This is my
    multi-line caption. It is *pretty nifty* ;-)
---
a = 2
print('my 1st line')
print(f'my {a}nd line')
```







```{bibliography} references.bib
```