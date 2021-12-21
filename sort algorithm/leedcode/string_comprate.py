# _*_coding:utf_8_*_
# python代码仓库 was created by zy on 2021/12/21 20:26
import time
def run_time(func):
    def wraper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time %s　second' % (func.__name__, t2 - t1))
        # print(result)
        return result

    return wraper
@run_time
def compare(s,t):#判断t是不是s的重新排列组合
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
@run_time
def isequality(s,t):
    # print(list(s))
    # print(sorted(list(s)))
    return sorted(list(s))==sorted(list(t)) #排完序看看两个队列是否相等
def isequarity_dict(s,t):
    dict1 = {}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch,0)+1#如果dict[ch]不存在则返回dict[0]，key是字母，value是字母出现的次数
        print(ch,dict1[ch])
    for ch in t:
        dict2[ch] = dict2.get(ch,0)+1
        print(ch, dict2[ch])
    print(dict1)
    print(dict2)
    return dict1==dict2#dict1和dict2是统计字母出现的次数
s = "anagram"
t = "nagaram"
s1 = "rat"
t1 = "car"
# c = compare(s,t)
# d = isequality(s,t)
# print(c)
# print(d)
e = isequarity_dict(s1,t1)
print(e)