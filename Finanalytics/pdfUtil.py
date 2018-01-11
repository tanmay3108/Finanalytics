# importing required modules
from PyPDF2 import PdfFileReader, PdfFileWriter

import os
import json

#module_dir = os.path.dirname(__file__)  # get current directory
#print module_dir
#fund_name ='axis_long_term.pdf'
#fund_name ='uti.pdf'
fund_name = 'mf_details.pdf'
file_path = os.path.join("C:/Users/Tanmay/PycharmProjects/Finanalytics/docs", fund_name)
print file_path




# creating a pdf file object
pdfFileObj = open(file_path, 'rb')

# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObj)
#print pdfReader.isEncrypted
#pdfReader.decrypt('12345678')
print pdfReader.isEncrypted


# printing number of pages in pdf file
print(pdfReader.numPages)
print (pdfReader.getDocumentInfo())
# creating a page object

pageObj = pdfReader.getPage(0)



# extracting text from page
print(pageObj.extractText())
pageObj = pdfReader.getPage(1)
print(pageObj.extractText())



# closing the pdf file object
pdfFileObj.close()
