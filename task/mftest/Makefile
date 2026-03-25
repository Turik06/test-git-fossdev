PYTHON := .venv/bin/python3.12
PIP := .venv/bin/pip3.12
INSTALLED_FLAG := .venv/.installed


$(INSTALLED_FLAG): requirements.txt
	@python3.12 -m venv .venv
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@$(PIP) install deptry
	@touch $(INSTALLED_FLAG)
	@echo "Environment is ready"

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