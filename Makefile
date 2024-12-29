all: setup lint test

setup:
	pip install -r requirements.txt

test:
	pytest

lint:
	pylint --disable=R,C *.py