"""
字段的删除
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
df_new = df["Surname_Age"].str.split("_", expand =True)
df_new.columns = ["Surname","Age"]
df_mer= pd.merge(df, df_new, left_index =True, right_index=True)
#drop()删除字段,第一个参数指要删除的字段,axis=1表示字段所在列,inplace为True表示在当前表执行删除.
df_mer.drop("Surname_Age", axis = 1, inplace =True)
print(df_mer)
