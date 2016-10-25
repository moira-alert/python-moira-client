
PYTHON=python
PYTHONPATH=./
SOURCE_DIR=./
TESTS_DIR=./tests

all: help

help:
	@echo "install      - install python package"
	@echo "test         - run tests"
	@echo "test-deps    - install test dependencies"

install:
	$(PYTHON) setup.py install

test:
	$(PYTHON) -m unittest discover $(TESTS_DIR) -v

deps:
	pip install -r ./requirements.txt

test-deps:
	pip install -r ./test-requirements.txt
