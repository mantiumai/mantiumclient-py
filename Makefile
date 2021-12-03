test: lint test_only


test_only: 
	pytest -svx --cov-report term-missing --cov-report html --cov-branch --cov mantiumapi/


lint:
	@echo
	isort --diff -c --skip-glob '*.venv' .
	@echo
	blue --check --diff --color .
	@echo
	flake8 . || true
	@echo
	mypy --ignore-missing-imports . || true
	@echo
	bandit -r mantiumapi || true


format:
	isort .
	blue .

