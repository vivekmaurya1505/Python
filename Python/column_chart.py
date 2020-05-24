from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
wb = Workbook(write_only=True)
ws = wb.create_sheet()
rows = [
('Number', '', ''),
("Total Number \nof System \nRequirement", 10),
("Total Number \nOf Requirement \nCovered", 50)

]
for row in rows:
    ws.append(row)
    
chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "System requirment Coverage"
chart1.y_axis.title = 'Test number'
#chart1.x_axis.title = 'Sample length (mm)'
data = Reference(ws, min_col=2, min_row=1, max_row=4, max_col=2)
cats = Reference(ws, min_col=1, min_row=2, max_row=3)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
#chart1.shape = 4
ws.add_chart(chart1, "G10")
wb.save("bar.xlsx")

