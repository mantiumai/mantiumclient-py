test: lint test_only


test_only: 
	pytest -svx --cov-report term-missing --cov-report html --cov-branch --cov mantiumapi/


lint:
	@echo
	isort --diff -c --skip-glob '*.venv' .
	@echo
	blue --check --diff --color .
	@echo
	# flake8 .
	@echo
	# mypy --ignore-missing-imports .
	@echo
	# bandit -r mantiumapi


format:
	isort .
	blue .

