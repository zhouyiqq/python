import pymysql
print("查询某up主的粉丝性别构成(UID)：")
uid = input()
db = pymysql.connect(host='localhost', user='root', password='',
                         port=3306, db='bilibili')
cursor = db.cursor()
sql = "select count(fans.sex) from up inner join fans on up.up_id=fans.up_id " \
      "where up.up_id = '"+ uid +"' group by fans.sex"
cursor.execute(sql)
results = cursor. fetchall()
print("保密、男、女 个数分别为："+str(results))
print("请输入匹配规格：粉丝数，播放数，点赞数；<，>；数字(万)")
string = ''
input = input()
split1 = input[0:3]
split2 = input[3:4]
split3 = input[4:]
if(split1 == '粉丝数'):
    string += 'fans'
elif(split1 == '播放数'):
    string += 'view'
else:
    string += 'praise'
if(split2 == '<'):
    string += '<'
else:
    string += '>'
string += split3
sql = 'select * from up where '+string
cursor.execute(sql)
results = cursor. fetchall()
print(results)
db.close()