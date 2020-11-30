.PHONY: format test lint run watch

export PYTHONPATH=.


all: lint test run

format:
	black app tests

test:
	pytest --cov=app tests/

lint:
	flake8 app/ tests/

run:
	python app/main.py

watch:
	find . -path ./venv -prune -false -o -name "*.py" | entr python -m pytest -vv --cov-report html --cov=app tests/

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete