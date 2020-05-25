


import sys, PyPDF2
a= sys.argv[1]
print (a)
a= 'U5FF80.pdf'
p= open(a, 'rb')
pr= PyPDF2.PdfFileReader(p);
print (pr.numPages)

for i in range(0,pr.numPages):
    po= pr.getPage(i);
    print (po.extractText())
p.close();
