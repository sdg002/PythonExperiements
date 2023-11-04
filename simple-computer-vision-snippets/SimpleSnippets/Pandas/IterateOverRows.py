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

print("Displaying columns")
print(df.columns)
print(df.head())
PrintHorLine()
print("Iterate over columns, display only")

for index,row in df.iterrows():
    print("index=%d Price=%f" % (index,row["Price"]))

PrintHorLine()
print("Iterate and update a column")
for index,row in df.iterrows():
    print("index=%d Price=%f" % (index,row["Price"]))
    price=row["Price"]
    #row["Price"]=price+200
    #df.iloc[index]["Price"]=price+200
    df.at[index,"Price"]=(price+200)

print("Display results")
print(df.head())

PrintHorLine()

