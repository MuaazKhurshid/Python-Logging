import logging.config


def get_logger_obj() -> object:
    """
    Sets configs for Log obj and returns it.
    """
    logging.config.fileConfig('configs/logging.ini', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    return logger

logger = get_logger_obj()



if __name__ == '__main__':
    logger.info("Hello to Time Rotating Logging.")