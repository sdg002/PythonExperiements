import os
import openpyxl as pyxl
import openpyxl.worksheet.worksheet as ws

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
    
    return header_dict

def clear_columns(source_excel_filename:str, dest_excel_filename: str, sheet_name: str, header_dict: dict[str,int]):
    print(f"Going to clear cells in file: {source_excel_filename}")
    wb = pyxl.load_workbook(filename=source_excel_filename)    
    sheet: ws.Worksheet= wb.worksheets[wb.sheetnames.index(sheet_name)]


    range = sheet["A2":]    
    # column_names = header_row_dictionary.keys()
    # for column_name in header_row_dictionary:
    #      column_index=header_row_dictionary[column_name]
    #      print(f"Going to clear the content of column:{column_name} at index:{column_index} ")
    #     #sheet.(column=column_index)
    #     sheet[]

    pass


if __name__ == "__main__":
    source_xl_file = os.path.join(os.path.dirname(__file__), "demopythonexcel.xlsx")
    dest_xl_file= os.path.join(os.path.dirname(__file__), "demopythonexcel-new.xlsx")

    header_row_dictionary=read_header_row(source_excel_filename=source_xl_file)
    clear_columns(source_excel_filename=source_xl_file, dest_excel_filename=dest_xl_file, header_dict=header_row_dictionary, sheet_name='simple002')