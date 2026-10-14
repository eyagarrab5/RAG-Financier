.PHONY: install test api

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

api:
	uvicorn api.main:app --reload
