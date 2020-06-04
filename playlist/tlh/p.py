





t= open('t.html','rb').read().decode('latin1')
from bs4 import BeautifulSoup as bs
b= bs(t)
tables= b.find_all('table')
tablecount= -1

import re
def dxdd(v):
    m= re.search('\dx\d\d',v)
    if m:
        k= m.group()
        key= k.replace('x','.')
        return key
    return None

def wdwdd(v):
    m= re.search('Season \d',v)
    if m:
        season= m.group().split(' ')[-1]
        m= re.search('Episode \d+',v)
        episode= m.group().split(' ')[-1].zfill(2)
        key= '{}.{}'.format(season,episode)
        return key
    return None
def getkey(v):
    key= dxdd(v)
    if not key:
        key= wdwdd(v)
    return key

def makekey(tc,rc):
    return '{}.{}'.format(str(tc),str(rc).zfill(2))

ret= {}
for table in tables:
    tablecount+= 1
    if tablecount==0: continue
    rows= table.find_all('tr')
    rowcount= -1
    header= []
    for row in rows:
        rowcount+= 1
        if rowcount==0:
            headers= row.find_all('th')
            header= [x.text.lstrip().rstrip() for x in headers]
            print (tablecount, header)
        else:
            key= makekey(tablecount, rowcount)
            values= row.find_all('td')
            value= [x.text.lstrip().rstrip() for x in values]
            d= {k:v for k,v in zip(header,value)}
            d['id']= 'blank'
            d['title']= d['Title']
            ret[key]=d


t= open('listtlh', 'rb').read().decode('latin1').split('\n')
for v in t:
    if len(v)==0: continue
    key= getkey(v)
    idv= v[-15:][:11]
    print (key,idv)
    ret[key]['id']= idv

for k,v in ret.items():
    if not v['id']=='blank':
        if len(v['id'])==11:
            v['title']= '<span style="background-color: green;">{}</span>'.format(v['title'])
        else:
            v['title']= '<span style="background-color: yellow;">{}</span>'.format(v['title'])

ret['title']= 'The Littlest Hobo 1979-1985'

def prettyvtt (t):
    xs= t.split( '\n' )
    ret= []
    for x in xs:
        if len(x)== 0: continue
        r= re.findall('^\d\d:\d\d',x)
        if r: continue
        r= re.findall('^\s*$',x)
        if r: continue
        v= re.sub('<\d\d:\d\d:\d\d.\d\d\d>', '', x)
        v= re.sub('<c>', '', v)
        v= re.sub('<\/c>', '', v)
        #curr= re.split('\W+', v)
        if len(ret)>0:
            if ret[-1]==v:
                continue
        ret.append(v)
    return '<br>'.join(ret)

t= open('listtlhvtt', 'rb').read().decode('latin1').split('\n')
for v in t:
    if len(v)==0: continue
    print (v)
    key= getkey(v)
    print (key)
    idv= v[-18:][:11]
    s= open(v,'rb').read().decode('latin1')
    ret[key]['subtitles']= prettyvtt(s)


out= 'var w= {};'.format(ret);
b= open('out.json', 'w')
b.write(out)
b.close()

