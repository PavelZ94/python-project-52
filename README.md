# Task Manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/PavelZ94/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/PavelZ94/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/fbbb7d77cdca600f1e86/maintainability)](https://codeclimate.com/github/PavelZ94/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fbbb7d77cdca600f1e86/test_coverage)](https://codeclimate.com/github/PavelZ94/python-project-52/test_coverage)
[![Lint_check](https://github.com/PavelZ94/python-project-52/actions/workflows/lint_check.yml/badge.svg)](https://github.com/PavelZ94/python-project-52/actions)

## About

Task Manager is a task management system. It allows you to set tasks, assign performers and change their statuses. To work with the system, registration and authentication are required.
You can also set the statuses and labels on your tasks, set the executors.

## Stack

To install and use an application you should have:
- python = ">=3.10,<4.0"
- python-dotenv = "^1.0.1"
- dj-database-url = "^2.2.0"
- django = "^5.0.6"
- gunicorn = "^22.0.0"
- psycopg2-binary = "^2.9.9"
- django-bootstrap5 = "^24.2"
- django-crispy-forms = "^2.1"
- flake8 = "^7.1.0"
- django-extensions = "^3.2.3"
- django-filter = "^24.2"
- rollbar = "^0.16.3"
- coverage = "^7.5.4"

## Installation

Make sure you installed the latest versions of all programs before using application. To install programs you should use this command:

```pip install "name of program"```

To check version of program use this command:

```"name of program" --version```

After you are sure that all programs are installed follow these steps:
1) Clone The repository to your local machine:

```git clone git@github.com:PavelZ94/python-project-52.git```

```cd python-project-52```

2) Next you should install necessary dependencies:

```make install```

3) Create an .env file in the root directory according to the example: ```.env-example```

## Usage

To launch the application use command:
```
make start
```
It will launch application on default host and port: http://0.0.0.0:8000/

Also, you can launch it in development mode with debugger active using:
```
make dev
```

This case it will be launched http://127.0.0.1:5432/ as default if you used parameters `'localhost'` and port `'5432'` in .env file above.

In application you should firstly register and log in.
Then, you can create tasks, task execution statuses, labels of tasks, put the descriptions of your tasks.
Also you can change these options, delete unnecessary tasks, statuses, labels.

## The result of deploy:
https://python-project-52-8cz8.onrender.com

