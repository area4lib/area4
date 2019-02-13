#!/usr/bin/env bash
python3 -m pip install --upgrade --user setuptools wheel twine
cd ../
python3 setup.py sdist bdist_wheel
