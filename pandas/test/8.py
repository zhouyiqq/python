"""
字段的命名
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
#第一种方法使用rename()函数
# df_new = df["Surname_Age"].str.split("_", expand =True).rename(columns={0: "Surname", 1: "Age"})
#第二种方法直接设置columns参数
df_new = df["Surname_Age"].str.split("_", expand =True)
df_new.columns = ["Surname","Age"]
print(df_new)
