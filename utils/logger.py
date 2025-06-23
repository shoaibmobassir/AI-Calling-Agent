import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("AI-Agent-System")

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

def log_debug(msg):
    logger.debug(msg)
