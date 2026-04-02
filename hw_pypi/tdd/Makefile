.PHONY: venv build publish clean test
all: venv test
test: venv
	.venv/bin/pytest tests/

build: venv
	.venv/bin/python3 -m build

publish: build
	.venv/bin/python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf build dist *.egg-info .pytest_cache src/*/__pycache__ tests/__pycache__ ./.venv

venv:
	python3.12 -m venv .venv
	.venv/bin/pip3 install pytest build twine
	.venv/bin/pip3 install -e .