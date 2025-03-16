#
#Just populating a single column
#


import os
import openpyxl as pyxl
import openpyxl.worksheet.worksheet as ws
import numpy as np

def populate_single_column_on_sheet(source_excel_filename: str, dest_excel_filename: str):
    wb = pyxl.load_workbook(filename=source_excel_filename)
    print("Displaying all Sheets")
    print(wb.sheetnames)
    sheet_index= wb.sheetnames.index("simple001")
    sheet: ws.Worksheet= wb.worksheets[sheet_index]
    max_items= 30
    rng = np.random.default_rng()
    random_strings = [f"hello_{x}" for x in rng.integers(low=1,high=10, size=max_items) if True]
    print(f"Got hold of sheet:{sheet}")
    print(f"Going to print random string: {random_strings}")
    for row in range(2,max_items+1):
        c=sheet.cell(row=row, column=1)
        c.value = random_strings[row-2]
        print(f"Row={row}, Value={c.value}")

    wb.save(filename=dest_excel_filename)
    print("helo")

if __name__ == "__main__":
    source_xl_file = os.path.join(os.path.dirname(__file__), "demopythonexcel.xlsx")
    dest_xl_file= os.path.join(os.path.dirname(__file__), "demopythonexcel-new.xlsx")

    populate_single_column_on_sheet(source_excel_filename=source_xl_file, dest_excel_filename=dest_xl_file)