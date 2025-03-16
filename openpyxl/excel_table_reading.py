import os
import sys
import logging
import pandas as pd
import openpyxl as pyxl
import openpyxl.worksheet.worksheet as ws
import openpyxl.worksheet.table as tbl
import openpyxl.worksheet.cell_range as cell_range
from openpyxl.cell.cell import Cell


"""
This works - we are getting the table range
and then iterating row by row
if the first cell of any row is blank then we consider that to be the end of the Table

Drawback:
It takes about 10 seconds at the line where we are extrating the range object out of the sheet
"""
def read_table(source_excel_filename: str, sheet_name: str, table_name: str)->pd.DataFrame:
    wb = pyxl.load_workbook(filename=source_excel_filename)
    logging.info("Got work book instance")
    sheet_index = wb.sheetnames.index(sheet_name)
    sheet: ws.Worksheet= wb.worksheets[sheet_index]
    logging.info(f"Got an instance to the sheet {sheet}")
    table: tbl.Table = sheet.tables[table_name]
    logging.info(f"Got an instance to the table {table}")
    logging.info(f"Column names are: {table.column_names}")
    logging.info(f"{table.displayName=}")
    logging.info(f"Cell range={table.ref}")
    table_cell_range: cell_range = table.ref
    for row in sheet[table_cell_range]:
        first_cell: Cell = row[0]
        if not first_cell.value:
            break
        logging.info(f"{row=}")
        for cell in row:
            cell_value = cell.value
            logging.info(f"{cell_value=}")
            
        logging.info("------------------------")
    #
    #you were here, try following this for reading Excel table into
    # https://stackoverflow.com/questions/63452609/openpyxl-read-table-to-python
    # https://stackoverflow.com/questions/24429902/loop-through-each-row-in-a-table
    #
    pass


def read_table_with_iterrows(source_excel_filename: str, sheet_name: str, table_name: str)->pd.DataFrame:
    wb = pyxl.load_workbook(filename=source_excel_filename)
    logging.info("Got work book instance")
    sheet_index = wb.sheetnames.index(sheet_name)
    sheet: ws.Worksheet= wb.worksheets[sheet_index]
    logging.info(f"Got an instance to the sheet {sheet}")
    table: tbl.Table = sheet.tables[table_name]
    logging.info(f"Got an instance to the table {table}")
    logging.info(f"Column names are: {table.column_names}")
    logging.info(f"{table.displayName=}")
    logging.info(f"Cell range={table.ref}")
    table_cell_range: cell_range = table.ref
    for row in sheet[table_cell_range]:
        first_cell: Cell = row[0]
        if not first_cell.value:
            break
        logging.info(f"{row=}")
        for cell in row:
            cell_value = cell.value
            logging.info(f"{cell_value=}")
            
        logging.info("------------------------")
    #
    pass

    

def list_all_excel_tables(source_excel_filename: str)->None:
    wb = pyxl.load_workbook(filename=source_excel_filename)
    logging.info("Got work book instance")
    for sheet_name in wb.sheetnames:
        logging.info(f"sheet={sheet_name}")
        sheet_index= wb.sheetnames.index(sheet_name)
        sheet: ws.Worksheet= wb.worksheets[sheet_index]
        tables=sheet.tables
        for table in sheet.tables:
            logging.info(f"Got a table {table}")
        logging.info("----")
    return None



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Hello world. In this example we will demonstrate how to read an Excel file")
    logging.info(f"The current Python interpreter is {sys.executable}")
    logging.info("Done")
    source_xl_file = os.path.join(os.path.dirname(__file__), "excel_tables/table_demo.xlsx")
    logging.info(f"Going to read the file: {source_xl_file}")
    list_all_excel_tables(source_excel_filename=source_xl_file)
    list_all_(source_excel_filename=source_xl_file)
    read_table(source_excel_filename=source_xl_file, sheet_name="MyTable", table_name="Table1")

