# _*_coding:utf_8_*_
# pythonProject1 was created by zy on 2021/10/17 15:16
import time
stat_time = time.time()
def insert_sort(li):
    for i in range(1,len(li)):
        tmp =li[i]#将抽到的牌的值储存下来
        j=i-1#手中的牌的下标
        while j>=0 and li[j]>tmp:#如果手中的牌大于抽到的牌
            li[j+1] =li[j]
            j-=1#这是一个顺序移动寻找位置插入的过程
        li[j+1]=tmp#插入
        print(li)
li = [3,2,4,1,5,7,9,6,8]
insert_sort(li)
end_time=time.time()
print(li)
print("程序结束用时%fs"%(end_time-stat_time))