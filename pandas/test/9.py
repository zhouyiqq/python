"""
字段的合并
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
df_new = df["Surname_Age"].str.split("_", expand =True)
df_new.columns = ["Surname","Age"]
 #使用merge函数对两表的字段进行合并操作.
p = pd.merge(df, df_new, left_index =True, right_index=True)
print(p)
