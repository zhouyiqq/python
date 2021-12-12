# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/12 19:48
import random
import time
class sort_obj():
    def __init__(self,li):
        self.li = li

    def run_time(func):

        start_time = time.time()
        func
        end_time = time.time()
        print("程序结束用时%fs" % (end_time - start_time))
        return func


    def li_random(self,li):
        #将列表随机排序
        return random.shuffle(li)
    @run_time
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

    def insert_sort_gap(self,gap):
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

    # def shell_sort(self,li):
    """希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
           # 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。"""
    # li = self.li
    #     d = len(li) // 2
    #     while d >= 1:
    #         print(d)
    #         insert_sort_gap(li, d)
    #         d //= 2
    # return li

if __name__ == "__main__":
    li = [random.randint(0, 1000) for i in range(100)]
    sort = sort_obj(li)
    print(li)
    print(sort.bubble_sort())