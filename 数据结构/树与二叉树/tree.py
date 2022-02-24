# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/10 22:03
class Node:
    def __init__(self,name,type = 'dir'):
        self.name  = name
        self.type = type
        self.children = []
        self.parent = None
    def __repr__(self):
        return self.name
class FileSystenTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root
    def mkdir(self,name):
        #name以斜杆结尾
        if name[-1]!= "/":
            name+="/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now
    def ls(self):
        print(self.now.children)
        return self.now.children
    def cd(self,name):
        if name[-1]!="/":
            name+="/"
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return  0
        raise ValueError("该目录不存在")
    def pwd(self):
        print(self.now)
        return self.now
if __name__ == "__main__":
    tree = FileSystenTree()
    tree.mkdir("var/")
    tree.mkdir("test_t/")
    tree.ls()
    tree.cd("var/")
    tree.mkdir("hellow/")
    tree.ls()
    tree.pwd()
#链式储存方式
