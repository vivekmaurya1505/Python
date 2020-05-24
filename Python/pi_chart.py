
# import xlsxwriter module
import xlsxwriter


# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook("chart_pie.xlsx")


# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()


# here we create bold format object .
bold = workbook.add_format({'bold':1})


# this is our data with data list
headings = ['Category', 'Values']

data = [

    ['Apple', 'Cherry', 'Banana'],
    [50, 40, 10],

]

# Write a row of data starting from 'A1'
# with bold format.
worksheet.write_row('A1', headings, bold)


# Write a column of data starting from
# A2, B2, C2 respectively.
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])


#this is the type of chart
chart1 = workbook.add_chart({'type': 'pie'})

# Add a data series to a chart
chart1.add_series({
    'name':'Pie Sales Data',
     'categories':['Sheet1', 1,0,3,0],
     'values':['Sheet1', 1,1,3,1],


})



#set the title for the chart
chart1.set_title({'name':'Fruits Data Chart'})

#set the style for the chart
chart1.set_style(10)

#insert chart to the worksheet
worksheet.insert_chart('C2', chart1, {'x_offset':25, 'y_offset':10})

#close the workbook
workbook.close()
