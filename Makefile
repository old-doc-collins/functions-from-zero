all: install lint test

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	pylint --disable=R,C *.py