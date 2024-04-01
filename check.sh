#!/usr/bin/env -S bash -eu -o pipefail

pytest
ruff check
poetry build
