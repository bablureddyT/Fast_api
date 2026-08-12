import logging

# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger(__name__)
# logger.info("User created")
# logger.error("Database connection failed")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        #   filename="app.log",if you want to store logs in a file
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )