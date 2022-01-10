# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/9 21:20

class LinkList:
    class Node:#这是一个结点，定义了一个数据域和指向下一个结点的指针
        def __init__(self,item = None):
            self.item = item
            self.next = None
    class LinkListIterator:#这是一个链表的迭代器，包含本节点和下一个结点
        def __init__(self,node):
            self.node = node
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        def __iter__(self):
            return self
    def __init__(self,iterable=None):#真正的链表，直接将一个列表转换为一个链表
        self.head = None#头结点
        self.tail = None#尾结点
        if iterable:
            self.extend(iterable)
    def append(self,obj):
        s=LinkList.Node(obj)#s是链表中的一个结点
        if not self.head:#如果是第一个元素头结点和尾结点同时指向s
            self.head = s
            self.tail = s
        else:
            self.tail.next = s#尾结点插入
            self.tail = s#更新尾结点
    def extend(self,iterable):#封装迭代对象
        for obj in iterable:
            self.append(obj)
    def find(self,obj):#对于一个元素判断是否在哈希表里
        for n in self:
            if n == obj:
                return True
    def __iter__(self):#创建一个迭代的链表
        return self.LinkListIterator(self.head)
    def __repr__(self):#将self对象转换成字符解包输出self是可迭代的
        return "<<"+",".join(map(str,self))+">>"
#类似集合
class HashTab:
    def __init__(self,size = 101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]#创建一个长度为101的哈希表
    def h(self,k):#哈希值作为索引
        return k%self.size
    def insert(self,k):
        i = self.h(k)#i不唯一映射
        if self.find_(k):
            print("已经被插入")
        else:
            self.T[i].append(k)#将k插入的T[i]中
    def find_(self,k):
        i = self.h(k)
        a = self.T[i]
        b =  k
        return self.T[i].find(k)
ht = HashTab()
ht.insert(0)
ht.insert(1)
ht.insert(2)
ht.insert(156)
print(",".join(map(str,ht.T)))
print(ht.find_(2))
#如果发生hash冲突通过拉链法或者开发寻址法解决
# lk = LinkList([1,2,3,4,5])
# # for element in lk:
# #     print(element)
# print(lk)