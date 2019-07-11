from pathlib import PurePath

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = PurePath(__file__).parent.parent

CONFIG_DIR = "config"
ENV_FILE_TEMPLATE = ".env.template"
ENV_FILE = ".env"

FULL_PATH_ENV_FILE_TEMPLATE = PurePath(BASE_DIR, CONFIG_DIR, ENV_FILE_TEMPLATE)
FULL_PATH_ENV_FILE = PurePath(BASE_DIR, CONFIG_DIR, ENV_FILE)

DB_ENGINES = {
    "sqlite": "django.db.backends.sqlite3",
    "postgres": "django.db.backends.postgresql_psycopg2",
}

DEV = "development"
PROD = "production"

ENV_LIST_NAMES = {
    DEV, PROD,
}
