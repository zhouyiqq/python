# _*_coding:utf_8_*_
# pythonProject1 was created by zy on 2021/10/17 16:06
def select_sort_simple(li):
    '''简单选择排序'''
    li_new = []
    for i in range(len(li)):
        min_val = min(li)#寻找列表最小的值
        li_new.append(min_val)#在新列表添加最小的值
        li.remove(min_val)#从列表中删除最小的值
    return li_new#返回排序好的新列表
def select_sort(li):
    '''不开辟新的空间，寻找无序列表列表中的最小的数依次交换位置进行排序'''
    for i in range(len(li)-1):#不遍历列表最后一个元素
        min_loc = i#标记最小的数
        for j in range(i+1,len(li)):#在无序列表中遍历
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]#将无序列表最小的那个数交换位置
    return li
li=[3,4,2,1,5,6,8,7,9]
#print(select_sort_simple(li))
print(select_sort(li))