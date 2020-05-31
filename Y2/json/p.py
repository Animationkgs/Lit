

import os, re, json
count= 0

def iframe(vid):
    return '''<iframe width="440" height="248" src="https://www.youtube.com/embed/%s?rel=0&amp;mute=1&cc_load_policy=1" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> `;
   };''' % (vid,)


class Slide:

    def __init__(self, s):
        self.s= s
        ar= s['average_rating']
        self.ar= 0.0
        if ar:
            self.ar= float(ar)

    def __repr__(self):
        fields= 'uploader_id title view_count like_count dislike_count average_rating duration'
        ret= [ str(self.s[x]) for x in fields.split(' ') ]
        return ', '.join(ret)

    def frame(self): return iframe(self.vid)

def putd(d,k,k2,v):
    if k in d.keys():
        d[k][k2]= v
    else:
        d[k]= {k2: v}

def put(d,k,v):
    if k in d.keys():
        d[k].append(v)
    else:
        d[k]= [v]

count, count2= 0,0
files= None
for r,d,f in os.walk('.'):
    if not r=='.': continue
    f= list(f)
    files= sorted(f)
    print ('rdf',r,d,len(files))

e= {}
count= 0
for x in files:
    k= x.split('.')[-1]
    if k in ['json','vtt']:
        vid= x.split('.')[-3]
        if len(vid)>11:
            vid= vid[-11:]
            print ('vid',vid)
            putd (e, vid, k, x)
            count+= 1
            #if count==10: break
    else:
        count2+= 1
    if count2==100:
        break
print ('count',count)
print ('files',len(files))
print ('e',len(e))

def get(x):
    return open(x,'rb').read().decode('utf8')

def make(x):
    a= get(x)
    s= json.loads(a)
    s['formats']='No'
    s['url']='No'
    s['thumbnails']='No'
    s['http_headers']='No'
    vid= s['id'].replace('-','_')
    k= s['uploader_id']
    sli= Slide(s)
    return (sli,{ 's':s, 'repr': repr(sli) })

collectupid= {}
collectar= {}
collectdur= {}


for k,v in e.items():
    x= v['json', 'vtt']
    sli,ret= make(x)
    if len(v)>1:
        if 'vtt' in v.keys():
            ret['sub']= v['vtt']
    put(collectupid, ret['s']['uploader_id'], ret)
    put(collectar, int(100*sli.ar), ret)
    put(collectdur, int(int(ret['s']['duration'])/100.0), ret)
slides= {'upid':collectupid, 'ar':collectar, 'dur':collectdur}
w= ['var w= ', json.dumps(slides), ';']
w= ''.join(w)
b= open('json.js', 'w')
b.write(w)
b.close()
'''
        d[k].
            {'i': htmlimg(x)}
            if len(collect)==10:
                e[count]= collect
                collect= {}
                count+= 1
        else:
            print (x)
            try:
                t= open(x,'rb')
            except:
                print ('error')
                continue
            x1= t.read().decode('utf8')
            t.close()
            x1= htmlpretty(x1)
            #print (x1)
            x2= '{}.jpg'.format(x.split('.')[0])
            if os.path.exists(x2):
                x1= htmldiv(x1, lr='right')
                x2= htmlimg(x2)
                x2= htmldiv(x2, lr='left')
                xx= htmldiv0('{}{}'.format(x1,x2))
                #print (xx)
                e[x]= {'pane': xx}
            else:
                e['txt'][x]= { 't': x1 }
    e[count]= collect
    collect= {}
    count+= 1


'''

