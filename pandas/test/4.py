import pandas as pd
import numpy as np

df = pd.DataFrame({"ID":[100000,100101,100201], "Surname":["Zhao","Qian","Sun"]})
print(df.dtypes)
print()
print(df["ID"].dtype)