#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

#* Docker variables
IMAGE := python_star_wars_api_client
VERSION := latest

#* Poetry (For local development without docker)
.PHONY: poetry-download
poetry-download:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	-poetry run mypy --install-types --non-interactive ./

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Formatters
.PHONY: codestyle
codestyle:
	poetry run pyupgrade --exit-zero-even-if-changed --py39-plus **/*.py
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

.PHONY: formatting
formatting: codestyle

#* Linting
.PHONY: test
test:
	poetry run pytest -c pyproject.toml

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml ./
	poetry run black --diff --check --config pyproject.toml ./
	poetry run darglint --verbosity 2 python_star_wars_api_client tests

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml ./

.PHONY: check-safety
check-safety:
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive python_star_wars_api_client tests

.PHONY: lint
lint: test check-codestyle check-safety mypy

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		--build-arg INSTALL_DEV=true \
		--build-arg USER_ID=$$(id -u) \
  	--build-arg GROUP_ID=$$(id -g) \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile \
		--no-cache

.PHONY: docker-run
docker-run:
	@if [[ "$$(docker images -q $(IMAGE):$(VERSION) 2> /dev/null)" == "" ]]; then $(MAKE) docker-build;	fi
	docker run -it --rm \
   -v $$(pwd):/workspace \
   $(IMAGE):$(VERSION)

.PHONY: docker-run-bash
docker-run-bash:
	@if [[ "$$(docker images -q $(IMAGE):$(VERSION) 2> /dev/null)" == "" ]]; then $(MAKE) docker-build;	fi
	docker run -it --rm \
   -v $$(pwd):/workspace \
   $(IMAGE):$(VERSION) bash

.PHONY: docker-run-test
docker-run-test:
	@if [[ "$$(docker images -q $(IMAGE):$(VERSION) 2> /dev/null)" == "" ]]; then $(MAKE) docker-build;	fi
	docker run -it --rm \
   -v $$(pwd):/workspace \
   $(IMAGE):$(VERSION) make test

.PHONY: docker-run-lint
docker-run-lint:
	@if [[ "$$(docker images -q $(IMAGE):$(VERSION) 2> /dev/null)" == "" ]]; then $(MAKE) docker-build;	fi
	docker run -it --rm \
   -v $$(pwd):/workspace \
   $(IMAGE):$(VERSION) bash -c "poetry run mypy --install-types --non-interactive ./ && make lint"

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	@docker rmi -f $(IMAGE):$(VERSION) 2> /dev/null

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove docker-remove
