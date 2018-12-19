#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from setting import logger_setting


def get_logger():
    logger = logging.getLogger(__name__)
    if len(logger.handlers) == 0:
        logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler('%s%s' % (logger_setting.LOGGER_FILE_PATH, logger_setting.LOGGER_FILE_NAME))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s- %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        handler.encoding = 'utf-8'
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(console)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info("Start print log")
    logger.info("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
