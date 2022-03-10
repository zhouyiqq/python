# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/10 13:01
table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608
def dec(x):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor
def enc(x):#这个代码是oid转bv
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)
# av339530147
# BV1pR4y1G7UC
# print(dec("BV1pR4y1G7UC"))
bv ="BV1pR4y1G7UC"
av = f"AV{dec(bv)}"
oid = dec(bv)
print(bv)
print(av)
print(oid)