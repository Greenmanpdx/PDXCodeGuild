import PyPDF2


pdfFileObj = open('bestiary.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
