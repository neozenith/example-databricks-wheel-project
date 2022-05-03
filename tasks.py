# Third Party
from invoke_common_tasks import *  # noqa
from invoke_databricks_wheel_tasks import *  # noqa
from invoke_databricks_wheel_tasks.utils.poetry import poetry_wheelname
from invoke_databricks_wheel_tasks.utils.databricks import default_dbfs_wheel_path
from invoke import task

@task
def wheel_name(c):
    """Name of the wheel."""
    print(poetry_wheelname())

@task
def dbfs_wheel(c, branch=None):
    """DBFS wheel path."""
    print(default_dbfs_wheel_path(branch))
