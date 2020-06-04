

import re
def makekey(tc,rc):
    return '{}.{}'.format(str(tc),str(rc).zfill(2))

def vdota(v):
    return v.a.text

def getdata(tables):
    ret= {}
    tablecount= -1
    for table in tables:
        tablecount+= 1
        if tablecount==0: continue
        if tablecount==8:
            print(table)
            continue
        rows= table.find_all('tr')
        rowcount= -1
        header= []
        for row in rows:
            rowcount+= 1
            if rowcount==0:
                headers= row
                #print (headers)
                header= [str(x.text).replace('<','---') for x in headers]
                #print (tablecount, header)
            else:
                key= makekey(tablecount-1, rowcount)
                values= list(row)
                if tablecount==1 and rowcount==1:
                    values[0]= vdota(values[0])
                    values[1]= vdota(values[1])
                    values[2]= vdota(values[2])
                    values[3]= values[3].text
                if tablecount==1 and rowcount==2:
                    values[0]= values[0].text
                if tablecount in [2,3,4,5,6,7]:
                    values= [x.text for x in values]
                #print (values)
                value= [str(x) for x in values]
                value= [x.replace('<','---') for x in value]
                #print (rowcount, key, value)
                d= {k:v for k,v in zip(header,value)}
                if tablecount in [2,3,4,5,6,7]:
                    d['title']= d['Title']
                d['id']= 'blank'
                ret[key]=d
            #if rowcount==3: break
        if tablecount==9: break
    ret['0.01']['title']= 'Pilot'
    ret['0.01']['Description']= ret['0.02']['Title']
    del ret['0.02']
    return ret


t= open('t.html','rb').read().decode('latin1')
from bs4 import BeautifulSoup as bs
b= bs(t)
tables= b.find_all('table')


def write(ret):
    out= 'var w= {};'.format(ret)
    b= open('out.json', 'w')
    b.write(out)
    b.close()

ret= getdata(tables)
ret['title']= 'Leave It to Beaver'
ret['Original air date']= '1957-1963'
write(ret)
