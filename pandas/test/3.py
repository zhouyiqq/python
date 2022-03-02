"""
删除缺失值
"""
import pandas as pd
df = pd.DataFrame({"ID": ["A1000","A1001","A1002"],
         "entrytime": ["2015-05-06",pd.NaT,"2016-07-01" ]})
print(df.dropna())
