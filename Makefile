MODULE_DIR:=panktikhata
MAIN_SCRIPT:=$(MODULE_DIR)/main.py
RESOURCES_FILE:=$(MODULE_DIR)/resources.qrc
RESOURCES_OUTPUT:=$(MODULE_DIR)/assets/resources.py
PY_EXE:=python

all: rc run

rc:
	poetry run pyside6-rcc $(RESOURCES_FILE) -o $(RESOURCES_OUTPUT)

run:
	poetry run python $(MAIN_SCRIPT)

flake8:
	poetry run flake8

black:
	poetry run black panktikhata/
