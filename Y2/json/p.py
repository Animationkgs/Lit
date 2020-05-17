


import os, re, json
ret= []
for r,d,f in os.walk('.'):
    for q in f:
        if '.json' in q:
            ret.append(q)

ret= sorted(ret)
count= 0
b= open('json.js', 'w')
d= []
ar= []

def iframe(vid):
    return '''<iframe width="440" height="248" src="https://www.youtube.com/embed/%s?rel=0&amp;mute=1&cc_load_policy=1" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> `;
   };''' % (vid,)

class Slide:
    def __init__(self, vid): self.vid= vid
    def sett(self, t): self.t= t; return self
    def setvc(self, vc): self.vc= vc; return self
    def setdc(self, dc): self.dc= dc; return self
    def setlc(self, lc): self.lc= lc; return self
    def setar(self, ar):
        if ar: self.ar= ar
        else: self.ar= 0
        return self
    def __repr__(self):
        ret= 't vc lc dc ar'
        ret= ret.split(' ')
        ret= [self.__dict__[x] for x in ret]
        ret= [str(x) for x in ret]
        return ', '.join(ret)
    def frame(self): return iframe(self.vid)

for x in ret:
    count+= 1
    a= open(x,'rb').read().decode('utf8')
    s= json.loads(a)
    k= s['uploader_id']
    vid= s['id'].replace('-','_')
    v= Slide(s['id'])
    v= v.sett(s['title']).setvc(s['view_count']).setlc(s['like_count']).setdc(s['dislike_count']).setar(s['average_rating'])
    ar.append(v)
    d.append( (k, {vid:a, 'repr': repr(v)}) )

e= { k : [] for k,a in d} 
for k,a in d:
    e[k].append(a)

def takesecond(x): return (-x.ar,-x.vc)
ar.sort( key=takesecond)
e['top']= [ { 'repr':repr(v), 'id': v.vid, 'frame': v.frame()} for v in ar[:100] ]

w= ['var w= ', json.dumps(e), ';']
w= ''.join(w)
b.write(w)
b.close()

#content= [ 'srt{}{:02d}'.format(lesson,x) for x in range(1,len(ret)+1) ]
#print ('var srt{}= [{}];'.format(lesson, ','.join(content)));
