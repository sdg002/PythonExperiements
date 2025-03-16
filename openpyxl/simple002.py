#
#Populate multiple columns, find the Cell header and direct data accordingly
#We are expecting a certain columns in the Header row (ID,FirstName, LastName)
#We do not care about the order
#Determine the position and then write the 
#


import os
import openpyxl as pyxl
import openpyxl.worksheet.worksheet as ws
import random

def read_header_row(source_excel_filename: str):
    wb = pyxl.load_workbook(filename=source_excel_filename)
    print("Displaying all Sheets")
    print(wb.sheetnames)
    sheet_index= wb.sheetnames.index("simple002")
    sheet: ws.Worksheet= wb.worksheets[sheet_index]
    header_row = sheet[1]
    header_dict={}
    for cell in header_row:
        print(f"Column={cell.column} , Value={cell.value}")
        header_dict[cell.value]=cell.column
    
    #column_header_tuples = [(cell.column,cell.value) for cell in header_row if True]
    #return column_header_tuples
    return header_dict
    

def populate_table(source_excel_filename:str, dest_excel_filename: str, sheet_name: str, header_dict: dict[str,int]):
    wb = pyxl.load_workbook(filename=source_excel_filename)    
    sheet: ws.Worksheet= wb.worksheets[wb.sheetnames.index(sheet_name)]

    max_count=10 + random.randint(3,9)
    for index in range(0,max_count):
        id=100+index
        first_name = f"John_{id}"
        last_name = f"Doe_{id}"
        row=index+2
        sheet.cell(row=row, column=header_dict['ID']).value=id
        sheet.cell(row=row, column=header_dict['FirstName']).value=first_name
        sheet.cell(row=row, column=header_dict['LastName']).value=last_name
    wb.save(filename=dest_excel_filename)
    print(f"Done with populat.wion, rows={max_count}")

if __name__ == "__main__":
    source_xl_file = os.path.join(os.path.dirname(__file__), "demopythonexcel.xlsx")
    dest_xl_file= os.path.join(os.path.dirname(__file__), "demopythonexcel-new.xlsx")

    header_row_dictionary=read_header_row(source_excel_filename=source_xl_file)
    print(header_row_dictionary)
    populate_table(source_excel_filename=source_xl_file, dest_excel_filename=dest_xl_file, sheet_name='simple002', header_dict=header_row_dictionary)