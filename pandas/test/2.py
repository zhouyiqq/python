"""
填充缺失值
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'ID':['A10001', 'A10002', 'A10003', 'A10004'], 
          "Salary":[11560, np.NaN, 12988,12080]})
#用Salary字段的样本均值填充缺失值
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)