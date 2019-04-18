# area4 Makefile

dist: clean
	bash tools/build-package.sh
.PHONY: dist

clean:
	rm -rf build dist area4.egg-info MANIFEST
.PHONY: clean

beta:
	python3 -m pip install .
.PHONY: beta

safetyci:
	find ./requirements/ -name \*.txt -exec python3 -m safety check --full-report -r {} \;
.PHONY: safetyci

zip:
	python3 setup.py sdist --formats=zip
.PHONY: zip
