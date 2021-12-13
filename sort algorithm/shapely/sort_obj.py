# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/12 19:48
import random
import time
class sort_obj():
    def __init__(self,li):
        self.li = li

    def run_time(func):
        def wraper(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            print('%s running time %s　second' % (func.__name__, t2 - t1))
            return result
        return wraper
    def li_random(self,li):
        #将列表随机排序
        return random.shuffle(li)
    def bubble_sort(self):
        # 冒泡排序,对比相邻两个数，满足条件，然后交换位置
        li = self.li
        for i in range(len(li) - 1):  # 遍历列表
            for j in range(len(li) - 1):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
        return li
    def insert_sort(self):
        #插入排序
        li = self.li
        for i in range(1, len(li)):
            tmp = li[i]  # 将抽到的牌的值储存下来
            j = i - 1  # 手中的牌的下标
            while j >= 0 and li[j] > tmp:  # 如果手中的牌大于抽到的牌
                li[j + 1] = li[j]
                j -= 1  # 这是一个顺序移动寻找位置插入的过程
            li[j + 1] = tmp  # 插入
        return li

    def partition_sort(self):
        '''快速排序，归位函数'''
        li = self.li
        left = 0
        right =len(li) - 1
        tmp = li[left]
        while left < right:
            while left < right and li[right] >= tmp:
                right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[left] = tmp
        return li

    def select_sort_simple(self,li):
        '''简单选择排序'''
        li = self.li
        li_new = []
        for i in range(len(li)):
            min_val = min(li)  # 寻找列表最小的值
            li_new.append(min_val)  # 在新列表添加最小的值
            li.remove(min_val)  # 从列表中删除最小的值
        return li_new  # 返回排序好的新列表

    def select_sort(self):
        '''不开辟新的空间，寻找无序列表列表中的最小的数依次交换位置进行排序'''
        li = self.li
        for i in range(len(li) - 1):  # 不遍历列表最后一个元素
            min_loc = i  # 标记最小的数
            for j in range(i + 1, len(li)):  # 在无序列表中遍历
                if li[j] < li[min_loc]:
                    min_loc = j
            li[i], li[min_loc] = li[min_loc], li[i]  # 将无序列表最小的那个数交换位置
        return li
    @run_time
    def insert_sort_gap(self,gap):#把无序区里的数放在有序区里冒泡
        '''这是插入排序，gap是每组数的相隔数'''
        li = self.li
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and li[j] > tmp:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        return li

if __name__ == "__main__":
    li = [random.randint(0, 1000) for i in range(1000)]
    sort = sort_obj(li)
    print(li)
    print(sort.insert_sort_gap(1))
