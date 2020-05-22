

import os, json, html

class Alphabet:

    def __init__(self, x):
        self.x= x
        self.i= int(x,16)
        self.h= hex(self.i).split('x')[1].zfill(4)
        self.sound= None

    def key(self):
        ret= '{}x{}'
        return ret.format( self.i, self.h )

    def html(self): return '&#x{};'.format( self.h )

    def show(self):
        v= [ self.html(), str(self.sound) ]
        return ', '.join(v)

    def unescape(self): return html.unescape( self.html() )

    def json(self): return { self.key(): self.show() }

class ShowRange:

    def __init__(self,r):
        self.r= r
        self.a= { i: Alphabet(hex(i)) for i in r }

    def unescape(self):
        return [ k.unescape() for k,v in self.a.items() ]

    def html(self):
        return { v.key(): v.show() for k,v in self.a.items() }


r1= range(2300,2501)
r2= range(0x1100, 0x1113)
r3= range(0x1161, 0x1176)
r4= range(0x11A8, 0x11C3)

hindi= ShowRange(r1)
klc= ShowRange(r2)
kv= ShowRange(r3)
ktc= ShowRange(r4)

a= 'G GG N D DD R M B BB S SS . J JJ C K T P H'
a= a.split(' ')
for i,v in zip(klc.r,a):
    klc.a[i].sound= v

a= 'A AE YA YAE EO E YEO YE O WA WAE OE YO U WEO WE WI YU EU YI I'
a= a.split(' ')
for i,v in zip(kv.r,a):
    kv.a[i].sound= v

a= 'G GG GS N NJ NH D L LG LM LB LS LT LP LH M B BS S SS NG J C K T P H'
a= a.split(' ')
for i,v in zip(ktc.r,a):
    ktc.a[i].sound= v

'''ą ć ę ł ń ó ś ź ż &#261; &#263; &#281; &#322; &#324; &#243; &#347; &#378; &#380; &#x0105; &#x0107; &#x0119; &#x0142; &#x0144; &#x00F3; &#x015B; &#x017A; &#x017C;
'''
        
a= [(260, 'A ogonek'), (261, 'a ogonek'), (262, 'C acute')]
a+= [(263, 'c acute'), (280, 'E ogonek'), (281, 'e ogonek')]
a+= [(321, 'L stroke'), (322,	'l stroke'), (323, 'N acute')]
a+= [(324, 'n acute'), (211, 'O acute'), (243, 'o acute')]
a+= [(324, 'n acute'), (211, 'O acute'), (243, 'o acute')]
a+= [(346, 'S acute'), (347, 's acute'), (377, 'Z acute')]
a+= [(378, 'z acute'), (379, 'Z dot above'), (380, 'z dot above')]
a+= [(497, 'DZ'), (498, 'Dz'), (499, 'dz')]
r5= [ x for (x,y) in a ] 
print (r5)

polish= ShowRange(r5)
a= [ y for (x,y) in a ]
for i,v in zip(polish.r,a):
    polish.a[i].sound= v


#print (hindi.unescape())
#print (kv.unescape())
#print (klc.unescape())
#print (ktc.unescape())

e= {}
e['hindi']= hindi.html()
e['kv']= kv.html()
e['klc']= klc.html()
e['ktc']= ktc.html()
e['polish']= polish.html()

s= json.dumps(e)
s= ['var duo= ', s, ';']
s= ''.join(s)
b= 'json.js'
b= open(b,'w')
b.write(s)
b.close()

