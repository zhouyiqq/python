# _*_coding:utf_8_*_
# pandas was created by zy on 2021/11/26 21:09
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def project_info(project_data, project_name=' '):
    # 获取资源情况
    server_memory = project_data['内存大小'].astype(float)
    memory_labels, memory_distribut = memory_distribution(server_memory)

    #获取主机环境分布
    host_environment = project_data['主机环境']
    host_labels, host_env_nums=host_env(host_environment)
    #获取过去两周内存使用情况
    memoryratio_last2week = project_data['最近两周内存使用率峰值(%)'].str.strip('%').astype(float) / 100
    rate_labels,memoryratio = memory_used(memoryratio_last2week)
    labels=[memory_labels,host_labels,rate_labels]
    data=[memory_distribut,host_env_nums,memoryratio]
    title=['内存分布情况','主机环境情况','过去两周内存使用情况']
    draw_multipie(labels,data,title,project_name)

def draw_multipie(labels,data,title,project_name):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用指定的汉字字体类型（此处为黑体）

    fig, axj = plt.subplots(nrows=1, ncols=3, figsize=(8, 8), dpi=200)  # 建立饼图坑
    axes = axj.flatten()  # 子图展平
    for ax in range(0, 3):

        axes[ax].pie(x=data[ax], labels=labels[ax], autopct='%3.1f%%')
        axes[ax].set_title(project_name +str(sum(data[ax]))+'台服务器'+title[ax] )
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.8, hspace=0.5)  # 调整子图间距
    plt.savefig('./data/'+project_name+'.jpg')
    plt.show()


def project_server(project_id):
    # 去重取出产品编码
    pid = project_id.apply(str).tolist()  # 转成list
    id_list = list(set(pid))  #
    print(id_list)
    id_list.sort()
    print(id_list)
    id_list=['BU00026', 'BU00028', 'BU00030', 'BU00031', 'BU00193', 'BU00215', 'BU00246', 'BU00304', 'BU00439']
    project_name=['-智能强排','-软装协同','-智选精装','-筑美','-设计工具','-集团设管','-规划(强排)','-装修三维','-智能地库']
    id_nums = []  # 统计数字
    for _ in id_list:  # 赋初值
        id_nums.append(0)
    for id in pid:
        for i in range(len(id_list)):
            if id == id_list[i]:
                id_nums[i] += 1
    for i in range(len(id_list)):
        id_list[i] += (project_name[i]+': ' + str(id_nums[i]) + '台')
    labels = id_list
    title_str = '225台服务器在各个产品的分布情况'
    draw_pie(labels, id_nums, title_str)

def host_env(host_environment):
    #去重取出所有环境
    envs = host_environment.apply(str).tolist()  #转成list
    envs_list = list(set(envs)) #
    host_env_nums=[]  #统计数字
    for _ in envs_list:  #赋初值
        host_env_nums.append(0)
    for env in envs:
        for i in range(len(envs_list)):
            if env==envs_list[i]:
                host_env_nums[i]+=1
    for i in range(len(envs_list)):
        if 'nan'==envs_list[i]:
            envs_list[i]='未标注：'+str(host_env_nums[i])+'台'
        else:
            envs_list[i] +=(': '+ str(host_env_nums[i])+'台')
    labels =envs_list

    return labels, host_env_nums
def draw_envs_pie(labels,host_env_nums):
    title_str = '225台服务器的主机环境分布情况'
    draw_pie(labels, host_env_nums, title_str)
def memory_distribution(server_memory):
    memory_distribut= [0, 0, 0, 0, 0, 0,0]
    '''
        第0个：4G及以下；
        第1个，8G,
        第2个: 16G,
        第3个：32G,
        第4个：64G,
        第5个：128G
        第6个：256G
    '''
    for m in server_memory:
        if m<=4:
            memory_distribut[0]+=1
        elif m<=8:
            memory_distribut[1]+=1
        elif m<=16:
            memory_distribut[2]+=1
        elif m<=32:
            memory_distribut[3]+=1
        elif m<=64:
            memory_distribut[4]+=1
        elif m<=128:
            memory_distribut[5]+=1
        elif m<=256:
            memory_distribut[6] += 1
        else:
            print("no memory")
    labels = ['4G及4G以下:' + str(memory_distribut[0]) + '台', '8G：' + str(memory_distribut[1]) + '台',
              '16G：' + str(memory_distribut[2]) + '台', '32G：' + str(memory_distribut[3]) + '台',
              '64G：' + str(memory_distribut[4]) + '台', '128G：' + str(memory_distribut[5]) + '台',
              '256G：' + str(memory_distribut[6]) + '台']
    return labels,memory_distribut
