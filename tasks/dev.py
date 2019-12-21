from invoke import task


@task
def test(c):
    """
    Task for running tests.

    :param c: context variable of invoke
    """
    c.run("pytest")


@task
def flake(c):
    """
    Task for running linter.

    :param c: context variable of invoke
    """
    c.run("flake8")


@task
def isort(c):
    """
    Task for running isort tool which will check order import.

    :param c: context variable of invoke
    """
    c.run("isort -rc .")
