# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/31 20:46
from collections import deque
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
def print_f(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] == -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])#起点
    realpath.reverse()
    print(realpath[:])
def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1 -1))#表示起点
    path = []

    while len(queue)>0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_f(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2 #标记已经走过

    else:
        print("没有路")
        return False
maze_path_queue(1,1,8,8)