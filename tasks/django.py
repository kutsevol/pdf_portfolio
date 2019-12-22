from invoke import task


@task
def run(c):
    """
    Task for running django app on 0.0.0.0 address and 8000 port.

    :param c: context variable of invoke
    """
    c.run("python manage.py runserver 0.0.0.0:8000")


@task
def migrate(c, make=False):
    """
    Task for preparing and executing migration.

    :param c: context variable of invoke
    :param make: flag for apply migrate equal (./manage.py migrate)
    """
    if make:
        c.run("python manage.py makemigrations")
    c.run("python manage.py migrate")


@task
def static(c):
    """
    Task for collecting static files.

    :param c: context variable of invoke
    """
    c.run("python manage.py collectstatic")
