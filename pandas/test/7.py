"""
字段的拆分
"""
import pandas as pd
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
#对Surname_Age字段进行拆分
df_new = df["Surname_Age"].str.split("_", expand =True)
print(df_new)
