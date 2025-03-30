.PHONY: all
all: build

.PHONY: clean
clean:
	rm -rf dist/ build/ *.egg-info

.PHONY: build
build: clean
	python -m build

.PHONY: upload
upload: build
	twine upload dist/*

.PHONY: install
install: build
	pip install dist/*.whl