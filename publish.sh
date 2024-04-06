#!/usr/bin/env -S bash -eu -o pipefail

PypiRepository="$1"

poetry self add poetry-setuptools-scm-plugin
if [[ "$PypiRepository" == "testpypi" ]]
then
  poetry config repositories.testpypi https://test.pypi.org/legacy/
fi
poetry config pypi-token."$PypiRepository" "$PYPI_TOKEN"
if [[ "$PypiRepository" == "testpypi" ]]
then
  poetry run poetry --no-interaction publish --build --repository "$PypiRepository"
else
  poetry run poetry --no-interaction publish  --build
fi
