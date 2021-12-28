# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/27 22:11
import queue #线程安全
from collections import deque #里面包含一些数据结构，解题用
# q = deque()#创建队列
# q.append()#进队
# q.popleft()#出队
# q.appendleft()#双向队列队首进队
# q.pop()#双向队列队尾出队
#迷宫问题
#给一个二维列表，表示表示迷宫，（0表示通道，1表示围墙）
#回溯法：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点，使用栈储存当前路径