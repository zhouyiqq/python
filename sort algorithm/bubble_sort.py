# _*_coding:utf_8_*_
# sort algorithm was created by zy on 2021/10/16 17:36
import random
import time
#冒泡排序,对比相邻两个数，满足条件，然后交换位置
stat_time = time.time()
def bubble_sort(li):
    for i in range(len(li)-1):#遍历列表
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
li = [random.randint(0,1000) for i in range(100)]
bubble_sort(li)
end_time = time.time()
print("一共用时%fs"%(end_time-stat_time))
print(li)