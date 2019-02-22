# area4 Makefile
# Used to run tests in CIs

# -- Default command --

default:
	echo "Silly, the make command requires which function you want to run."
.PHONY: default Makefile

# -- area4 commands --

clean:
	-rm -rf build dist area4.egg-info area4.dist-info
	-find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

dist: clean
	chmod +x tools/build-package.sh
	bash tools/build-package.sh
.PHONY: dist

distinfo:
	chmod +x tools/create-dist-info.sh
	bash tools/create-dist-info.sh
.PHONY: distinfo

test:
	python3 code_tests.py
.PHONY: test

testrequirements:
	python3 -m pip install -r requirements/test.txt
.PHONY: testrequirements

devrequirements:
	python3 -m pip install -r requirements/dev.txt
.PHONY: devrequirements

beta:
	python3 -m pip install .
.PHONY: beta

pydocstyle:
	find . -name '*.py' -exec python3 -m pydocstyle --explain --count --source {} \;
.PHONY: pydocstyle

pycodestyle:
	find . -name '*.py' -exec python3 -m pycodestyle --show-source --show-pep8 {} \;
.PHONY: pycodestyle

flake8:
	find . -name '*.py' -exec python3 -m flake8 --show-source --statistics {} \;
.PHONY: flake8

pylint:
	find . -name '*.py' -exec python3 -m pylint {} \;
.PHONY: pylint

# -- MarkdownTests commands --

installlinkcheck:
	npm install -g markdown-link-check@3.7.2
.PHONY: installlinkcheck

installmdlint:
	npm install -g markdownlint-cli
.PHONY: installmdlint

linkcheck:
	find . -name \*.md -exec markdown-link-check {} \;
.PHONY: linkcheck
