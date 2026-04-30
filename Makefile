.DEFAULT_GOAL := help
PRODUCT_SERVICE_URL ?= http://127.0.0.1:8001
PRODUCT_SERVICE_PORT ?= 8001
ORDER_SERVICE_PORT ?= 8002

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)
	@echo "Practice removed"

help:
	@echo "This makefile for repo-level activity"
# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md
run-product:
	cd product_service && poetry run uvicorn src.app.main:app --host 127.0.0.1 --port $(PRODUCT_SERVICE_PORT)

run-order:
	powershell -Command "cd order_service; $$env:PRODUCT_SERVICE_URL='$(PRODUCT_SERVICE_URL)'; poetry run uvicorn src.app.main:app --host 127.0.0.1 --port $(ORDER_SERVICE_PORT)"