def draw_memory_distribution_pie(labels,memory_distribut):

    title_str = '225台服务器的内存分布情况'

    draw_pie(labels, memory_distribut, title_str)

def memory_used(memoryratio_last2week):
    memoryratio = [0, 0, 0, 0, 0, 0, 0]  # 第0个：没有值；第1个，0-10,10-30,30-50,50-70,70-90,90-100
    '''
    第0个：没有值；
    第1个，0-10,
    第2个: 10-30,
    第3个：30-50,
    第4个：50-70,
    第5个：70-90,
    第6个：90-100
    '''
    for mr in memoryratio_last2week:

        if mr:
            if mr < 0.1:
                memoryratio[1] += 1
            elif mr < 0.3:
                memoryratio[2] += 1
            elif mr < 0.5:
                memoryratio[3] += 1
            elif mr < 0.7:
                memoryratio[4] += 1
            elif mr < 0.9:
                memoryratio[5] += 1
            else:
                memoryratio[6] += 1
        else:
            memoryratio[0] += 1
    # #整体服务器性能情况，以内存作为衡量8，16,32 64,128
    ##整体服务器用途情况(主机环境)，以开发，测试等分类
    ##整体服务器数量分配，分配给各个项目的情况，
    ##过去两周内存使用率情况，“未统计‘”，0,10,30,50,70，90
    ##整体服务器内存分配，分配给各个项目的情况
    ##各个项目的情况，整体服务器的数量、性能情况、环境使用情况，使用率
    labels = ['未记录-'+str(memoryratio[0])+'台', '内存使用率0-10%：'+str(memoryratio[1])+'台',
              '内存使用率10%-30%：'+str(memoryratio[2])+'台', '内存使用率30%-50%：'+str(memoryratio[3])+'台',
              '内存使用率50%-70%：'+str(memoryratio[4])+'台', '内存使用率70%-90%：'+str(memoryratio[5])+'台',
              '内存使用率90%以上：'+str(memoryratio[6])+'台']
    return labels, memoryratio

def draw_memoryused_pie(labels,memoryratio):
    # labels=['未记录','内存使用率：0-10%','内存使用率：10%-30%','内存使用率：30%-50%','内存使用率：50%-70%','内存使用率：70%-90%','内存使用率：90%以上']
    title_str='225台服务器过去两周内存使用情况'

    draw_pie(labels,memoryratio,title_str)

def draw_pie(labels,sizes,title_str):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # explode = (0, 0, 0, 0.1, 0, 0,0)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
    plt.title(title_str)
    plt.savefig('./data/' + title_str + '.jpg')
    plt.show()



if __name__ == '__main__':
    # ----------------输入配置，包括待处理文件等----------------------------
    original_filename = "服务器运行情况表.xlsx"
    # ----------------获取数据，DataFrame结构-----------------
    attendData_DF = pd.read_excel(original_filename)
    # ----------------获取资源数据，DataFrame结构-----------------
    server_memory=attendData_DF['内存大小'].astype(float)
    labels, server_memory_ratio=memory_distribution(server_memory)
    draw_memory_distribution_pie(labels,server_memory_ratio)
    # ----------------获取数据，最近两周内存使用率峰值(%)-----------------
    memoryratio_last2week = attendData_DF['最近两周内存使用率峰值(%)'].str.strip('%').astype(float) / 100
    labels, memoryratio=memory_used(memoryratio_last2week)
    draw_memoryused_pie(labels,memoryratio)
    # ----------------获取数据，服务器用途分析即：主机环境-----------------
    host_environment=attendData_DF['主机环境']
    labels, host_env_nums= host_env(host_environment)
    draw_envs_pie(labels, host_env_nums)
    # ----------------获取数据，服务器的在项目的分布情况-----------------
    project=attendData_DF['产品编码']
    project_server(project)
    # ----------------获取数据，服务器的某个具体项目的分布情况-----------------
    qiangpai= attendData_DF.loc[attendData_DF['产品编码'] == 'BU00026']
    project_info(qiangpai, project_name='BU00026-智能强排 ')

    qiangpai = attendData_DF.loc[attendData_DF['产品编码'] == 'BU00439']
    project_info(qiangpai, project_name='BU00439-智能地库 ')

    qiangpai = attendData_DF.loc[attendData_DF['产品编码'] == 'BU00215']
    project_info(qiangpai, project_name='BU00215-集团设管 ')

    qiangpai = attendData_DF.loc[attendData_DF['产品编码'] == 'BU00030']
    project_info(qiangpai, project_name='BU00030-智选精装 ')










