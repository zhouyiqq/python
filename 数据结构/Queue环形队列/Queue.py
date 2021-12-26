# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/26 16:12
from collections import deque
class Queue:
    def __init__(self,size=100):
        self.queue = [0 for _ in range(size)]#环形队列,队尾出值，队首插值
        self.rear = 0 #队首指针
        self.front =0 #队尾指针
        self.size = size
    def push(self,element):#进队列
        if not self.is_filled():
            self.rear = (self.rear+1)%self.size#队首往前移动一位
            self.queue[self.rear] = element #队首指针指向新进的元素
        else:
            raise IndexError("队列已经满了，无法插入元素")
    def pop(self):#出队列
        if not self.is_empty():
            self.front = (self.front+1)%self.size#队尾往前移动一位
            return self.queue[self.front]#返回队尾元素
        else:
            raise IndexError("队列已经空了，无法出队列")#触发异常
    def is_empty(self):
        return self.rear == self.front
    def is_filled(self):
        return (self.rear+1)%self.size == self.front
def tail(n):
    with open("test.txt","r") as F:
        q = deque(F,n)
        return q
if __name__ == "__main__":
    print(tail(5))
