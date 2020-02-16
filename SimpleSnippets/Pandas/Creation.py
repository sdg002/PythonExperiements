import unittest
import pandas as pd
import numpy as np
from Common import PrintHorLine

#
#Very basic creation - specify all data at the time of creation
#
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

#
#Creation by specifying column types
#
PrintHorLine()
print("Create DataFrame by specifying column types")
columns_spec={ 
                "Price": pd.Series([], dtype='float' ) ,
                "Cat": pd.Series([], dtype="str"),
                "Qty": pd.Series([], dtype='float' ) 
            }
df = pd.DataFrame(columns_spec)
print(df.columns)
print(df.head())
PrintHorLine()
#
#Adding rows to empty data frame using loc
#
print("Append row to empty data frame - using loc method")
df.loc[len(df)]=[11,"toy",1]
df.loc[len(df)]=[13,"food",3.5]
print(df)
PrintHorLine()
#
#Add rows to using a new DataFrame
#
print("Append row using append() method")
new_record={
        "Price": [11] , 
        "Cat": ["food"], 
        "Qty":[110]
        }
df_temp=pd.DataFrame(new_record)
df=df.append(df_temp,ignore_index=True)
print(df)
PrintHorLine()

