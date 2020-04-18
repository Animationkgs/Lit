


f= open('speckled.js', 'rb')
s= f.read().decode('latin1')
from nltk.tokenize import sent_tokenize as st
for x in st(s):
    print (x)
    print ('\n\n\n')
