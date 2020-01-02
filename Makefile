dist: clean
	bash build-package.sh
.PHONY: dist

clean:
	rm -rf build dist area4.egg-info MANIFEST __pycache__ area4/__pycache__ .mypy_cache
.PHONY: clean

beta: clean
	python3 -m pip install .
.PHONY: beta
