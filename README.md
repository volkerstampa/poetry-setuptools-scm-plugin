# Poetry Setuptools SCM Plugin

poetry-setuptools-scm-plugin is a [Poetry](https://python-poetry.org/) plugin that uses
[setuptools_scm](https://github.com/pypa/setuptools_scm) to extract a package version from [git](https://git-scm.com/)
or [Mercurial](https://www.mercurial-scm.org/) metadata.

## Installation

Add the plugin to Poetry:

```bash
poetry self add poetry-setuptools-scm-plugin
```

## Usage

To enable it in your Poetry-based project add the following to your `pyproject.toml`:

```toml
[tool.setuptools_scm]
```

With this the version specified in `version` of the `tool.poetry` section in `pyproject.toml` is ignored and
the version derived by `setuptools_scm` is used instead. See [its documentation](https://setuptools-scm.readthedocs.io/)
on further configuration options.

> [!NOTE]
> The Poetry team believes
> ["that the version is one of the static metadata and the pyproject.toml is the single source of truth for it"](https://github.com/python-poetry/poetry/issues/4971#issuecomment-1013930810).

## Similar tools

- [poetry-version-plugin](https://github.com/tiangolo/poetry-version-plugin/):
  This plugin allows to read the version either from a git tag or a version definition in an `__init__.py` file. To my
  latest knowledge it cannot derive dev-versions from git.
- [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning):
  Instead of using
  setuptools_scm this plugin utilizes [Dunami](https://github.com/mtkennerly/dunamai) which
  comes with even more features than setuptools_scm.

## Development

### Prerequisites

- Python >=3.10, can for example be installed with [pyenv](https://github.com/pyenv/pyenv):

  ```bash
  pyenv install 3.10
  pyenv local 3.10
  ```

- [Poetry](https://python-poetry.org/docs/#installation) >=1.2

- the latest release of the plugin installed in poetry
  ```bash
  poetry self add poetry-setuptools-scm-plugin
  ```

### Setup

```bash
poetry install
```

To simplify running commands in the Poetry environment:

```bash
poetry shell
```

The following section assume that the commands are executed from such a Poetry shell.

### Test

```bash
pytest
```

### Check

```bash
ruff check
```

### Build

```bash
poetry build
```
