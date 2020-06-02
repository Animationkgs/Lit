


t= open('t.html', 'rb').read()
t= t.decode('latin1')

from bs4 import BeautifulSoup as bs
b= bs(t)

field= 'num title directed written aired desc'.split(' ')
prev= None

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

w['1.01']['id']= 'T8jskuQEq6A'
w['1.04']['id']= 'A7bRJsnXutE'
w['3.02']['id']= 'ru6yjKHHVJw'
w['3.03']['id']= 'e4TgbgDrIT4'
w['3.24']['id']= '06TZN_haFxk'
w['title']= 'My Secret Identity 1988-1991'

for k in row:
    if not k['id']=='blank':
        k['title']= '<span style="background-color: green;">{}</span>'.format(k['title'])

out= 'var w= {};'.format(w);

b= open('out.json','w')
b.write(out)
b.close()

#print (len(ret))

