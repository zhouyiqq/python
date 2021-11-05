# _*_coding:utf_8_*_
# pythonProject1 was created by zy on 2021/10/17 17:18
def partition(li,left,right):
    '''归位函数'''
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
    li[left] = li[right]
    while left < right and li[left] <= tmp:
        left += 1
    li[left] = tmp
li = [5,7,4,6,3,1,2,9,8]
print(li)
partition(li,0,len(li)-1)
print(li)