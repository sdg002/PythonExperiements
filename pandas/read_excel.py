"""
In this example we are reading an Excel table
What did we learn ?
-------------------
Reading a Table is a sensible approach
The index is an object - you may have to apply an index
Excel dates are converted to datetime64[ns]

Lesson about white space
------------------------
If there are all white spaces in the bottommost row then this is use as delimiter but this row is read
You will have to dropna

Lesson about white space
-------
If there is white space in the rows below then all columns are converted to object type
This is easy to reproduce - click on the first empty row and then type spaces and you will see the conversion

So always apply a conversion

Converting to date
------------------
You will have to eliminate rows with leading white space
    filter2=df_2["id"].astype(dtype="str").str.startswith(" ") == False
    df_2_stripped=df_2[filter2]
Then you will have to convert the date column to a strongly typed date
    df_2_date=df_2_stripped.astype({"dob": "datetime64[s]"})
"""

import logging
import os
import pandas as pd

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    source_xl_file = os.path.join(os.path.dirname(__file__), "pandas_table_demo.xlsx")
    
    logging.info(f"Going to read first table")
    df_1=pd.read_excel(io=source_xl_file, sheet_name="MyTable")
    logging.info(f"{len(df_1)} rows were read")
    logging.info(df_1.head())
    logging.info("------------------")
    logging.info("Displaying column types")
    logging.info(df_1.dtypes)

    logging.info("------------------")
    logging.info(f"Going to read second table")
    df_2=pd.read_excel(io=source_xl_file, sheet_name="MyTable2")
    logging.info(f"{len(df_2)} rows were read")
    logging.info(df_2.head(10))
    logging.info("Displaying column types")
    logging.info(df_2.dtypes)
    # Dates from Excel are read as datetime64[ns]

    # if are blank rows, then those are read as NaN, Nan, NaT
    # Nothing is read after a blank row like the one above is discovered

    # How to skip blank rows?
    logging.info("------------------")
    df_2.dropna(axis=0, how="all" ,inplace=True)
    logging.info("After dropna with axis=0")
    logging.info(df_2.head(10))
    logging.info("------------------")
    logging.info("------------------")
    df_2.dropna(axis=1, how="all" ,inplace=True)
    logging.info("After dropna with axis=1")
    logging.info(df_2.head(10))
    logging.info("------------------")
    logging.info("Displaying columns")
    logging.info(df_2.columns)
    logging.info("------------------")
    logging.info("Displaying column types")
    logging.info(df_2.dtypes)
    logging.info("------------------")
    print(df_2["dob"])
    logging.info("Stripping of leading white space")
    filter2=df_2["id"].astype(dtype="str").str.startswith(" ") == False
    df_2_stripped=df_2[filter2]
    print(df_2_stripped)
    logging.info("------------------")

    #df_2_date=df_2_stripped["dob"].astype(dtype="datetime64[s]")
    df_2_date=df_2_stripped.astype({"dob": "datetime64[s]"})
    #df_2_date=df_2_stripped
    logging.info("Converting to date")
    print(df_2_date.head(10))
    logging.info("------------------")
    logging.info(df_2_date.dtypes)


    pass
