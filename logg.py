import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_log.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(massage)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)