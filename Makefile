# Makefile

PACKAGE_NAME = "smoothprogressbar"
PACKAGE_DIR = $(PACKAGE_NAME)
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    user : make install                   install the packages'
	@echo '           make uninstall                 remove the package'
	@echo '    dev  : make venv                      install venv'
	@echo '           source venv/bin/activate       activate venv'
	@echo '           make dev                       install as dev'
	@echo '           make doc                       make the README'
	@echo '           make test                      test'
	@echo '           make stubs                     refresh stubs'
	@echo

venv:
	@pip3 install virtualenv --user
	@virtualenv venv

dev:
	@pip3 install -e ".[dev]"

install:
	@pip3 install . --upgrade

uninstall:
	@pip3 uninstall -y $(PACKAGE_NAME)

doc:
	@pyreverse src/$(PACKAGE_NAME) -ASmy -o mmd -p $(PACKAGE_NAME) -d doc

docstring2md:
	@export_docstring2md -p $(PACKAGE_DIR) --output-file README.md -mmd doc/classes_smoothprogressbar.mmd -tml pyproject.toml -td doc/todo.md --toc

test:
	@pytest --pyargs $(PACKAGE_NAME)

publish:
	@pytest --pyargs $(PACKAGE_NAME)
	@git add .
	@git commit
	@git push

.PHONY: default init dev install uninstall doc stubs test example publish
