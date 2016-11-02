.SILENT:

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

tests: clean
	py.test -s -vvvv tests/

setup-local:
	pip install -U pip
	pip install -r requirements-dev.txt
