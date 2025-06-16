.PHONY: install test

install:
	pip install -r requirements.txt
	pip install pytest

test:
	pytest -q