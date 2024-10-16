# utils/logging_utils.py
import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Function to setup a logger.

    Args:
        name (str): The name of the logger.
        log_file (str): The file to which logs should be written.
        level (int): The logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
