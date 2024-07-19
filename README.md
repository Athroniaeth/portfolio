<div align="center">
    <h1 style="font-size: xx-large; font-weight: bold;">Portfolio</h1>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.12-0">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/License-MIT-f">
    </a>
    <br>
</div>

Pierre Chaumont's portfolio using FastAPI (Python) on the back-end and Tailgrids on the front-end (HTML, Tailwinds).

## Installation

This project uses Miniconda and Poetry for dependency management. To install the dependencies, run the following command:

```bash
poetry install
```

## Usage

To run the project, use the following commands:

```bash
python src
```

## Contribution

To install the development dependencies, run:

```bash
poetry install --dev
```

To add a new dependency, use:

```bash
poetry add <dependency>
```

For development-specific dependencies, use:

```bash
poetry add --group dev <dependency>
```

To activate pre-commit hooks, run:

```bash
poetry run pre-commit install
```

## Structure

```bash
├── README.md         # The file you are currently reading
├── htmlcov           # The coverage report folder
├── pyproject.toml    # The poetry configuration file
├── ruff.toml         # The ruff configuration file (linter, formatter)
├── scripts           # Scripts useful for the project (no CI/CD)
├── src               # The source code folder
│   ├── __init__.py   # Can add global variables
│   ├── __main__.py   # The entry point of the project
└── tests             # The tests folder (pytest)
```
