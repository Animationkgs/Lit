

import re
def ddotdd(v):
    m= re.search('\d\.\d\d',v)
    if m:
        key= m.group()
        return key
    return None
def dddd(v):
    m= re.search('\d\d\d\d',v)
    if m:
        k= m.group()
        season= k[:2][-1]
        episode= k[-2:]
        return '{}.{}'.format(season,episode)
    return None

def getkey(v):
    key= ddotdd(v)
    if not key:
        key= dddd(v)
    return key


t= open('t.html', 'rb').read()
t= t.decode('latin1')

from bs4 import BeautifulSoup as bs
b= bs(t)

field= 'num title directed written aired desc'.split(' ')

tx= b.find_all('table')
xc= -1
row= []
for x in tx:
    xc+= 1
    if xc==0: continue
    if xc==1: continue
    ys= x.find_all('tr')
    yc= -1
    for y in ys:
        yc+= 1
        zs= y.find_all('td')
        res= [str(z) for z in zs]
        if len(res)>0:
            row.append(res) 

def make(x,y):
    num,title,directed,written,aired= x
    ret= { 'num': num }
    ret['title']= title
    ret['directed']= directed
    ret['written']= written
    ret['aired']= aired
    ret['desc']= y[0]
    return ret
row1= [x for i,x in enumerate(row) if i%2==0]
row2= [x for i,x in enumerate(row) if i%2==1]
row= [ make(x,y) for x,y in zip(row1,row2) ]
for i,x in enumerate(row):
    season= str(int(i/24.0)+1)
    num= str((i%24)+1).zfill(2)
    x['key']= '{}.{}'.format(season,num)
    x['id']= 'blank'

w= { x['key']:x for x in row }
def join(d1,d2):
    ret= { k:v for k,v in d1.items() }
    for k,v in d2.items():
        ret[k]= v
    return ret


def tbd(kv):
    k,v= kv.split(' ')
    w[k]['id']= 'tbd {}'.format(v)

tbd( '2.01 itUR48waCns' )
tbd( '2.08 HOI25XxgySE' )
tbd( '3.06 jOGZ5SMmVPc' )
tbd( '1.08 uaZkD7IbGiw' )
tbd( '2.16 j6WvoVchHXg' )
tbd( '1.03 e9zJiaD1r7w' )
tbd( '1.05 9Vu4Bt3tacY' )
tbd( '1.07 https://www.youtube.com/watch?v=1HZD34yxiNY' )
tbd( '1.09 https://www.youtube.com/watch?v=i5Iu546YulQ' )
tbd( '1.11 https://www.youtube.com/watch?v=QLWqUE-7LaU' )


t= open('listmsi', 'rb').read().decode('latin1').split('\n')
for v in t:
    if len(v)==0: continue
    k= v[-20:][:4]
    idv= v[-15:][:11]
    print (idv)
    w[k]['id']= idv

w['title']= 'My Secret Identity 1988-1991'

w['voyager reunites']= 'https://ohnotheydidnt.livejournal.com/118071255.html'
w['kid francescoli italia 90']= 'xifnM2pGAYQ'
w['kid francescoli disco queen']= '5AyBFWyY0lQ'

import re

def prettyvtt (t):
    xs= t.split( '\n' )
    ret= []
    for x in xs:
        if len(x)== 0:
            ret.append(x)
            continue
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

def pretty (x):
    return '<br>'.join(x.split( '\n' ))

import os
def putsubs():
    vtt= [[x for x in f if x[-4:]=='.vtt'] for r,d,f in os.walk('json') if r=='json'][0]
    vtt= [(getkey(x),x) for x in vtt]
    d= { k:v for k,v in vtt }
    txt= [[x for x in f if x[-4:]=='.txt'] for r,d,f in os.walk('json') if r=='json'][0]
    txt= [(getkey(x),x) for x in txt]
    for k,v in txt:
        d[k]= v
    return d

for k,v in putsubs().items():
    print (k,v)
    s= open('json/'+v,'rb').read().decode('latin1')
    w[k]['subtitles']= prettyvtt(s)

for k in row:
    if not k['id']=='blank':
        if len(k['id'])==11:
            k['title']= '<span style="background-color: green;">{}</span>'.format(k['title'])
        else:
            k['title']= '<span style="background-color: yellow;">{}</span>'.format(k['title'])


out= 'var w= {};'.format(w);

b= open('out.json','w')
b.write(out)
b.close()

#print (len(ret))

