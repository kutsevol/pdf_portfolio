from invoke import task


@task
def run(c):
    c.run("python manage.py runserver 0.0.0.0:8000")


@task
def migrate(c, make=False):
    if make:
        c.run("python manage.py makemigrations")
    c.run("python manage.py migrate")


@task
def static(c):
    c.run("python manage.py collectstatic")
