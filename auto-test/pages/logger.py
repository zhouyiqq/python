import logging
import os
import time

# 创建日志
logging.getLogger("shapely").setLevel(logging.CRITICAL)
logger = logging.getLogger()

# 设置日志
# 等级总开关的默认级别为WARNING，此处改为DEBUG
logger.setLevel(logging.DEBUG)

# 文件handler
log_time = time.strftime('%Y%m%d', time.localtime(time.time()))
log_path = os.path.join(os.getcwd(), 'logs/')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file_name = log_path + log_time + '.log'
file_handler = logging.FileHandler(log_file_name)
# 设置文件handler的等级
file_handler.setLevel(logging.INFO)
# 第三步，定义handler的输出格式
file_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - pid:%(process)d - tid:%(thread)d - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# 控制台handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


def debug(msg, *args):
    if len(args) > 0:
        logger.debug(msg.format(*args))
    else:
        logger.debug(msg)


def info(msg, *args):
    if len(args) > 0:
        logger.info(msg.format(*args))
    else:
        logger.info(msg)


def warning(msg, *args):
    if len(args) > 0:
        logger.warning(msg.format(*args))
    else:
        logger.warning(msg)


def error(msg, *args):
    if len(args) > 0:
        logger.error(msg.format(*args), exc_info=True)
    else:
        logger.error(msg, exc_info=True)


def critical(msg, *args):
    logger.critical(msg)


if __name__ == "__main__":
    debug('this is a logger debug message')
    info('this is a logger info message')
    warning('this is a logger warning message')
    error('this is a logger error message')
    critical('this is a logger critical message')
