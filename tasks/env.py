from invoke import task

from utils.dump_config import check_exist_env_file, dump, parse


@task
def create_dot_env(c, rewrite=False, db_engine="sqlite",
                   django_env="production"):
    """
    Create .env file from template with the ability to change a several
    parameters
    :param c: context (invoke variable)
    :param rewrite: rewrite .env file if exist (default=False)
    :param db_engine: to set the custom engine (postgres, sqlite, etc.),
    :param django_env: to set env settings (development or production))
    """
    kwargs = {
        "db_engine": db_engine,
        "django_env": django_env,
    }

    if not rewrite and check_exist_env_file():
        raise FileExistsError(
            "Check exist version of .env file in config folder"
        )

    parse_result = parse()

    dump(
        parse_data=parse_result,
        **kwargs,
    )
