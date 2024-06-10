RESOURCES_FILE:=panktikhata/resources.qrc
RESOURCES_OUTPUT:=panktikhata/assets/resources.py

all: rc run

rc:
	poetry run pyside6-rcc $(RESOURCES_FILE) -o $(RESOURCES_OUTPUT)

run:
	poetry run python skhata/
