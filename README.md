Poetry Setuptools SCM Plugin
============================

poetry-setuptools-scm-plugin is a [Poetry](https://python-poetry.org/) plugin that uses 
[setuptools_scm](https://github.com/pypa/setuptools_scm) to extract a package version from [git](https://git-scm.com/) 
or [Mercurial](https://www.mercurial-scm.org/) metadata.

# Installation

Execute the following in your Poetry-based project:

```bash
poetry self add poetry-setuptools-scm-plugin
```

To prevent warnings from setuptools_scm also add the following to your `pyproject.toml`:

```toml
[tool.setuptools_scm]
```

With this the version specified in `version` of the `tool.poetry` section in `pyproject.toml` is ignored and
the version derived by `setuptools_scm` is used instead. See [its documentation](https://setuptools-scm.readthedocs.io/)
on further configuration options.

# Development

## Prerequisites

- Python >=3.10, can for example be installed with [pyenv](https://github.com/pyenv/pyenv):
   ```bash
   pyenv install 3.10
   pyenv local 3.10
   ```

- [Poetry](https://python-poetry.org/docs/#installation) >=1.2

## Setup

```bash
poetry install
```

To simplify running command in the Poetry environment:

```bash
poetry shell
```

## Test

```bash
pytest
```

## Check

```bash
ruff check
```

## Build

´´´bash
poetry build
poetry publish
```
