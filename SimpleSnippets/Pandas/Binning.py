import unittest
import pandas as pd
import numpy as np
from Common import PrintHorLine

print("Create DataFrame by specifying dictionary")
df = pd.DataFrame([
                    {'Price': 10, 'Cat': 'food', 'Qty': 2},
                    {'Price': 20, 'Cat': 'toy', 'Qty': 4},
                    {'Price': 15, 'Cat': 'food', 'Qty': 5},
                    {'Price': 12, 'Cat': 'food', 'Qty': 7}
                    ],
                    )

input_series=df["Qty"]
df["bins"]=pd.cut(bins=[1,4.5,8],x=input_series)
df["bins_equal"]=pd.cut(bins=2,x=input_series)

print(df)

#
#Group by bins
#
bins2=pd.cut(bins=2,x=input_series)
groups1=df.groupby(bins2)
a=groups1.agg({"Price":[sum]})
print(a)
#
#Group by bins and Cat
#
bins2=pd.cut(bins=2,x=input_series)
groups2=df.groupby(["Cat",bins2])
print(groups2)

pass
