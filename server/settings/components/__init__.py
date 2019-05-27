from decouple import AutoConfig

from utils.constants import BASE_DIR, CONFIG_DIR

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))
