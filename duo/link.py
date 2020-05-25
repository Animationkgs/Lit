



import json
from bs4 import BeautifulSoup as b

#a= requests.get('file:///sdcard/Download/sync/Lit/duo/a.html')
s= open('a.html').read().encode('utf8')
s= b(s,'html.parser')
s= s.find_all('a')
#s= str(s)
#s= json.dumps(s)
#s= json.load's(s)
for x in s:
    print (x['href'])
