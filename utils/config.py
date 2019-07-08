import os
import secrets

from utils.constants import (DB_ENGINES, FULL_PATH_ENV_FILE,
                             FULL_PATH_ENV_FILE_TEMPLATE)


def parse():
    parse_result = {}

    with open(FULL_PATH_ENV_FILE_TEMPLATE) as env_template_file:
        for line in env_template_file:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                # Ignore comments and lines without assignment.
                continue

            # Remove whitespaces and quotes:
            env_name, env_value = line.split("=", 1)
            env_name = env_name.strip()
            env_value = env_value.strip().strip('\'"')

            parse_result[env_name] = env_value
    return parse_result


def dump(parse_data, engine):
    parse_data["DJANGO_SECRET_KEY"] = secrets.token_hex(25)
    parse_data["DJANGO_DB_ENGINE"] = DB_ENGINES[engine]

    with open(FULL_PATH_ENV_FILE, "w") as env_file:
        for key, value in parse_data.items():
            env_file.write(
                f"{key}={value}\n"
            )


def check_exist_env_file():
    return os.path.isfile(FULL_PATH_ENV_FILE)
