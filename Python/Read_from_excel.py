'''
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = (r"C:/Users/Desktop/vivek_office/Read_excel.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(0,0))
'''
'''
#Extracting no of rows
print(sheet.nrows)

#Extracting no of column
print(sheet.ncols)

#Extracting all rows
for row in range(sheet.nrows):
    print(sheet.cell_value(row,0))

#Extracting all column

for col in range(sheet.ncols):
    print(sheet.cell_value(0, col))

#Extract a particular row value

print(sheet.row_values(1))

#Extract a particular column value

print(sheet.col_values(1))

'''


import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[,.]", ":", text))

print("light rain event".replace(' ', '_'))































