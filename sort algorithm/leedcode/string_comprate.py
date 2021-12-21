# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/21 20:26
s = "anagram"
t = "nagaram"
s1 = "rat"
t1 = "car"
def compare(s,t):
    #首先看两个字符串的长度是否一样
    #然后匹配两个字符串里相同的部分
    #最后比较剩余的部分是否一张，一致返回Ture否则返回flase
    if len(s) == len(t):
        swith = [0 for _ in range(len(t))]
        index = []
        for i in range(len(s)):
            for j in range(len(t)):
                if j not in index:
                    if s[i] == t[j]:
                        swith[j] = 1
                        index.append(j)
        if all(swith):
            return True
        else:
            return False

    else:
        return False
c = compare(s1,t1)
print(c)