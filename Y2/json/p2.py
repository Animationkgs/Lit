

import os, re, json
ret, ret2= [], []
for r,d,f in os.walk('.'):
    for q in f:
        if '.json' in q:
            ret.append(q)
        else:
            ret2.append(q)

def key(x):
    ret= '0'
    try: 
        ret= x.split('.')[-3][-11:]
    except:
        print ('error',x)
    return ret

d= { key(x):[] for x in ret }
d['0']= []
for x in ret: d[key(x)].append(x)
for x in ret2: d[key(x)].append(x)

ret= sorted(ret)
print (len(ret))
print (ret[:10])

import os
for k,v in d.items():
    if k=='0': continue
    print (k,v)
    if len(v)==1:
        c= "~/y2 --skip-download --write-auto-sub {}".format(k)
        print (os.system(c))

