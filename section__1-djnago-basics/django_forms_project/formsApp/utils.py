# logger.py

import logging

def setup_logger(name, log_file=None, level=logging.INFO):
    """
    Setup a logger with the given name, log file, and level.
    
    :param name: Logger name, usually __name__.
    :param log_file: File path for logging. If None, only console output is used.
    :param level: Logging level, e.g., logging.INFO, logging.DEBUG.
    :return: Configured logger.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    # If a log file is specified, add a file handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
