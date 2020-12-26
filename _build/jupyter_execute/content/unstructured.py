#!/usr/bin/env python
# coding: utf-8

# (unstructured)=
# # Unstructured Text / Regular Expressions

# (simple)=
# ## Some simple string processing methods 
# 
# These can be applied globally (returning one bool value for whole string) or on each individual character
# in the string (using iteration).

# In[1]:


text = "sgtEEEr2020.0"


# In[2]:


# Strings have methods for checking "global" string properties
print("1.", text.isalpha())

# These can also be applied per character
print("2.", [c.isalpha() for c in text])


# ### Here is a list of very basic ones

# ```python 
# text.isdigit()
# text.isalpha()
# text.isspace()
# text.islower()
# text.isupper()
# text.isnumeric()
# ```

# (regularexpressions)=
# ## Regular Expressions

# Regular Expresssions are made available in python through the `re` module. Here are some useful links:
# 
# [Regular Expression HowTo](https://docs.python.org/3/howto/regex.html0)
# 
# [Regular Expression Documentation](https://docs.python.org/3/library/re.html#module-re)
# 
# (metacharacters)=
# ### Metacharacters
# 
# Metacharacters in Regexes specificy some unique behavior and allow for more complex pattern matching. They have a sytnactic value separate from their 
# literal value, unless part of a class that specifies otherwise.
# 
# They include: ` . ^ $ * + ? { } [ ] \ | ( )`
# 
# (squarebrackets)=
# #### Square Brackets ` [ ] `
# 
# `[ ]` are used for specifying a character class: a set of characters you wish to mathch.
# 
# - Can be listed individually: `[abcd] ` or using a hyphen for a range `[a-d]`
# - Metacharacters lose their special significance inside `[]` so `[a[bc]]` will look to match all 5 characters including brackets.
# - **Complements:** `[^a] ` A carrot at the start will indicate to search for every character except those within `[]`
# 
# (backslash)=
# #### Backslash `\`
# 
# - Arguably most important metacharacter. Can be used as an escape sequence `\\` == ``` `\` ```
# - More importantly, \ can be used to specify certain predefined sequences. 
# 
# Here are some of the most common
# 
# ```{list-table}
# :header-rows: 1
# 
# * - Command
#   - Sequence
# 
# * - `\d`
#   - Matches any decimal digit, [0-9]
#   
# * - `\D`
#   - Complement of `\d`. Matches any non-digit character. [^0-9]
#   
# * - `\s`
#   - Matches any whitespace character, [ \t\n\r\f\v]
# 
# * - `\S`
#   - complement of `\s`. Matches any non-whitespace character [^ \t\n\r\f\v]
#   
# * - `\w`
#   - Matches any alphanumeric character. [a-zA-Z0-9_]
# 
# * - `\W`
#   - Complement of `\w`
#   
# * - `\A`
#   - Matches only at the start of a string
#   
# * - `\Z`
#   - Matches only at the end of a string`
#   
# * - `\b`
#   - Word boundary. Zero-width assertion that matches only at the beginning or end of a word. 
#   A **word** is any sequence of alphanumeric characters. Whitespace or punctuation are delimiters.
#   
# * - `\B`
#   - Only matches when not at word boundary
#   
# * - `^`
#   - Matches at the beginning of string, unless re.M specified, then at beginning of each new line
#   
# * - `$`
#   - Matches at end of string, unless re.M specified, then right before newlines. 
# 
# ```
# 
# (repeating)=
# ### Repeating Chars (*) , (+) , (?)
# 
# - {ref}` * <asterisk>`
# - {ref}` + <plus>`
# - {ref}` ? <question>`
# - {ref}` {m,n} <bounds>`
# 
# 
# (asterisk)=
# #### *  , 0 or more times repetition
# 
# The `*` character specifies that that character or character block the precedes it can be matched **0 or more times**.
# 
# For example, `ca*t`  will match `ct`, `cat`, and `ca...at`
# 
# It can also be used on character class blocks: `a[bcd]*d`
# 
# It is greedy and will search for as many repetitions as possible before scaling back to 0.
# 
# (plus)=
# #### +  , 1 or more times repetition
# 
# The `+` character is the same as `*` except it must match **1 or more times**
# 
# (question)=
# #### ?   , must match either 0 or 1 time.
# 
# Can think of it as designating something as optional. For example,
# 
# `home-?brew ` will match either ` home-brew ` or ` homebrew`
# 
# (bounds)=
# #### {m,n}  , $m, n \in \mathcal{Z}$ lower and upper bound on matching
# 
# Necessitates that a char or char block matches at least m times but not more than n times: $m\leq \text(matches) \leq n$
# 
# `a\{1,3}b ` matches ` a\b `, ` a\\b `, and ` a\\\b`
# 
# 

