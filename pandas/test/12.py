"""
记录的合并
"""
import pandas as pd
df1 = pd.DataFrame({"ID": ["A10006","A10001"],"Salary": [12000, 20000]})
df2 = pd.DataFrame({"ID": ["A10008"], "Salary": [10000]})
#使用concat()函数将df1与df2的记录进行合并
data = pd.concat([df1, df2])
print("\n记录的合并\n",data)