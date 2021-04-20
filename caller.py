import logging
from callee import func

logger = logging.getLogger(__name__)

def main():
    logger.info("info")
    logger.debug("debug")
    func()

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG)
    #logger.level or logging.level
    logger.setLevel(logging.INFO)
    main()
