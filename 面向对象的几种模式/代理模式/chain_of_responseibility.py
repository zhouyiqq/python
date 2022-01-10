# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/2 15:59
from abc import ABCMeta,abstractmethod
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_contect(self):
        pass
    @abstractmethod
    def set_contect(self,contect):
        pass

class RealSubject(Subject):
    def __init__(self,filename):
        self.filename = filename
        f = open(filename)
        print("读取文件")
        self.contect = f.read()
        f.close()
    def get_contect(self):
        return self.contect
    def set_contect(self,contect):
        f = open(self.filename,"w")
        f.write(contect)
        f.close()
# sudj = RealSubject("test.txt")
# print(sudj.get_contect())
class VirtualProxy(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None
    def get_contect(self):
        if not self.subj:
            self.subj=RealSubject(self.filename)
        return self.subj.get_contect()
    def set_contect(self,contect):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_contect(contect)


subj = VirtualProxy("test.txt")
print(subj.get_contect())