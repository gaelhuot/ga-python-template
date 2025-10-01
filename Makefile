.PHONY: help install test lint format clean run dev prod

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=app --cov-report=html

lint: ## Run linting
	flake8 app tests
	mypy app

format: ## Format code
	black app tests
	isort app tests

format-check: ## Check code formatting
	black --check app tests
	isort --check-only app tests

clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/

run: ## Run the application
	python run.py

dev: ## Run the application in development mode
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

prod: ## Run the application in production mode with Gunicorn
	gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --keep-alive 5 --graceful-timeout 20 --access-logfile - --error-logfile - app.main:app

all-checks: format lint test ## Run all quality checks
