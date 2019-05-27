from invoke import task


@task
def test(c):
    c.run("pytest")


@task
def flake(c):
    c.run("flake8")


@task
def isort(c):
    c.run("isort -rc .")
