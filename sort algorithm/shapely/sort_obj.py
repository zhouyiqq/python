# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/12 19:48
import heapq
import random
import time
class sort_obj():
    def __init__(self,li=None):
        self.li = li

    def run_time(func):
        def wraper(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            print('%s running time %s　second' % (func.__name__, t2 - t1))
            print(result)
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

    def partition(self,li, left, right):
        tmp = li[left]#以下标为left的为基准
        while left < right:
            while left < right and li[right] >= tmp:#遍历基准left右边的所有数
                right -= 1
            li[left] = li[right]#如果右边有大于基准的数，把右边的值写到左边的空位上
            while left < right and li[left] <= tmp:#遍历基准left左边的所有数
                left += 1
            li[right] = li[left]#如果左边有小于基准的数，把左边的值写到右边的空位上
        li[left] = tmp#把tmp归位
        return left
    def quick_sort(self,li,left,right):#快速排序
        if left < right:#至少两个元素
            mid = self.partition(li,left,right)#这个函数是将选择的数归位
            self.quick_sort(li,left,mid-1)#递归左边的作为一个模块
            self.quick_sort(li,mid+1,right)#递归右边的作为一个模块
        return li
    @staticmethod
    def shift(li, low, high):
        """
        调整堆
        low:堆根结点的位置
        high：堆得最后一个元素的位置
        """
        # 用i 和 j 来记要交换的位置
        # 如果父节点是i，那么子节点是i*2+1左孩子，右孩子是i*2+2
        # 如果左孩子节点是j,那么父节点是(j-1)/2
        i = low  # 根节点
        j = 2 * i + 1  # 开始对比左孩子
        tmp = li[i]  # 把堆顶元素存起来 ,那么堆顶对应i，i永远指向空位
        while j <= high:  # 接下来用孩子与根节点对比大小，一直遍历到最后一个元素
            if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子比左孩子大，那么就将j指向右孩子，找到两个孩子里最大的那个,还要保证右孩子有
                j = j + 1  # j指向右孩子
            if li[j] > tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1  # 向下调整一层
            else:  # tmp更大，就不用交换
                break
        li[i] = tmp  # 把原来的空位补上
    @staticmethod
    def buildMaxHeap(arr):#建堆
        n = len(arr)
        for i in range((n-2)//2,-1,-1):#i表示建堆的时候调整的部分的根的下标
            sort_obj.shift(arr,i,n-1)
        # print(arr)
        #建堆完成，从最后一个非叶子结点调整，一直调整到根结点
    def heapsort(self,arr=None):#堆排序
        #时间复杂度nlogn
        #将arr视为完全二叉数
        #堆是特殊的完全二叉数
        #至下而上的搜索整个二叉树
        #找到最大的数放在堆顶，向下调整
        #从堆顶取出最大数加入到新列表中，其实没有必要占一个额外的列表，找出最大的数放在堆底，只是占位置，最后的数最大
        #再重复以上步骤
        #堆的定义，上边的比下边的大
        #选最后一个数作为棋子补根节点
        #构造堆，农村包围城市，选最后一个非叶子结点开始调整
        arr = self.li
        global arrLen #定义一个全局变量，树的结点
        arrLen = len(arr)
        sort_obj.buildMaxHeap(arr)#先建堆
        # print(self.__dict__)
        #节省内存，把堆顶元素和堆底元素进行交换，就是一个循环
        for i in range(arrLen-1,-1,-1):#i一直指向堆的最后一个元素
            arr[0],arr[i] = arr[i],arr[0]#让最后一个元素与第一个元素交换
            sort_obj.shift(arr,0,i-1)#i-1是新的high
        #i是0，堆已经空了，现在的堆已经是排好序的
        return arr
    def topk(self,k,li=None):
        if not li:
            li = self.li
        #该函数取列表li前k个大的元素
        heap = li[0:k]#取出前k个元素
        heapq.heapify(heap)#前k个元素建立一个小根堆
        for i in range(k,len(li)):
            if li[i]>heap[0]:
                heapq.heapreplace(heap,li[i])
        heap.sort()
        return heap
if __name__ == "__main__":
    li = [random.randint(0, 100) for i in range(10)]
    sort = sort_obj(li)
    print(li)
    print(sort.heapsort())
    print(sort.topk(3))


