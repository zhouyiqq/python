# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/21 20:36
li = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]
def searchMatrix(matrix,target):
    for line in matrix:
        if target in line:
            print(line)
            return True
    return False
def searchMatrix_plus(matrix,target):
    #获取二维列表的长和宽
    h = len(matrix)
    w = len(matrix[0])
    if h==0 or w==0:
        return False
    left = 0
    right = w*h-1
    while left <= right:
        """
        1 2 3 4
        5 6 7 8 
        9 10 11 12
        h=3
        w=4
        right = 11 从零开始
        一维转二维
        11 -> 2,3 11//4 11%4
        """
        mid = (left+right)//2
        i = mid//w
        j = mid%w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j]>target:
            right =mid-1
        else:
            left = mid+1
    else:
        return False
result = searchMatrix_plus(li,60)
print(result)
