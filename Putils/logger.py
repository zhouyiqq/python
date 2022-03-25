# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/17 20:38
#此代码做日志管理的
import logging
import os
import time
from colorama import Fore, Style
#创建日志
# logging.getLogger("sort_algonrithm").setLevel(logging.CRITICAL)
logger = logging.getLogger("zy")
logger.setLevel(logging.DEBUG)
#创建处理器
log_time = time.strftime("%Y%m%d",time.localtime(time.time()))
log_path = os.path.join(os.getcwd(), 'logs/')
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
        logger.debug(Fore.WHITE+msg.format(*args)+Style.RESET_ALL)
    else:
        logger.debug(Fore.WHITE+msg+Style.RESET_ALL)
def info(msg,*args):
    if len(args)>0:
        logger.info(Fore.GREEN+msg.format(*args)+Style.RESET_ALL)
    else:
        logger.info(Fore.GREEN+msg+Style.RESET_ALL)
def waring(msg,*args):
    if len(args)>0:
        logger.warning(Fore.RED+msg.format(*args)+Style.RESET_ALL)
    else:
        logger.warning(Fore.RED+msg+Style.RESET_ALL)
def critical(msg,*args):
    if len(args)>0:
        logger.critical(Fore.RED+msg.format(*args)+Style.RESET_ALL)
    else:
        logger.critical(Fore.RED+msg+Style.RESET_ALL)
if __name__ == "__main__":
    info("警告")

# log.critical("你好")
    # print('\033[1;35;0m字体变色，但无背景色 \033[0m')  # 有高亮 或者 print('\033[1;35m字体有色，但无背景色 \033[0m')
    # print('\033[1;45m 字体不变色，有背景色 \033[0m')  # 有高亮
    # print('\033[1;35;46m 字体有色，且有背景色 \033[0m')  # 有高亮
    # print('\033[0;35;46m 字体有色，且有背景色 \033[0m')  # 无高亮