clean:
	-rm -rf build dist area4.egg-info
	-find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

dist: clean
	bash tools/build-package.sh
.PHONY: dist

test:
	python test-code.py
.PHONY: test
