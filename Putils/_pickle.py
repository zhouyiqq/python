# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 17:06
import os
from Putils.logger import logger
def __saveTempData(obj, file_name):
    try:
        import pickle
        _dir = "c:/data/outline/"
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        save_file = open(_dir + file_name + ".pkl", "wb+")
        content = pickle.dumps(obj)
        save_file.write(content)
        save_file.close()
    except Exception as e:
        logger.error("文件保存失败:{}", str(e))

#
# _dir = "c:/data/outline/"
#     with open(_dir + "inin_data.pkl.pkl", "rb") as file:
#         init_data = pickle.loads(file.read())
#     with open(_dir + "are_list.pkl.pkl", "rb") as file:
#         are_list = pickle.loads(file.read())

