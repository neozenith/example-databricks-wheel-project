# Databricks / PySpark Dev Workflow

This project prototypes 2 types of dev workflows to go beyond using just notebooks.

 - Testing locally with `pytest` and `pyspark`
 - Integration testing deploying wheels to Databricks and using `databricks-cli` to trigger the job.

## Quick Start

You will need to setup and configure your Personal Access Token (PAT) for 
[`databricks-cli`](https://docs.databricks.com/dev-tools/cli/index.html).

```sh
# This installs dependencies and could take a while
poetry shell

# Run local testing
inv test

# Build wheel and upload to databricks
inv build
inv db.upload --profile dev --artifact-path 'dbfs:/FileStore/wheels/'

# Reinstall wheel on cluster
inv db.reinstall --profile dev --cluster-id 0307-061523-vrvjuz1j --wheel 'dbfs:/FileStore/wheels/projectname-0.1.0-py3-none-any.whl'

# You will need to manually create a new job on databricks and get the job-id
# TODO add task and job template to automate this too.
inv db.go --profile dev --job-id 1234
```

## Lifecycle Tasks

This project utilises a combination of the following tools for dev automation:
 - [`poetry`](https://python-poetry.org/)
   - `poetry` is exceptional at dependency management, building wheels and setting up virtual envs.
 - [`invoke`](https://www.pyinvoke.org/)
   - `invoke` uses a plain `tasks.py` python file to define our custom tasks and CLI args.
   - It can also chain tasks together as `pre` and `post` dependencies.
   - It has a neat interface to `run` shell tasks and capture the `stdout` for processing into other tasks.
   - Full power of Python for task automation available.

```sh
$ poetry shell
(.venv)$ inv --list
Available tasks:

  all            Custom databricks flow.
  build          Build wheel.
  format         Autoformat code for code style.
  lint           Linting and style checking.
  test           Run test suite.
  db.go          Trigger default job associated for this project.
  db.reinstall   Reinstall version of wheel on cluster with a restart.
  db.upload      Upload wheel artifact to DBFS.

Default task: test
```
