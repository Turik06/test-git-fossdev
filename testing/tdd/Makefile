create-structure:
	mkdir src test docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep
	
install-dep:
	pip install -r requirements.txt

build:
	pip install -e

test-pytest:
	python3 -m pytest

create-evn:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

test: create-evn install-dep install test-pytestmke

