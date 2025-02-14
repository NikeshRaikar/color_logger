import logging
import json


file = open('D:\\AT-Test\\automation_framework\\data.json')
data = json.load(file)
trgt_sw = data['Base_Target']["TS"]
bs_sw = data['Base_Target']["BS0"]


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    blue = "\x1b[34;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(asctime)s]-\t[%(name)s]-\t[%(levelname)s]::\t%(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: yellow + format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name, level=''):
    '''
    Func : This is used to create logger at module level
    :param name: __name__ of the module
    :param level: Supports all debug levels "DEBUG", "INFO", "CRITICAL", "ERROR"
    :return: Logger is returned.
    '''
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # formatter = logging.Formatter(f'[%(asctime)s]-\t[%(name)s]-\t[%(levelname)s]::\t%(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    # console_handler.setFormatter(formatter)
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    # file_handler = logging.FileHandler(f"../../automation_testframework/ORU_.log", mode="a", encoding="utf-8")
    # file_handler.setLevel(level)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    file_handler = logging.FileHandler(f"../../automation_testframework/Logs/STDOUT/ORU_.log", mode="a", encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)
    return logger





