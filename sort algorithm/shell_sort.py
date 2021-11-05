# _*_coding:utf_8_*_
# sort algorithm was created by zy on 2021/10/16 8:14
"""希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。"""
import random
import time
stat_time = time.time()
#li=[5,7,4,6,3,1,2,9,8]
def insert_sort_gap(li,gap):
    '''这是插入排序，gap是每组数的相隔数'''
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        print(d)
        insert_sort_gap(li,d)
        d //= 2

li = list(range(1000))
random.shuffle(li)
shell_sort(li)#将列表元素随机排序
print(li)
end_time=time.time()
print("程序结束用时%fs"%(end_time-stat_time))