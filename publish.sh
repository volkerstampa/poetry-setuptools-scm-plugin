#!/usr/bin/env -S bash -eu -o pipefail

PypiRepository="$1"

if [[ "$PypiRepository" == "testpypi" ]]
then
  poetry config repositories.testpypi https://test.pypi.org/legacy/
fi
poetry config pypi-token."$PypiRepository" "$PYPI_TOKEN"
if [[ "$PypiRepository" == "testpypi" ]]
then
  poetry --no-interaction publish -build --repository "$PypiRepository"
else
  poetry --no-interaction publish  --build
fi
