"""
删除重复值
"""
import pandas as pd
df = pd.DataFrame({"ID": ["A1000","A1001","A1002", "A1002"],
        "departmentId": [60001,60001, 60001, 60001]})
print(df.drop_duplicates())
