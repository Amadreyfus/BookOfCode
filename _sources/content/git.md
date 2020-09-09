(git)=
# Git

[Pro Git Book](https://git-scm.com/book/en/v2)

[Git Documentation](https://git-scm.com/docs)

(git_commands)=
## Git Commands

```{list-table}
:header-rows: 1

* - Git Command
  - Description

* - `git clone`
  - Clone a repository into a new directory

* - `git fetch`
  - Syncs a local repository with remote repository importing unique remote commits and updating local-remote representation

* - `git push <origin> <master>`
  - Uploads local changes to a remote repo and updates the remote repo with new commits
  
* - `git pull`
  - Command that fetches remote changes and updates them

* - `git add <-A>`
  - Stages the changes made to a repo and gets them ready for commit
  
* - `git status`
  - Lets you know the status of the repo/div you are currently in

* - `git diff`
  - Will show changes/differences between files in commit and their present state.
  
* - `git config --global user.username <name>`
  - Adds Github username to git
  
* - `git remote add <remotename> <url>`
  - Adds remote connections to a local repository
  
* - `git remote set-url <remotename> <url>`
  - Can set or reset a url location for a named remote repo
  
* - `git pull <remotename> <branch>`
  - Pull in changes to a local repo from a branch in remote
 
* - `git remote -v`
  - View remote addresses

* - `git commit -m "message"`
  - Applies commit to current branch of repository

* - `git branch <newBranch>`
  - Creates a new branch
  
* - `git checkout <name>`
  - Checks out an object, establishes where you are in terms of git
  
* - `git checkout -b <name>`
  - Creates a new branch and checks it out simultaneously

* - `git merge <desiredbranch>`
  - Merges desired branch with currently checked out branch. **It moves the checked out branch**
  
* - `git rebase <where_to_move> <what_to_move>`
  - Moves all work from one branch onto another sequentially, without merging.
  
* - `git checkout HEAD^`
  - Uses relative reference to move to the parent of HEAD.

* - `git checkout <branch>^`
  - Moves up one from current branch

* - `git checkout <object>~<n>`
  - Specifies how far back in ancestry you want to go
  
* - `git cherry-pick <commit1> <commit2> ...`
  - Copies a series of commits to below current location

* - `git describe <object>`
  - Describes where you are relative to closes anchor (tag)

```  
(emojis)=
## Git Commit Message Emojis

```{note}
Using <kbd>Win</kbd>+<kbd>.</kbd> will pull up the Emoji Keyboard on Windows
```

Commit Type | Emoji
----------  | -----
Initial Commit | [🎉 Party Popper](http://emojipedia.org/party-popper/)
Version Tag | [🔖 Bookmark](http://emojipedia.org/bookmark/)
Content Update | [📝 Memo](https://emojipedia.org/memo/) 
New Feature | [✨ Sparkles](http://emojipedia.org/sparkles/)
Bugfix | [🐛 Bug](http://emojipedia.org/bug/)
Security Fix | [🔒 Lock](https://emojipedia.org/lock/)
Metadata | [📇 Card Index](http://emojipedia.org/card-index/)
Refactoring | [♻️ Black Universal Recycling Symbol](http://emojipedia.org/black-universal-recycling-symbol/)
Documentation | [📚 Books](http://emojipedia.org/books/)
Internationalization | [🌐 Globe With Meridians](http://emojipedia.org/globe-with-meridians/)
Accessibility | [♿ Wheelchair](https://emojipedia.org/wheelchair-symbol/)
Performance | [🐎 Horse](http://emojipedia.org/horse/)
Cosmetic | [🎨 Artist Palette](http://emojipedia.org/artist-palette/)
Tooling | [🔧 Wrench](http://emojipedia.org/wrench/)
Tests | [🚨 Police Cars Revolving Light](http://emojipedia.org/police-cars-revolving-light/)
Tests | [🧪 Test Tube](https://emojipedia.org/test-tube/)
Deprecation | [💩 Pile of Poo](http://emojipedia.org/pile-of-poo/)
Removal | [🗑️ Wastebasket](http://emojipedia.org/wastebasket/)
Work In Progress (WIP) | [🚧 Construction Sign](http://emojipedia.org/construction-sign/)