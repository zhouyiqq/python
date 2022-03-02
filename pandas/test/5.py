"""
修改数据类型
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname": [" Zhao ","Qian"," Sun " ]})
#将ID列的类型转化为字符串的格式
print(df["ID"].astype(str))
