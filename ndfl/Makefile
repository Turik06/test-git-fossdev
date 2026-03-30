# Makefile

.PHONY: install test build publish clean

install:
	pip install -e .[dev]

test:
	pytest tests/

build: clean
	python -m build

publish: build
	python -m twine upload --repository testpypi dist/*

clean:
	rm -rf dist/ build/ src/*.egg-info .pytest_cache/