# (using)=
# ### Using Regular Expressions
# 
# The `re` module provides an interface to the regular expresssion engine that allows us to compile RE's into objects and then perform
# matching operations on them
# 
# 
# The basic idea is something like this:
# 
# ````{margin}
# ```{note}
# Using the python raw string formatting keeps the text as clean as possible
# ```
# ````
# 
# ```python
# import re
# p = re.compile(r'ab*')
# 
# # or, to ignore case
# p = re.compile(r'ab*', re.IGNORECASE)
# ```
# (patterns)=
# ### Pattern Objects and Matching Operations
# 
# Regular expressions are compiled into pattern objects which then allows us to perform matching operations upon them.  
# 
# Here are some of the most common methods that take the form `p.method()`
# 
# ```{list-table}
# :header-rows: 1
# 
# * - Syntax
#   - Description
# 
# * - `match()`
#   - Determines if the RE matches at the beginning of a string
#   
# * - `search()`
#   - Scans through a string looking for any location where RE matches
#   
# * - `findall()`
#   - Finds all substrings where RE matches and returns it as a list
# 
# * - `findter()`
#   - Finds all substrings where RE matches and returns it as an iterable
# 
# ```
# 
# So running something such as:
# 
# ```python
# p = re.compile(r'regex')
# m = p.match('string')
# ```
# 
# will create a match object that is `None` type if no match is found.
# 
# Here are some useful `match()` attributes/methods:
# 
# ```{list-table}
# :header-rows: 1
# 
# * - Syntax
#   - Description
# 
# * - `group()`
#   - Returns the string matched by RE
#   
# * - `start()`
#   - Returns the starting index position of first letter in match
#   
# * - `stop()`
#   - Returns the (ending position index + 1) of match
# 
# * - `span()`
#   - returns a tuple containing start(), stop() values
# 
# ```
# 
# Here is the general structure of a match program:
# 
# ```python
# p = re.compile( ... )
# m = p.match( 'string goes here' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')
# ```    
# 
# 
# 

# (flags)=
# ### Compilation Flags (re.<>)
# 
# `````{margin}
# ````{note}
# He is the format for these flags, bitwise OR `|`
# can be used to chain multiple flags
# ```python
# p = re.complile(regex, re.A | re. I)
# ```
# ````
# `````
# 
# ```{list-table} Table of Available Flags
# :header-rows: 1
# 
# * - Syntax
#   - Description
# 
# * - `ASCII, A`
#   - Makes several escapes like \w, \b, \s, \d match only on ASCII characters with the correspnding
#   properties
#   
# * - `DOTALL, S`
#   - Makes ` . ` match any character, **including newlines** 
#   
# * - `IGNORECASE, I`
#   - Runs case-insensitive matches
# 
# * - `LOCALE, L`
#   - Do a locale-aware match. Helps with writing programs that account for language-alphabetic symbolic diff.
#   
# * - `MULTILINE, M`
#   - breaks up a string with newlines `\n` into multiple strings affecting the `^` and `$` metacharacters
# 
# * - `VERBOSE, X`
#   - This flag allows you to write regular expressions that are more readable by granting you more
#   flexibility in how you can format them
# 
# ```
# 
# 
