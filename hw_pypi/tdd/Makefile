.PHONY: build publish clean test

test:
	.venv/bin/pytest tests/

build:
	.venv/bin/python -m build

publish: build
	.venv/bin/python -m twine upload --repository testpypi dist/*

clean:
	rm -rf build dist *.egg-info .pytest_cache src/*/__pycache__ tests/__pycache__