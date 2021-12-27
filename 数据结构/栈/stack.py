# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/27 19:23
class Stack:
    """
    LIFO:后进先出
    push：进栈
    pop：出栈
    """
    def __init__(self):
        self.stack = []
    def push(self,element):#进栈
        self.stack.append(element)
    def pop(self):#出栈
        return self.stack.pop()
    def get_top(self):#取栈顶
        if len(self.stack) > 0:
            return self.stack[-1]#取列表的最后一个元素
        else:
            return None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
#