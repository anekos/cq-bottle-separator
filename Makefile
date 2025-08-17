.PHONY: watch
watch:
	axe src/**/*.py -- uv run bottle-separator -- build --show
