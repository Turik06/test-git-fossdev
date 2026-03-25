PYTHON := .venv/bin/python3
PIP := .venv/bin/pip3
INSTALLED_FLAG := .venv/.installed


$(INSTALLED_FLAG): requirements.txt
	@python3 -m venv .venv
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@touch $(INSTALLED_FLAG)
	@echo "Environment is ready"

.PHONY: run

run: $(INSTALLED_FLAG)
	@$(PYTHON) src/app.py

.PHONY: clear
clear:
	@
	@rm -rf .venv
	@echo "Virtual environment removed"