import os
import secrets

from utils.constants import (
    DB_ENGINES,
    ENV_LIST_NAMES,
    FULL_PATH_ENV_FILE,
    FULL_PATH_ENV_FILE_TEMPLATE,
    PROD,
)


def parse():
    """
    To get all key-values from template file.

    :return: dict with key and values as default from template file.
    """
    parse_result = {}

    with open(FULL_PATH_ENV_FILE_TEMPLATE) as env_template_file:
        for line in env_template_file:
            line = line.strip()

            if not line or line.startswith('#') or '=' not in line:
                # Ignore comments and lines without assignment.
                continue

            # Remove whitespaces and quotes:
            env_name, env_value = line.split('=', 1)
            env_name = env_name.strip()
            env_value = env_value.strip().strip('\'"')

            parse_result[env_name] = env_value
    return parse_result


def dump(parse_data, **kwargs):
    """
    Write parsed and updated data to the file.

    :param parse_data: original dict from template
    :param kwargs: values which should be updated for the new file
    """
    parse_data.update(set_options(parse_data, **kwargs))

    with open(FULL_PATH_ENV_FILE, 'w') as env_file:
        for key, value in parse_data.items():
            if value:
                env_file.write(
                    f"{key}={value}\n",
                )


def check_exist_env_file():
    """
    Check exist .env file.

    :return: bool (True/False)
    """
    return os.path.isfile(FULL_PATH_ENV_FILE)


def set_options(result, **kwargs):
    """
    To set custom options from command line.

    :param result: dict (env.template) with env variables
    :param kwargs: parameters from command line
    :return: update dict
    """
    result['SECRET_KEY'] = secrets.token_hex(25)
    result['DB_ENGINE'] = DB_ENGINES[kwargs.get('db_engine', 'sqlite')]

    if kwargs.get('django_env') in ENV_LIST_NAMES:
        result['DJANGO_ENV'] = kwargs['django_env']

    if kwargs.get('generate_admin_path'):
        result['ADMIN_URL'] = ''.join((secrets.token_hex(25), '/'))

    if result['DJANGO_ENV'] == PROD:
        result["DOMAIN_NAME"] = kwargs["domain_name"]

    return result
