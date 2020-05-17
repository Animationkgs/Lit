


import PyPDF2
p= open('a.pdf', 'rb')
pr= PyPDF2.PdfFileReader(p);
print (pr.numPages)

for i in range(0,pr.numPages):
    po= pr.getPage(i);
    print (po.extractText())
p.close();
