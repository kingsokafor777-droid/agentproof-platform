.PHONY: validate check

validate:
	python3 scripts/validate_docs.py

test:
	python3 -m unittest discover -s tests -v

check: validate test
