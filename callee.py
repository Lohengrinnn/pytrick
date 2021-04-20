import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def func():
    logger.info("info")
    logger.debug("debug")
