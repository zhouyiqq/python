# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/27 22:11
# import queue #线程安全
# from collections import deque #里面包含一些数据结构，解题用
# q = deque()#创建队列
# q.append()#进队
# q.popleft()#出队
# q.appendleft()#双向队列队首进队
# q.pop()#双向队列队尾出队
#迷宫问题
#给一个二维列表，表示表示迷宫，（0表示通道，1表示围墙）
#回溯法：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点，使用栈储存当前路径
#回退法，深度优先搜索
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
dirs = [
        lambda x,y:(x+1,y),#上
        lambda x,y:(x-1,y),#下
        lambda x,y:(x,y-1),#左
        lambda x,y:(x,y+1)#右
    ]#表示四个方向
def maze_path(x1,y1,x2,y2):#x1,y1表示起点，x2，y2表示终点
    _stack = []#列表为栈
    _stack.append((x1,y1))

    #栈空表示没有路
    while(len(_stack)>0):#只要栈不空就一直寻找下去
        curNode = _stack[-1]#当前结点
        if curNode[0]==x2 and curNode[1]==y2:
            #表示走到终点了
            print(_stack[:])
            return True
        #四个方向，上，右，下，左
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])#寻找下一个结点
            #如果下一个结点能走
            #x表示行，y表示列
            if maze[nextNode[0]][nextNode[1]] == 0: #0表示空白可以走
                #把这个结点加到栈上
                _stack.append(nextNode)
                #把这个结点标记为走过
                maze[nextNode[0]][nextNode[1]] = 2
                break#找到一个可走的方向就跳出循环
        else:#如果这个结点几个方向都被堵了
            maze[nextNode[0]][nextNode[1]] = 2#把这个结点标记为走过
            _stack.pop()#栈顶出栈,默认删除最后一个元素

    else:
        print("死路")
        return False
maze_path(1,1,8,8)
#广度优先搜索，使用队列储存目前正在考虑的点
