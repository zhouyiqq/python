# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/11/6 14:25
def twoSum(nums, target):
    hashmap={}#建立一个字典
    for ind,num in enumerate(nums):#将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        hashmap[num] = ind#num是数字，int是索引值
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]
if __name__ == "__main__":
    list = [2, 5, 7, 15]
    target = 9
    index = twoSum(list,target)
    print(index)