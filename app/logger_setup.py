import os
import logging
import logging.config
from dotenv import load_dotenv

def setup_logging():
    load_dotenv()

    log_file = os.getenv("LOG_FILE", "calc.log")
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    with open("logging.conf", "r") as f:
        config = f.read().replace("%(LOG_FILE)s", log_file)

    with open("temp_logging.conf", "w") as f:
        f.write(config)

    logging.config.fileConfig("temp_logging.conf", disable_existing_loggers=False)
    os.remove("temp_logging.conf")

    logging.getLogger().setLevel(log_level)
