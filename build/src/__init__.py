from src.configurations.config import BaseConfig
from src.utils.json_log_formatter import JsonFormatter
from src.data.PlayersStats import PlayersStats
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from datetime import datetime
import logging


def init_logging(conf):
    root_logger = logging.getLogger('')

    root_logger.setLevel(logging.DEBUG)

    handler = TimedRotatingFileHandler(conf.LOG_CONFIG[conf.ENV]["file_path"], when='midnight')
    handler.setLevel(conf.LOG_CONFIG[conf.ENV]["file_level"])
    handler.setFormatter(JsonFormatter())
    handler.suffix = '%Y%m%d'
    root_logger.addHandler(handler)

    console_handler = StreamHandler()
    console_handler.setLevel(conf.LOG_CONFIG[conf.ENV]["console_level"])
    console_handler.setFormatter(JsonFormatter())
    console_handler.suffix = '%Y%m%d'
    root_logger.addHandler(console_handler)
    logging.info("Logger setup completed")


def set_app_unique_id(config):
    config.APP_EXEC_ID = f"{config.APP_NAME}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    logging.info(f"Application {config.APP_NAME} started with execution id {config.APP_EXEC_ID}")


def init_database(configurations):
    logging.info(f"Setting up the database {configurations.SQLALCHEMY_DATABASE_URI}")
    engine = create_engine(configurations.SQLALCHEMY_DATABASE_URI)
    logging.info(f"Setting up the session maker: started")
    configurations.SESSION_MAKER = sessionmaker(engine)
    logging.info(f"Setting up the session maker: done")
    if not database_exists(engine.url):
        create_database(engine.url)
        logging.info(f"New database created {database_exists(engine.url)}")
    else:
        logging.info(f"Database already exists")
    with engine.connect() as connection:
        with configurations.SESSION_MAKER() as session:
            if engine.dialect.has_table(connection, PlayersStats.__tablename__):
                PlayersStats.__table__.drop(engine)
            PlayersStats.__table__.create(engine)
            session.commit()


def initialize():
    configurations = BaseConfig
    init_logging(configurations)
    set_app_unique_id(configurations)
    init_database(configurations)
    return configurations
