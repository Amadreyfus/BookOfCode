(magic)=
# Magic Commands in Ipython

<br />

**Quick Reference Links to Page Content**

- {ref}`bookmark`
- {ref}`cd`
- {ref}`config`
- {ref}`history`
- {ref}`macro`
- {ref}`timeit`
- {ref}`Table of Magic Commands <magic_table>`
- {ref}`Table of Magic Commands for Cells <cell_table>`

(bookmark)=
## `<%bookmark>`  Bookmarks  

Creates a bookmark, which is essentially a reference to a path location

`%bookmark <name>       ` Creates a bookmark to current directory  
`%bookmark <name> <dir> ` Creates a bookmark to chosen directory  
`%bookmark -l           ` Lists all bookmarks in the workspace  
`%bookmark -d <name>    ` Removes a specific bookmark  
`%bookmark -r           ` Removes all bookmarks

(cd)=
## `<%cd>`  Changing Working Directory  

Allows you to change your working directory for inputting and outputting files

The magic command **%dhist** can provide a nicely formatted list of directories visited during a session

`cd -b <bookmark_name> ` If the bookmark is unique in the namespace, -b is not required, but it allows for tab completion  
`cd                    ` Will change directory to the root directory  
`cd -                  ` Will change directory to last directory visited  
`cd ..                 ` Will change directory up one level heirarchically   
`cd <path>             ` Will change directory to a specific path  
`cd -<n>               ` Will change directory to the corresponding integer n in the %dhist

(config)=
## `<%config>`  Changing Configuration of Ipython 

`%config                           ` Shows what classes in workspace are configurable  
`%config <class>                   ` Shows what is configurable in the current class  
`%config <class>.<trait> = <value> ` Sets a new configuration value for a trait

(debug)=
## `<%debug>`  Interactive Debugging Environment

`%debug [--breakpoint FILE:LINE] [statement [statement ...]] ` Don't know much about debugging  

(history)=
## `<%history>`  Getting History of Input Commands

`%history          ` Returns the input commands that have been entered in the session  
`-n                ` Prints line numbers for each input  
`-o                ` Also prints the output for each input  
`-p                ` Prints classic >>> prompts before each input  
`-t                ` Prints translated history as python understands it (makes your inputs into explicit code)  
`-f <path\filename>` Writes history to a specificied location, creating a new file with filename  
`-r <range>        ` Places a range on the number of lines displayed  

(macro)=
## `<%macro>`  Create a Macro Using History

Defines a macro for future re-execution. Uses the line numbers of history.

`%macro <name> <n1-n5, n7, n9> ` Where n's are line numbers in your history  
`-r                            ` Use raw input  
`-q                            ` Quiet

(timeit)=
## `<%timeit>` Time Execution of Python Statements

`%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] ` Inline Statement  
`%%timeit                                     ` Cell Statement  
`-n <N>                                       ` Execute given statement N times in a loop.   
`-r <R>                                       ` Number of repititions of N loops. Default: 7  
`-p <P>                                       ` Precision to P digits of time  
`-o                                           ` Returns TimeitResult object

(magic_table)=
## Table of Other Magic Commands

```{list-table}
:header-rows: 1

* - Command
  - Description
  
* - `%quickref`
  - Displays a reference sheet with all magic commands
  
* - `%alias ` and ` %alias_magic ` and ` %unalias`
  - Allows users to create references (aliases) for system commands or lines and cells of code 
  
* - `%dhist`
  - Prints a history of directories visited in a session 
  
* - `%dirs`
  - Returns the current directory stack (files in current directory)
  
* - `%matplotlib [-l] [gui]`
  - Setup matplotlib to work interactively, -l lists all available backends, gui specifies backend

* - `%pip`
  - Run the pip package manager w/in current kernel

* - `%pwd`
  - Displays current working directory
  
* - `reset [-f] [-s] [in] [out] [dhist]`
  - Resets the namespace by removing all names defined by user
  
* - `reset_selective`
  - Allows specification of which named references to remove
  
* - `set_env`
  - Allows user to set environment config and variables
``` 

(cell_table)=
## Cell Magic Commands

```{list-table}
:header-rows: 1

* - Command
  - Description
  
* - `%%bash`
  - Runs cells with bash in a subprocess
  
* - `%%capture`
  - Run the cells, capturing stdout, stderr and IPython richdisplay() cells 
  
* - `%%html`
  - Render the cells as blocks of html 
  
* - `%%javascript ` or ` %%js`
  - Runs the cell as a block of javascript
  
* - `%%latex`
  - Cell run as LateX

* - `%%markdown`
  - Run as markdown

* - `%%perl`
  - perl
  
* - `%%python2`
  - You guessed it.
  
* - `%%ruby`
  - ruby
  
* - `%% writefile [-a] filename`
  - Writes content of cell to a file in pwd
``` 