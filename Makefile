test:
	make unit-test
	make flake8

unit-test:
	python -m unittest discover -s ./tests/  -p "test_*.py"

flake8:
	# I want to specify all files at once but I couldn't resolve it
	flake8  app/*/*.py *.py tests/*/*.py
