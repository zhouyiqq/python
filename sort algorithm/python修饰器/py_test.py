# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/11/7 16:39
#这就是修饰器牛不牛比
#客人空手来，还得请上楼，干啥都同意，有参给上楼
def secondFloor(func):
    def thirdFloor(info):
        print("原函数开始执行了")
        func(info)
        print("原函数执行完了")
    return thirdFloor
@secondFloor
def origion(info):
    print(info)

#sf = secondFloor(origion)
#sf()
info = "hellword"
origion(info)
