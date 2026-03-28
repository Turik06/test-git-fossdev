PYTHON := .venv/bin/python3.12
PIP := .venv/bin/pip3.12
MYPY := .venv/bin/mypy
INSTALLED_FLAG := .venv/.installed


$(INSTALLED_FLAG): requirements.txt
	@python3.12 -m venv .venv
# 	@$(PIP) install --upgrade pip
# 	@$(PIP) install -r requirements.txt
# 	@$(PIP) install deptry
	@.venv/bin/python3.12 -m pip install --upgrade pip
	@.venv/bin/python3.12 -m pip install -r requirements.txt
	@.venv/bin/python3.12 -m pip install mypy deptry
	@.venv/bin/python3.12 -m pip install mypy deptry pycodestyle
	@touch $(INSTALLED_FLAG)
	@echo "Environment is ready"

.PHONY: typecheck
typecheck: $(INSTALLED_FLAG)
	@echo "Start type checking"
	@$(MYPY) src/calc.py

.PHONY: lint
lint: $(INSTALLED_FLAG)
	@echo "Start linting"
	@$(PYTHON) -m pycodestyle src/example.py

.PHONY: run

run: $(INSTALLED_FLAG)
	@$(PYTHON) src/app.py


check-deps: $(INSTALLED_FLAG)
	@$(PYTHON) -m deptry src --requirements-files requirements.txt

.PHONY: clear
clear:
	@
	@rm -rf .venv
	@echo "Virtual environment removed"