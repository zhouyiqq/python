# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/28 13:25
#pickle提供简单持久化的功能，将对象以文件的形式储存在磁盘上
#几乎所有的数据结构（列表，字典，集合，类）都可以被序列化
#序列化后可读性差
import pickle
# pickle.dumps(obj,file,proctocol) 将obj序列化写到file（文件）里，proctocol默认为0，表示以文本的形式写入，1或2表示以二进制写入
# pickle.load(file) 反序列化，表示将文件数据解析为一个对象，解析的时候类必须已经定义，不然报错
#clear_memo() 对同一个对象多次调用dump时，pickle不会多次序列化，除非清楚备忘录
def save_variable(v,filename):  #保存变量
    with open(filename,'wb') as f:
        pickle.dumps(v,f)
        return filename
def load_variable(filename): #读取变量
    with open(filename,'rb') as f:
        r = pickle.load(f)
    return r


