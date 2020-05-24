import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('filename.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
number_pages=pdfReader.numPages
print(pdfReader.numPages) 
  
# creating a page object
count=0
count_1=0 
for i in range(2,number_pages):
    pageObj = pdfReader.getPage(i) 

# extracting text from page 
    requiremt_extract=pageObj.extractText()
    print(requiremt_extract)
#    a=requiremt_extract.split('\n' or '.')
#    for section_number in a:
#        if len(section_number)<=3:
#            for dot in section_number:
#                if dot == '.':
#                    try:
#                        if(int(section_number[:-1])):
#                            count=int(section_number[:-1])
#                            print(section_number[:-1])
#                            
#                    except:
#                        if len(section_number)==2:
#                            section_number=str(count)+'.'+section_number
#                            print(section_number[:-1])


  
# closing the pdf file object 
pdfFileObj.close()
