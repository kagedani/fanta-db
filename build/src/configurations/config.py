class BaseConfig(object):
    ENV = "default"
    APP_NAME = "fanta-db-23"
    EMPTY_STRING = ""
    APP_EXEC_ID = EMPTY_STRING
    MAX_CONNECT_TIMEOUT = 30
    MAX_RESPONSE_TIMEOUT = 30
    FANTACALCIO_IT_ENDPOINT = "https://www.fantacalcio.it"
    FANTACALCIO_IT_LOGIN_PATH = "/api/v1/User/login"
    FANTACALCIO_IT_DOWNLOAD_PATH = "/api/v1/Excel/stats/{SEASON}/1"
    FANTACALCIO_IT_DOWNLOAD_CONFIG = {
        "2324": "18",
        "2223": "17",
        "2122": "16",
        "2021": "15"
    }
    USERNAME = "Aldone95"
    PSW = "*******"
    LOG_CONFIG = {
        "default": {
            "file_level": "INFO",
            "file_path": f"./src/log/{APP_NAME}.json",
            "console_level": "DEBUG"
        }
    }
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://fanta_db_username:fanta_db_password@localhost/fanta_db"
    SESSION_MAKER = None

