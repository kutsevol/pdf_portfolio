from invoke import task

from utils.config import check_exist_env_file, dump, parse


@task
def create_dot_env(c,
                   generate_admin_url=False,
                   rewrite=False,
                   db_engine="sqlite",
                   django_env="production",
                   domain_name="127.0.0.1",
                   ):
    """
    Create .env file from template with the ability to change parameters.

    :param c: context (invoke variable)
    :param generate_admin_url: create random string for admin path
    (default=False and will be use admin/)
    :param rewrite: rewrite .env file if exist (default=False)
    :param db_engine: to set the custom engine (postgres, sqlite, etc.),
    :param django_env: to set env settings (development or production)
    :param domain_name: to set domain name (use for production env)
    """
    kwargs = {
        "db_engine": db_engine,
        "django_env": django_env,
        "generate_admin_path": generate_admin_url,
        "domain_name": domain_name,
    }

    if not rewrite and check_exist_env_file():
        raise FileExistsError(
            "Check exist version of .env file in config folder",
        )

    parse_result = parse()

    dump(
        parse_data=parse_result,
        **kwargs,
    )
