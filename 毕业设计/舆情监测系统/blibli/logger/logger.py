# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/17 20:38
#此代码做日志管理的
import logging
import os
import time
#创建日志
# logging.getLogger("sort_algonrithm").setLevel(logging.CRITICAL)
logger = logging.getLogger("zy")
logger.setLevel(logging.DEBUG)
#创建处理器
log_time = time.strftime("%Y%m%d",time.localtime(time.time()))
log_path = os.path.join(os.getcwd(), 'logger/logs/')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file_name = log_path + log_time + ".log"
#文件输出hander
file_handler = logging.FileHandler(log_file_name)
file_handler.setLevel(logging.INFO)#文件输出级别
file_formatter = logging.Formatter("%(asctime)s-%(filename)s[line:%(lineno)d]-pid:%(process)d-tid:%(thread)d-%(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
#控制台hander
console_hander = logging.StreamHandler()
console_hander.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s-%(levelname)s:%(message)s")
console_hander.setFormatter(console_formatter)
logger.addHandler(console_hander)
def debug(msg,*args):
    if len(args)>0:
        logger.debug(msg.format(*args))
    else:
        logger.debug(msg)
def info(msg,*args):
    if len(args)>0:
        logger.info(msg.format(*args))
    else:
        logger.info(msg)
def waring(msg,*args):
    if len(args)>0:
        logger.warning(msg.format(*args))
    else:
        logger.warning(msg)
def critical(msg,*args):
    if len(args)>0:
        logger.critical(msg.format(*args))
    else:
        logger.critical(msg)
if __name__ == "__main__":
    waring("警告")