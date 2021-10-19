# PyDRS - Sirius Power Supplies communication.

![Linting and Static](https://github.com/lnls-sirius/pydrs/actions/workflows/lint.yml/badge.svg)
![Latest tag](https://img.shields.io/github/tag/lnls-sirius/pydrs.svg?style=flat)
[![Latest release](https://img.shields.io/github/release/lnls-sirius/pydrs.svg?style=flat)](https://github.com/lnls-sirius/pydrs/releases)
[![PyPI version fury.io](https://badge.fury.io/py/pydrs.svg)](https://pypi.python.org/pypi/pydrs/)
[![Read the Docs](https://readthedocs.org/projects/spack/badge/?version=latest)](https://lnls-sirius.github.io/pydrs/)

Development packages are listed at [requirements-dev.txt](requirements-dev.txt) and runtime dependencies at [requirements.txt](requirements.txt).

## Conda

As an option, Conda can be used to create a specific environment where PyDRS library can be installed.
Conda can be installed with [**miniconda**](https://docs.conda.io/en/latest/miniconda.html#miniconda) or [**anaconda**](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

```command
conda create --name pydrs python=3.6
conda activate pydrs
```

## Dev Utility scripts

```sh
sh ./scripts/clean.sh
```
## Pypi

In the chosen environment, PyDRS installation can be proceeded through PIP package manager.
Note: If you do not have pip installed, you can download and install it from here: [**pip**](https://pypi.org/project/pip/)

```command
pip install pydrs
``` 
