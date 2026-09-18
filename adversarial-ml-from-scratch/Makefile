.PHONY: setup test lint clean

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt && pip install -e .

test:
	pytest -v

lint:
	black --check src tests
	flake8 src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
