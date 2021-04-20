import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def func():
    s_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("file.log")
    s_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.WARNING)
    logger.addHandler(s_handler)
    logger.addHandler(f_handler)
    # handler.level >= level and logger.level >= level
    # so debug won't be printed.
    print("debug won't print since logger.level = INFO")
    # s_handler and default handler created within basicConfig
    # both output to console.
    logger.debug("debug")
    logger.info("info")
    logger.warn("warn")
