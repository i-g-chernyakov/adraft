#!/usr/bin/env bash

VENV=./venv

virtualenv --python=python3.5 --quiet --no-site-packages $VENV
chmod +x $VENV/bin/activate
. $VENV/bin/activate

pip install -r requirements_test.txt

py.test
