import configparser
import pathlib

# Setup base directory
# 1). Finds the path from this gets called for the first time
BASE_PATH = pathlib.Path().absolute()  # not go up one dir (....Path('..')....)

# # 2). Finds the path where the main functions for loading config runs
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load config
config = configparser.ConfigParser()
# Move one up to find the project root's path and then config present in it
final_path = BASE_PATH.joinpath("config.ini")  # .joinpath("..", "config.ini") # go up one dir

config.read(final_path)

DB_CONN = {
    'USER': config['db_conn']['user'],
    'PASSWORD': config['db_conn']['password'],
    'HOST': config['db_conn']['host'],
    'PORT': config['db_conn']['port'],
    'DATABASE': config['db_conn']['database'],
    'RAISE_ON_WARNINGS': config['db_conn']['raise_on_warnings'],
}

API_CONF = {
    'HOST': config['api_conf']['host'],
    'PORT': int(config['api_conf']['port']),
}

TABLE_CONF = {
    'NAME': config['table_conf']['name'],
    'ID_COL': config['table_conf']['id_col'],
}
