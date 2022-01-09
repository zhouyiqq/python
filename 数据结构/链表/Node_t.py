# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/4 19:10
#链表是有一系列节点组成的元素集合，每个节点包含两个部分，数据域Item和指向下一个节点的指针next，通过节点自己的互相连接，最终形成一个链表
class Node:
    def __init__(self,item):
        self.item = item#数据域
        self.next = None#指向下一个节点的指针
def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head
def print_linklist(head):
    while head:
        print(head.item,end=",")
        head = head.next
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head
lk = create_linklist_tail([1,2,3])
print_linklist(lk)
