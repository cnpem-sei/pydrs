#!/bin/sh
set -eux

. ./scripts-dev/clean.sh

python3 -m build
twine upload --repository pydrs dist/*
