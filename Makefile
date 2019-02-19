clean:
	-rm -rf build dist area4.egg-info
	-find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

dist: clean
        chmod +x tools/build-package.sh
	bash tools/build-package.sh
.PHONY: dist

test:
	python3 test-code.py
.PHONY: test
