# area4 Makefile

default:
	echo "Silly, the make command requires which function you want to run."
.PHONY: default Makefile

clean:
	-rm -rf build dist area4.egg-info area4.dist-info node_modules
	-find . *.pyc -exec rm {} \;
	-find . *.pyo -exec rm {} \;
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

beta:
	python3 -m pip install .
.PHONY: beta

safetyci:
	python3 -m safety check --full-report -r requirements/dev.txt
	python3 -m safety check --full-report -r requirements/test.txt
.PHONY: safetyci

markdownlint:
	markdownlint --config=.markdownlint.yml *.md
	markdownlint --config=.markdownlint.yml .github/*.md
	markdownlint --config=.markdownlint.yml .github/ISSUE_TEMPLATE/*.md
	markdownlint --config=.markdownlint.yml extras/*.md
.PHONY: markdownlint
