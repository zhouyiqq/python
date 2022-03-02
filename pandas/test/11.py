"""
记录的抽取
"""
# 1) 关系运算: df[df.字段名 关系运算符 数值], 比如抽取年龄大于30岁的记录.
import pandas as pd
import numpy as np
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
print("\n源数据\n",df)
df_new = df["Surname_Age"].str.split("_", expand =True)
df_new.columns = ["Surname","Age"]
df_mer= pd.merge(df, df_new, left_index =True, right_index=True)
df_mer.drop("Surname_Age", axis = 1, inplace =True)
#将Age字段数据类型转化为整型
df_mer["Age"] = df_mer["Age"].astype(int)
#抽取Age中大于30的记录
data = df_mer[df_mer.Age > 30]
print("\n关系运算\n",data)

# 2) 范围运算: df[df.字段名.between(s1, s2)], 注意既包含s1又包含s2, 比如抽取年龄大于等于23小于等于28的记录. 
data = df_mer[df_mer.Age.between(23,28)]
print("\n范围运算\n",data)
# 3) 逻辑运算: 与(&) 或(|) 非(not)

#比如上面的范围运算df_mer[df_mer.Age.between(23,28)]就等同于df_mer[(df_mer.Age >= 23) & (df_mer.Age <= 28)]
 
data = df_mer[(df_mer.Age >= 23 ) & (df_mer.Age <= 28)]
print("\n逻辑运算\n",data)

#4) 字符匹配: df[df.字段名.str.contains("字符", case = True, na =False)] contains()函数中case=True表示区分大小写, 默认为True; na = False表示不匹配缺失值.
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28"],"SpouseAge":[np.NaN,"32",np.NaN]})
#匹配SpouseAge中包含2的记录
data = df[df.SpouseAge.str.contains("2",na = False)]
print("\n字符匹配\n",data)

#5) 缺失值匹配:df[pd.isnull(df.字段名)]表示匹配该字段中有缺失值的记录.
df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28"],"SpouseAge":[np.NaN,"32",np.NaN]})
#匹配SpouseAge中有缺失值的记录
data = df[pd.isnull(df.SpouseAge)]
print("\n缺失值匹配\n",data)
