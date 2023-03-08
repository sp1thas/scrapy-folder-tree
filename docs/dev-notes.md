# Development

## Workflow

This project uses the Github Flow.

![The Github flow](static/githubflow.png)

## Dev Environment

Navigate in the project's root folder and run:

```shell
poetry install --dev
```

Make sure that poetry and pre-commit is already installed.

## Static analysis

The project is static analysed using the following tools:

 - isort
 - mypy
 - black

as pre-commit hooks:

```shell
pre-commit run --all-files
```