# import xlrd
# from openpyxl.workbook import Workbook
# from openpyxl.reader.excel import load_workbook, InvalidFileException

# def open_xls_as_xlsx(filename):
#     # first open using xlrd
#     book = xlrd.open_workbook(filename)
#     index = 0
#     nrows, ncols = 0, 0
#     while nrows * ncols == 0:
#         sheet = book.sheet_by_index(index)
#         nrows = sheet.nrows
#         ncols = sheet.ncols
#         index += 1

#     # prepare a xlsx sheet
#     book1 = Workbook()
#     sheet1 = book1.get_active_sheet()

#     for row in xrange(0, nrows):
#         for col in xrange(0, ncols):
#             sheet1.cell(row=row, column=col).value = sheet.cell_value(row, col)

#     return book1

# open_xls_as_xlsx('./2015_01_03.xls')

# conda install -c conda-forge pyexcel 
# conda install -c conda-forge pyexcel-xlsx 
# conda install -c conda-forge pyexcel-xls 

# import pyexcel as p 

# p.save_book_as(file_name='2015_01_03.xls', dest_file_name='2015_01_03.xlsx')



# import os
# import win32com.client
# xl = win32com.client.Dispatch("Excel.Application")
# path =  os.getcwd().replace('\'','\\') + '\\'
# print(path)
# wb = xl.Workbooks.Open(path+"2015_01_03.xls")
# wb.SaveAs(path+"2015_01_03.xlsx", FileFormat = 51)
# wb.Close()
# xl.Quit()


import os
import win32com.client
import time
# xl = win32com.client.Dispatch("Excel.Application")
# path =  os.getcwd().replace('\'','\\') + '\\'
# print(path)
# wb = xl.Workbooks.Open(path+"2015_01_03.xls")
# wb.SaveAs(path+"2015_01_03.xlsx", FileFormat = 51)
# wb.Close()
# xl.Quit()

path = 'C:/Users/admin/Downloads/'
startday = '2015-01-01'
name = 'pear'

xl = win32com.client.Dispatch("Excel.Application")
path = path.replace('/','\\')
print(f'{path}{startday}_{name}.xls')

wb = xl.Workbooks.Open(f'{path}{startday}_{name}.xls')
wb.SaveAs(f'{path}{startday}_{name}.xlsx', FileFormat = 51)
wb.Close()
xl.Quit()
time.sleep(1)