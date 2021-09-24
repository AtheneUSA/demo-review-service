# Demo Review Service

This repository serves as a demo for several Python libraries and design best practices as part of Athene Advance 2021.

## Features

- [FastAPI](https://fastapi.tiangolo.com/) Python web framework
- [SQLModel](https://sqlmodel.tiangolo.com/) Python SQL ORM
- [Poetry](https://python-poetry.org/) Python dependency management
- [12 Factor](https://12factor.net/) design principles
- [Black](https://github.com/psf/black) Python code formatter

## Getting Started

Poetry is used to make development easy.
Follow the install instructions for Poetry.
In order to allow your IDE to easily find the python interpreter for the project, instruct Poetry to create the virtual environment in the project directory.
```
poetry config virtualenvs.in-project true
```
Then simply install the project dependencies.
```
poetry install
```

Start the application in development mode
```
poetry run uvicorn fastapi_template.main:app --reload
```
or with the configured run script.
```
poetry run start
```
Note: The reload option should not be configured in production and could be automatically toggled with a DEBUG envvar or similar.
