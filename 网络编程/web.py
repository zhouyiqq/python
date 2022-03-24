import json
import sys
from multiprocessing import Process, Pool
from core.db.redis_helper import redis_engine
from series_frame import index_part
from conf.Logger import arithmetic_logger
from time import sleep
from conf.Logger import web_server_logger
logger = web_server_logger
def del_uuid(project_key):
    redis_engine.hdel('indicator_project', project_key)
    arithmetic_logger.info(
        "删除项目{}-------------indicator_project的uuid存储,长度{}".format(project_key, redis_engine.hlen('indicator_project')))
    redis_engine.hdel('indproject_data', project_key)
    arithmetic_logger.info(
        "删除项目{}-------------indproject_data存储，指标等候项目长度{}".format(project_key, redis_engine.hlen("indproject_data")))


class CalculateServer(Process):

    def __init__(self, project_key, para_json):
        super(CalculateServer, self).__init__()
        self.project_key = project_key
        self.para_json = para_json

    def run(self):
        index_part(self.para_json)
        del_uuid(str(self.project_key))


class IndicatorServer(Process):

    def __init__(self, i):
        super(IndicatorServer, self).__init__()
        self.process_num = i

    # 复写run方法
    def run(self):
        while True:
            try:
                project_key = redis_engine.rpop("indicator_queue")
                if project_key:
                    arithmetic_logger.info(
                        "指标项目{}弹出,{}号进程开始处理，等候队列长度{}，等候项目长度{}".format(project_key, self.process_num,
                                                                      redis_engine.llen("indicator_queue"),
                                                                      redis_engine.hlen("indproject_data")))
                    # inputPath = r'E:\main_code_prod\input_test\input2.json'
                    # with open(inputPath, 'r', encoding='UTF-8') as json_file:
                    #     para_json = json.load(json_file)
                    para_json = redis_engine.hget('indproject_data', str(project_key))
                    if para_json:

                        # print("开始计算".format(para_json["projectInfo"]["projectId"]))
                        # ins = CalculateServer(str(para_json["projectInfo"]["projectId"]), para_json)
                        ins = CalculateServer(str(project_key), json.loads(para_json))
                        ins.start()
                        ins.join()

                else:
                    sleep(1)
            except:
                arithmetic_logger.error("指标计算异常===============================")
def test():
    inputPath = r'E:\main_code_prod\input_test\input2.json'
    with open(inputPath, 'r', encoding='UTF-8') as json_file:
        json_para = json.load(json_file)
    json_para_Info=json_para["projectInfo"]
    redis_engine.hset('indicator_project', json_para_Info["projectId"], json_para_Info["uuid"])
    redis_engine.hset('indproject_data', json_para_Info["projectId"], json.dumps(json_para))
    redis_engine.lpush("indicator_queue", json_para_Info["projectId"])

if __name__ == '__main__':
    # pool = Pool(processes=4)
    # test()
    lt = [IndicatorServer(i) for i in range(12)]
    for server in lt:
        server.start()
    logger.info("指标indicatorsever服务已启动......................................")
    while True:
        sleep(120)
