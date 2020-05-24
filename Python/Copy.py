#from xlutils modules I will call copy class
from xlutils.copy import copy
#make a writable copy of the opened excel file
Write_workbook=copy(Read_workbook1)
#Read the first sheet to write to within the writable copy
Write_sheet=Write_workbook.get_sheet(0)
#write the text first row and 9th column (Give Title)
Write_sheet.write(1,1 ,"Required_ID")
