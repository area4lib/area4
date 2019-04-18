# area4 Makefile

dist: clean
	chmod +x tools/build-package.sh
	bash tools/build-package.sh
	chmod -x tools/build-package.sh
.PHONY: dist

clean:
	rm -rf build dist area4.egg-info area4.dist-info MANIFEST
.PHONY: clean

test:
	python3 tests.py
.PHONY: test

beta:
	python3 -m pip install .
.PHONY: beta

safetyci:
	find ./requirements/ -name \*.txt -exec python3 -m safety check --full-report -r {} \;
.PHONY: safetyci

zip:
	python3 setup.py sdist --formats=zip
.PHONY: zip
