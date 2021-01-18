(conda)=
# Conda Commands

[conda commdads][cc]



(conda-quickref)=
## Quick References for this Page

- {ref}`condaclean`
- {ref}`condaconfig`
- {ref}`condacreate`
- {ref}`condainfo`
- {ref}`condainstall`
- {ref}`condalist`
- {ref}`condapackage`
- {ref}`condaremove`

(condaclean)=
### conda clean

Removes unused packages and cache. Some popular options listed below.

```bash
conda clean [-h] [-a] [-i] [-p] [-t] [-f] [-c TEMPFILES [TEMPFILES ...]] [-d] [--json] [-q] [-v] [-y]
```

```{list-table}
:header-rows: 1

* - Options
  - Description
  
* - `-a`, `--all`
  - Removes index cache, lock files, unused cache packages, and tarballs.

* - `-p`, `--packages`
  - Removes unused packages
  
* - `-y`, `--yes`
  -  Do not ask for confirmation  
  
```  

(condaconfig)=
## conda config

Modifies values in .condarc. Writes to the user .condarc file (/home/docs/.condarc) by default.

```bash
conda config [-h] [--json] [-v] [-q] [--system | --env | --file FILE] [--show [SHOW [SHOW ...]] | --show-sources | --validate |
             --describe [DESCRIBE [DESCRIBE ...]] | --write-default]
```

```{list-table}
:header-rows: 1

* - Options
  - Description
```

(condacreate)=
## conda create

Creates a new environment from a list of specified pacakges.

```bash
conda create [--clone ENV] [-n ENVIRONMENT | -p PATH] [-c CHANNEL] [--use-local] [--override-channels]
             [--repodata-fn REPODATA_FNS] [--strict-channel-priority] [--no-channel-priority] [--no-deps | --only-deps]
             [--no-pin] [--copy] [-C] [-k] [--offline] [-d] [--json] [-q] [-v] [-y] [--download-only] [--show-channel-urls]
```             

```{list-table}
:header-rows: 1

* - Options
  - Description
```

(condainfo)=
## conda info

Displays information about a current conda install.


```bash
conda info [--json] [-v] [-q] [-a] [--base] [-e] [-s] [--unsafe-channels]
```

```{list-table}
:header-rows: 1

* - Options
  - Description
  
* - `-a`, '-all'
  - Show all information

* - `-e`, `--envs`
  - Lists all known conda environments
  
* - `--base`
  - Displays base environment path
  
* - `-s`, `--system`
  - Lists environment variables
```

(condainstall)=
## conda install



(condalist)=
## conda list


(condapackage)=
## conda package


(condaremove)=
## conda remove
[cc]: https://docs.conda.io/projects/conda/en/latest/commands.html





