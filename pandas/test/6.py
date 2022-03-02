"""
字段的抽取
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname": [" Zhao ","Qian"," Sun " ]})
#需要将ID列的类型转换为字符串, 否则无法使用slice()函数
df["ID"]= df["ID"].astype(str)
#抽取ID前两位
data = df["ID"].str.slice(0,2)
print(data)