# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/9 23:22
class person:
    def __init__(self,num):
        self.num  = num
    class head:
        def __init__(self):
            pass
        class eye:
            def __init__(self,num):
                self.num = num
                # print(self.num)
p = person(5).head.eye(10)

print(p.num)