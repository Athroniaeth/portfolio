@echo off
poetry run ruff format || exit 0
poetry run ruff check --statistics