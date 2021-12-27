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
    def is_empty(self):
        return len(self.stack)==0

stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())
#括号匹配问题，给一个字符串全是括号判断是否匹配
#解决思路：只要栈顶与要进来的匹配就出栈，不匹配就将这个元素进栈
s = "(){}{[(20)]}"
def brace_match(s):
    match = {')':'(','}':'{',']':'['}#做匹配用的字典
    for ch in s:
        if ch in {'(','{','['}:
            stack.push(ch)
        elif ch in {')','}',']'}:
            if stack.get_top() == match[ch]:#ch in {')',']','}'}
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
print(brace_match(s))
#数学表达式