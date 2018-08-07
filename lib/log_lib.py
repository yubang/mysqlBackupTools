# coding:UTF-8

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from config import config


class LogLib:

    @staticmethod
    def get_logging(log_name):

        level = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARN": logging.WARN,
        }.get(config.system_log_level, logging.DEBUG)

        LOG_FILE = os.path.join(config.system_log_path, log_name+".log")
        handler = TimedRotatingFileHandler(LOG_FILE, 'D', 1, 0)  # 实例化handler

        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(funcName)s - %(message)s'
        formatter = logging.Formatter(fmt)  # 实例化formatter
        handler.setFormatter(formatter)  # 为handler添加formatter
        handler.suffix = "%Y%m%d-%H%M.log"
        log = logging.getLogger(log_name)
        log.setLevel(level)
        log.addHandler(handler)
        return log
