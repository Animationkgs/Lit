

import os, json, html

alphabets= {}


def entity16(x):
    return '&#x{};'.format(x)

def entity16ord(x):
    h= hex(x).split('x')[1].zfill(4)
    return '&#x{};'.format(h)

def escape16(x):
    return '&amp;&num;x{};'.format(x)


def entity10(x):
    return '&#{};'.format(x)

def escape10(x):
    return '&amp;&num;{};'.format(x)


def span(x,style):
    return '<span style="{}">{}</span>'.format(style,x)


class Alphabet:

    def __init__(self, i, meaning= None):
        self.i= i
        self.h= hex(i).split('x')[1].zfill(4)
        alphabets[self.h]= self
        self.meaning= meaning
        self.sound= None
        if meaning:
            self.sound= meaning.split(' ')[-1]
        else:
            print (i,meaning,self.show())

    def entity16(self): return entity16(self.h)
    def escape16(self): return escape16(self.h)
    def entity10(self): return entity10(self.i)
    def key(self): return '{}={}'.format( self.entity10(), self.entity16() )

    def html(self):
        style= "font-size: 100px; background-color: linen"
        return span( self.entity16(), style )

    def show(self):
        style= "font-size: small; font-family: serif"
        x= '{}{}'.format( self.html(), self.meaning )
        return span(x,style)

    def unescape(self): return html.unescape( self.entity16() )


alphabets['0028']= '('
alphabets['002c']= ','

class Word:

    def __init__(self, a, meaning):
        a= a.split(' ')
        self.a= [ alphabets[x] for x in a ]
        self.meaning= meaning

    def entity16(self): return ''.join([ x.entity16() for x in self.a ])
    def escape16(self): return ''.join([ x.escape16() for x in self.a ])
    def sound(self): return ', '.join([ x.sound for x in self.a ])

    def show(self):
        style= "font-size: 100px; background-color: linen"
        x= "{} sound=[{}] meaning {}".format( self.entity16(), self.sound(), self.meaning )
        return span(x, style)


class ShowRange:

    def __init__(self,r,a=None, meaning= None):
        if a:
            r= r[:len(a)]
        else:
            a= [None for x in r]
        self.r= r
        self.a= { i: Alphabet(i,v) for i,v in zip(r,a) }
        self.meaning= ' '.join([str(x) for x in [meaning, 'count=', len(a)]])

    def html(self):
        d= { v.key(): v.show() for k,v in self.a.items() }
        d['repr']= self.meaning
        return d

    def mapsound(self, a, n1=0):
        n2= n1 + len(a)
        for i,v in zip(self.r[n1:n2],a):
            self.a[i].sound= v


r2= range(0x1100, 0x1113)
a= 'G GG N D DD R M B BB S SS . J JJ C K T P H'.split(' ')
klc= ShowRange(r2, a, 'korean lead consonant')

r3= range(0x1161, 0x1176)
a= 'A AE YA YAE EO E YEO YE O WA WAE OE YO U WEO WE WI YU EU YI I'.split(' ')
kv= ShowRange(r3, a, 'korean vowel')

r4= range(0x11A8, 0x11C3)
a= 'G GG GS N NJ NH D L LG LM LB LS LT LP LH M B BS S SS NG J C K T P H'.split(' ')
ktc= ShowRange(r4, a, 'korean trail consonant')

a= [(260, 'A ogonek'), (261, 'a ogonek'), (262, 'C acute')]
a+= [(263, 'c acute'), (280, 'E ogonek'), (281, 'e ogonek')]
a+= [(321, 'L stroke'), (322,	'l stroke'), (323, 'N acute')]
a+= [(324, 'n acute'), (211, 'O acute'), (243, 'o acute')]
a+= [(324, 'n acute'), (211, 'O acute'), (243, 'o acute')]
a+= [(346, 'S acute'), (347, 's acute'), (377, 'Z acute')]
a+= [(378, 'z acute'), (379, 'Z dot above'), (380, 'z dot above')]
a+= [(497, 'DZ'), (498, 'Dz'), (499, 'dz')]
r5= a
r= [ x for (x,y) in r5 ] 
a= [ y for (x,y) in r5 ] 
polish= ShowRange(r,a,'polish')

'''ą ć ę ł ń ó ś ź ż &#261; &#263; &#281; &#322; &#324; &#243; &#347; &#378; &#380; &#x0105; &#x0107; &#x0119; &#x0142; &#x0144; &#x00F3; &#x015B; &#x017A; &#x017C;
'''

r6= range(0x0900,0x0980)
dvngr= { 'repr': 'devanagari' }
n1= 0
a= VariousSigns= '''0900 DEVANAGARI SIGN INVERTED CANDRABINDU = vaidika adhomukha candrabindu
0901 DEVANAGARI SIGN CANDRABINDU = anunasika, 0310 combining candrabindu
0902 DEVANAGARI SIGN ANUSVARA = bindu
0903 DEVANAGARI SIGN VISARGA'''.split('\n')
dvngr[0]= ShowRange(r6,a,'Various Signs').html()
n1+= len(a)


a= IndependentVowels= '''0904 DEVANAGARI LETTER SHORT A • used for short e in Awadhi • also used in Devanagari transliterations of some South Indian and Kashmiri languages by a publisher in Lucknow
0905 DEVANAGARI LETTER A
0906 DEVANAGARI LETTER AA
0907 DEVANAGARI LETTER I
0908 DEVANAGARI LETTER II
0909 DEVANAGARI LETTER U
090A DEVANAGARI LETTER UU
090B DEVANAGARI LETTER VOCALIC R
090C DEVANAGARI LETTER VOCALIC L
090D DEVANAGARI LETTER CANDRA E
090E DEVANAGARI LETTER SHORT E • Kashmiri, Bihari languages • also used for transcribing Dravidian short e
090F DEVANAGARI LETTER E
0910 DEVANAGARI LETTER AI
0911 DEVANAGARI LETTER CANDRA O
0912 DEVANAGARI LETTER SHORT O • Kashmiri, Bihari languages • also used for transcribing Dravidian short o
0913 DEVANAGARI LETTER O
0914 DEVANAGARI LETTER AU'''.split('\n')
dvngr[1]= ShowRange(r6[n1:],a,'Independent Vowels').html()
n1+= len(a)


a= Consonants= '''0915 DEVANAGARI LETTER KA
0916 DEVANAGARI LETTER KHA
0917 DEVANAGARI LETTER GA
0918 DEVANAGARI LETTER GHA
0919 DEVANAGARI LETTER NGA
091A DEVANAGARI LETTER CA
091B DEVANAGARI LETTER CHA
091C DEVANAGARI LETTER JA
091D DEVANAGARI LETTER JHA
091E DEVANAGARI LETTER NYA
091F DEVANAGARI LETTER TTA
0920 DEVANAGARI LETTER TTHA
0921 DEVANAGARI LETTER DDA
0922 DEVANAGARI LETTER DDHA
0923 DEVANAGARI LETTER NNA
0924 DEVANAGARI LETTER TA
0925 DEVANAGARI LETTER THA
0926 DEVANAGARI LETTER DA
0927 DEVANAGARI LETTER DHA
0928 DEVANAGARI LETTER NA
0929 DEVANAGARI LETTER NNNA • for transcribing Dravidian alveolar n ≡ 0928 093C
092A DEVANAGARI LETTER PA
092B DEVANAGARI LETTER PHA
092C DEVANAGARI LETTER BA
092D DEVANAGARI LETTER BHA
092E DEVANAGARI LETTER MA
092F DEVANAGARI LETTER YA
0930 DEVANAGARI LETTER RA
0931 DEVANAGARI LETTER RRA • for transcribing Dravidian alveolar r • half form is represented as “Eyelash RA” ≡ 0930 093C
0932 DEVANAGARI LETTER LA
0933 DEVANAGARI LETTER LLA
0934 DEVANAGARI LETTER LLLA • for transcribing Dravidian l ≡ 0933 093C
0935 DEVANAGARI LETTER VA
0936 DEVANAGARI LETTER SHA
0937 DEVANAGARI LETTER SSA
0938 DEVANAGARI LETTER SA
0939 DEVANAGARI LETTER HA'''.split('\n')
dvngr[2]= ShowRange(r6[n1:],a,'Consonants').html()
n1+= len(a)

s= 'These dependent vowel signs are used in Kashmiri and in the Bihari languages (Bhojpuri, Magadhi, and Maithili)'
a= DependentVowelSigns= '''093A DEVANAGARI VOWEL SIGN OE
093B DEVANAGARI VOWEL SIGN OOE'''.split('\n')
dvngr[3]= ShowRange(r6[n1:], a, 'Dependent Vowel Signs<br>' + s).html()
n1+= len(a)


a= VariousSigns= '''093C DEVANAGARI SIGN NUKTA • for extending the alphabet to new letters
093D DEVANAGARI SIGN AVAGRAHA'''.split('\n')
dvngr[4]= ShowRange(r6[n1:], a, 'Various Signs').html()
n1+= len(a)


a= DependentVowelSigns2= '''093E DEVANAGARI VOWEL SIGN AA
Stands to the left of the consonant<br> 093F DEVANAGARI VOWEL SIGN I
0940 DEVANAGARI VOWEL SIGN II
0941 DEVANAGARI VOWEL SIGN U
0942 DEVANAGARI VOWEL SIGN UU
0943 DEVANAGARI VOWEL SIGN VOCALIC R
0944 DEVANAGARI VOWEL SIGN VOCALIC RR
0945 DEVANAGARI VOWEL SIGN CANDRA E = candra
0946 DEVANAGARI VOWEL SIGN SHORT E • Kashmiri, Bihari languages • also used for transcribing Dravidian short e
0947 DEVANAGARI VOWEL SIGN E
0948 DEVANAGARI VOWEL SIGN AI
0949 DEVANAGARI VOWEL SIGN CANDRA O
094A DEVANAGARI VOWEL SIGN SHORT O • Kashmiri, Bihari languages • also used for transcribing Dravidian short o
094B DEVANAGARI VOWEL SIGN O
094C DEVANAGARI VOWEL SIGN AU'''.split('\n')
dvngr[5]= ShowRange(r6[n1:], a, 'Dependent Vowel Signs').html()
n1+= len(a)


a= Virama= '''094D DEVANAGARI SIGN suppresses inherent vowel = halant (the preferred Hindi name) VIRAMA'''.split('\n')
dvngr[6]= ShowRange(r6[n1:], a, 'Virama').html()
n1+= len(a)

a= DependentVowelSigns3= '''094E DEVANAGARI VOWEL SIGN PRISHTHAMATRA E • character has historic use only • combines with E to form AI, with AA to form O, and with O to form AU
094F DEVANAGARI VOWEL SIGN AW • Kashmiri, Bihari languages'''.split('\n')
dvngr[7]= ShowRange(r6[n1:], a, 'Dependent Vowel Signs').html()
n1+= len(a)


a= Sign= '''0950 DEVANAGARI OM → 1F549 om symbol'''.split('\n')
dvngr[8]= ShowRange(r6[n1:], a, 'Sign').html()
n1+= len(a)

a= VedicToneMarks= '''0951 DEVANAGARI STRESS SIGN UDATTA = Vedic tone svarita • mostly used for svarita, with rare use for udatta • used also in Vedic texts written in other scripts → 1CDA vedic tone double svarita
0952 DEVANAGARI STRESS SIGN ANUDATTA = Vedic tone anudatta • used also in Vedic texts written in other scripts → 1CDC vedic tone kathaka anudatta'''.split('\n')
dvngr[9]= ShowRange(r6[n1:], a, 'Vedic Tone Marks').html()
n1+= len(a)


a= AccentMarks= '''0953 DEVANAGARI GRAVE ACCENT → 0300 combining grave accent
0954 DEVANAGARI ACUTE ACCENT → 0301 combining acute accent'''.split('\n')
s= 'These accent marks were originally intended for Latin transliteration of Sanskrit, but 0300 and 0301 should be used instead. These two accents should not be used with the Devanagari script; they have no Indic shaping properties.'
dvngr[10]= ShowRange(r6[n1:], a, 'Accent Marks<br>' + s).html()
n1+= len(a)


a= DependentVowelSign4= '''0955 DEVANAGARI VOWEL SIGN CANDRA LONG E • used in transliteration of Avestan'''.split('\n')
dvngr[11]= ShowRange(r6[n1:], a, 'Dependent Vowel Sign').html()
n1+= len(a)


a= DependentVowelSignsforKashmiri= '''0956 DEVANAGARI VOWEL SIGN UE
0957 DEVANAGARI VOWEL SIGN UUE'''.split('\n')
dvngr[12]= ShowRange(r6[n1:], a, 'Dependent Vowel Signs for Kashmiri').html()
n1+= len(a)


s= '''These eight consonants with nuktas are listed in CompositionExclusions.txt. That means that they do not recompose during normalization. The NFC form is the same as the decomposed sequence.'''
a= AdditionalConsonants= '''0958 DEVANAGARI LETTER QA ≡ 0915 093C
0959 DEVANAGARI LETTER KHHA ≡ 0916 093C
095A DEVANAGARI LETTER GHHA ≡ 0917 093C
095B DEVANAGARI LETTER ZA ≡ 091C 093C
095C DEVANAGARI LETTER DDDHA ≡ 0921 093C
095D DEVANAGARI LETTER RHA ≡ 0922  093C
095E DEVANAGARI LETTER FA ≡ 092B 093C
095F DEVANAGARI LETTER YYA ≡ 092F 093C'''.split('\n')
dvngr[13]= ShowRange(r6[n1:], a, 'Additional Consonants<br>' + s).html()
n1+= len(a)


a= AdditionalVowelsforSanskrit = '''0960 DEVANAGARI LETTER VOCALIC RR
0961 DEVANAGARI LETTER VOCALIC LL
0962 DEVANAGARI VOWEL SIGN VOCALIC L
0963 DEVANAGARI VOWEL SIGN VOCALIC LL'''.split('\n')
dvngr[14]= ShowRange(r6[n1:], a, 'Additional Vowels for Sanskrit').html()
n1+= len(a)


s= '''These punctuation marks are for common use for the scripts of India despite being named "DEVANAGARI". They also occur as abbreviation signs in some South Indian scripts.'''
a= GenericPunctuationforscriptsofIndia = '''0964 । DEVANAGARI DANDA = purna viram • phrase separator
0965 ॥ DEVANAGARI DOUBLE DANDA = deergh viram'''.split('\n')
dvngr[15]= ShowRange(r6[n1:], a, 'Generic Punctuation for scripts of India<br>' + s).html()
n1+= len(a)


a= Digits= '''0966 DEVANAGARI DIGIT ZERO • also used to represent an anusvara following digits indicating secondary svara-s in Samavedic texts
0967 १ DEVANAGARI DIGIT ONE
0968 २ DEVANAGARI DIGIT TWO
0969 ३ DEVANAGARI DIGIT THREE
096A ४ DEVANAGARI DIGIT FOUR
096B ५ DEVANAGARI DIGIT FIVE
096C ६ DEVANAGARI DIGIT SIX
096D ७ DEVANAGARI DIGIT SEVEN
096E ८ DEVANAGARI DIGIT EIGHT
096F ९ DEVANAGARI DIGIT NINE'''.split('\n')
dvngr[16]= ShowRange(r6[n1:], a, 'Digits').html()
n1+= len(a)


a= AdditionalSigns= '''0970 DEVANAGARI ABBREVIATION SIGN • intended for Devanagari-specific abbreviations
0971 DEVANAGARI SIGN HIGH SPACING DOT'''.split('\n')
dvngr[17]= ShowRange(r6[n1:], a, 'Additional Signs').html()
n1+= len(a)


a= IndependentVowelforMarathi = '''0972 DEVANAGARI LETTER CANDRA A'''.split('\n')
dvngr[18]= ShowRange(r6[n1:], a, ' Independent Vowel for Marathi').html()
n1+= len(a)


s= 'These independent vowels are used in Kashmiri and in the Bihari languages.'
a= IndependentVowels= '''0973 DEVANAGARI LETTER OE
0974 DEVANAGARI LETTER OOE
0975 DEVANAGARI LETTER AW'''.split('\n')
dvngr[19]= ShowRange(r6[n1:], a, 'Independent Vowels<br>' + s).html()
n1+= len(a)


a= IndependentVowelsforKashmiri= '''0976 DEVANAGARI LETTER UE
0977 DEVANAGARI LETTER UUE'''.split('\n')
dvngr[20]= ShowRange(r6[n1:], a, 'Independent Vowels for Kashmiri').html()
n1+= len(a)

a= AdditionalConsonants= '''0978 DEVANAGARI LETTER MARWARI DDA
0979 DEVANAGARI LETTER ZHA • used in transliteration of Avestan → 0AF9  gujarati letter zha
097A DEVANAGARI LETTER HEAVY YA • used for an affricated glide JJYA'''.split('\n')
dvngr[21]= ShowRange(r6[n1:], a, 'Additional Consonants').html()
n1+= len(a)


a= SindhiImplosives= '''097B DEVANAGARI LETTER GGA
097C DEVANAGARI LETTER JJA'''.split('\n')
dvngr[22]= ShowRange(r6[n1:], a, 'Sindhi Implosives').html()
n1+= len(a)


a= GlottalStop= '''097D DEVANAGARI LETTER GLOTTAL STOP • used for writing Limbu in Devanagari • a glyph variant has the connecting top bar'''.split('\n')
dvngr[23]= ShowRange(r6[n1:], a, 'Glottal Stop').html()
n1+= len(a)


a= SindhiImplosives2= '''097E DEVANAGARI LETTER DDDA
097F DEVANAGARI LETTER BBA'''.split('\n')
dvngr[24]= ShowRange(r6[n1:], a, 'Sindhi Implosives').html()
n1+= len(a)
dvngr['repr']= '{} count {}'.format('devanagari', str(n1))

w={}
def push(a, meaning):
    a= Word(a, meaning)
    w[a.escape16()]= a.show()

push( '091c 0948 0938 093e', 'as')
push( '092e 0948 0902', 'I')
push( '0907 0930 092b 093e 0928', 'Irfan')
push( '0916 093e 0928', 'Khan')

'''], ['0x92c', '0x940', '0x92e', '0x93e', '0x930', '0x93f', '0x92f', '0x94b', '0x902'], ['0x915', '0x947'], ['0x915', '0x93e', '0x930', '0x923'], ['0x916', '0x94b'], ['0x926', '0x93f', '0x92f', '0x93e', '0x964']]
'''
push( "0939 093e 0932", "-" )
push( "0939 0940", "-" )
push( "092c 0949 0932 0940 0935 0941 0921", "-" )
push( "0928 0947", "-" )
push( "0907 0930 092b 093e 0928", "-" )
push( "0916 093e 0928", "-" )
push( "0914 0930", "-" )
push( "090b 0937 093f", "-" )
push( "0915 092a 0942 0930", "-" )
push( "091c 0948 0938 0947", "-" )
push( "0926 093f 0917 094d 0917 091c", "-" )
push( '0905 092d 093f 0928 0947 0924 093e 0913 0902', 'abhinetaon = the actors' )
push( "0915 094b", "-" )
push( '0932 093e 0907 0932 093e 091c', 'lailaaj = Incurable' )
push( "092c 0940 092e 093e 0930 093f 092f 094b 0902", "-" )
push( "0915 0947", "-" )
push( "0915 093e 0930 0923", "-" )
push( "0916 094b", "-" )
push( "0926 093f 092f 093e 0964", "-" )
push( "091c 0939 093e 0902", "-" )
push( "0907 0930 092b 093e 0928", "-" )
push( "0928 094d 092f 0942 0930 094b 090f 0902 0921 094b 0915 094d 0930 093e 0907 0928", "-" )
push( "091f 094d 092f 0942 092e 0930", "-" )
push( "091c 094b", "-" )
push( "0936 0930 0940 0930", "-" )
push( "092e 0947 0902", "-" )
push( "0915 0939 0940 0902", "-" )
push( "092d 0940", "-" )
push( "0939 094b", "-" )
push( "0938 0915 0924 093e", "-" )
push( "0939 0948", "-" )
push( "0938 0947", "-" )
push( "092a 0940 0921 093f 093c 0924", "-" )
push( "0925 0947", "-" )
push( "0935 0939 0940 0902", "-" )
push( "090b 0937 093f", "-" )
push( "0915 092a 0942 0930", "-" )
push( "0932 094d 092f 0942 0915 0947 092e 093f 092f 093e", "-" )
push( "0915 0948 0902 0938 0930", "-" )
push( "0938 0947", "-" )
push( "0906 0916 093f 0930 0940", "-" )
push( "0935 0915 093c 094d 0924", "-" )
push( "0924 0915", "-" )
push( "091c 0942 091d 0924 0947", "-" )
push( "0930 0939 0947 0964", "-" )
push( "0905 092c", "-" )
push( "0939 093e 0932", "-" )
push( "0939 0940", "-" )
push( "090f 0915", "-" )
push( "0914 0930", "-" )
push( "092c 0949 0932 0940 0935 0941 0921", "-" )
push( "0938 0947 0932 093f 092c 094d 0930 093f 091f 0940", "-" )
push( "0928 0947", "-" )
push( "0905 092a 0928 0940", "-" )
push( "0916 093e 0938", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0938 0947", "-" )
push( "092a 0930 094d 0926 093e", "-" )
push( "0909 0920 093e 092f 093e", "-" )
push( "0939 0948", "-" )
push( "091c 093f 0938 0947", "-" )
push( "0909 0928 094d 0939 094b 0902 0928 0947", "-" )
push( "0905 092a 0928 0940", "-" )
push( "0905 0926 092e 094d 092f", "-" )
push( "0907 091a 094d 091b 093e", "-" )
push( "0936 0915 094d 0924 093f", "-" )
push( "0938 0947", "-" )
push( "092c 0939 0941 0924", "-" )
push( "092a 0939 0932 0947", "-" )
push( "0939 0940", "-" )
push( "0939 0930 093e", "-" )
push( "0926 093f 092f 093e", "-" )
push( "0925 093e 0964", "-" )
push( "092f 0939", "-" )
push( "0938 0947 0932 093f 092c 094d 0930 093f 091f 0940", "-" )
push( "0914 0930", "-" )
push( "0915 094b 0908", "-" )
push( "0928 0939 0940 0902", "-" )
push( "092a 0942 0930 094d 0935", "-" )
push( "092c 094d 0930 0939 094d 092e 093e 0902 0921", "-" )
push( "0938 0941 0902 0926 0930 0940", "-" )
push( "0938 0941 0937 094d 092e 093f 0924 093e", "-" )
push( "0938 0947 0928", "-" )
push( "0939 0948 0902 0964", "-" )
push( "0938 0941 0937 094d 092e 093f 0924 093e", "-" )
push( "0938 0947 0928", "-" )
push( "0928 0947", "-" )
push( "0939 093e 0932", "-" )
push( "0939 0940", "-" )
push( "092e 0947 0902", "-" )
push( "0916 0941 0932 093e 0938 093e", "-" )
push( "0915 093f 092f 093e", "-" )
push( "0915 093f", "-" )
push( "0935 0939", "-" )
push( "0905 0924 0940 0924", "-" )
push( "092e 0947 0902", "-" )
push( "090f 0915", "-" )
push( "092a 0941 0930 093e 0928 0940", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0938 0947", "-" )
push( "091c 0942 091d", "-" )
push( "0930 0939 0940", "-" )
push( "0925 0940 0902", "-" )
push( "0914 0930", "-" )
push( "092c 091a", "-" )
push( "0917 0908 0902 0964", "-" )
push( "090f 0921 093f 0938 0902 0938", "-" )
push( "0921 093f 091c 0940 091c", "-" )
push( "0928 093e 092e", "-" )
push( "0915 0940", "-" )
push( "0907 0938", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0938 0947", "-" )
push( "0932 0921 0929 0947", "-" )
push( "0915 0947", "-" )
push( "092c 093e 0930 0947", "-" )
push( "092e 0947 0902", "-" )
push( "092d 093e 0935 0928 093e 0924 094d 092e 0915", "-" )
push( "0915 0939 093e 0928 0940", "-" )
push( "0938 093e 091d 093e", "-" )
push( "0915 0930 0924 0947", "-" )
push( "0939 0941 090f", "-" )
push( "0909 0928 094d 0939 094b 0902 0928 0947", "-" )
push( "0938 094b 0936 0932", "-" )
push( "092e 0940 0921 093f 092f 093e", "-" )
push( "092a 0930", "-" )
push( "090f 0915", "-" )
push( "092a 094b 0938 094d 091f", "-" )
push( "092d 0940", "-" )
push( "0932 093f 0916 0940", "-" )
push( "0939 0948", "-" )
push( "091c 093f 0938 092e 0947 0902", "-" )
push( "0909 0928 094d 0939 094b 0902 0928 0947", "-" )
push( "0915 0939 093e", "-" )
push( "0915 093f", "-" )
push( "0909 0928 094d 0939 094b 0902 0928 0947", "-" )
push( "0915 0948 0938 0947", "-" )
push( "091a 093e 0930", "-" )
push( "0938 093e 0932", "-" )
push( "0924 0915", "-" )
push( "0907 0938", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0915 0947", "-" )
push( "0916 093f 0932 093e 092b", "-" )
push( "0932 0921 093c 093e 0908", "-" )
push( "0932 0921 093c 0940 0964", "-" )


push( "0911 091f 094b 0907 092e 094d 092f 0942 0928", "-" )
push( "0938 0947", "-" )
push( "091c 0941 0921 093c 093e", "-" )
push( "0939 0948", "-" )
push( "0930 094b 0917", "-" )
push( "092a 0942 0930 094d 0935", "-" )
push( "092e 093f 0938", "-" )
push( "092f 0942 0928 093f 0935 0930 094d 0938", "-" )
push( "0928 0947", "-" )
push( "0916 0941 0932 093e 0938 093e", "-" )
push( "0915 093f 092f 093e", "-" )
push( "0915 093f", "-" )
push( "091c 092c", "-" )
push( "0909 0928 094d 0939 0947 0902", "-" )
push( "0938 093f 0924 0902 092c 0930", "-" )
push( "092e 0947 0902", "-" )
push( "090f 0921 093f 0938 0928", "-" )
push( "0928 093e 092e", "-" )
push( "0915 0940", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0915 093e", "-" )
push( "092a 0924 093e", "-" )
push( "091a 0932 093e", "-" )
push( "091c 094b", "-" )
push( "0911 091f 094b 0907 092e 094d 092f 0942 0928", "-" )
push( "0938 0947", "-" )
push( "091c 0941 0921 093c 0940", "-" )
push( "0939 0941 0908", "-" )
push( "0939 0948", "-" )
push( "0924 094b", "-" )
push( "092e 0941 091d 0947", "-" )
push( "0910 0938 093e", "-" )
push( "0932 0917", "-" )
push( "0930 0939 093e", "-" )
push( "0925 093e", "-" )
push( "092e 093e 0928 094b", "-" )
push( "0905 092c", "-" )
push( "0907 0938", "-" )
push( "0932 0921 093c 093e 0908", "-" )
push( "092e 0947 0902", "-" )
push( "092e 0947 0930 0947", "-" )
push( "0932 093f 090f", "-" )
push( "0915 0941 091b", "-" )
push( "0928 0939 0940 0902", "-" )
push( "092c 091a 093e", "-" )
push( "0939 0948 0964 0938 094b 0936 0932", "-" )
push( "092e 0940 0921 093f 092f 093e", "-" )
push( "092a 0930", "-" )
push( "0909 0938", "-" )
push( "0915 0920 093f 0928", "-" )
push( "0926 094c 0930", "-" )
push( "0915 0940", "-" )
push( "092f 093e 0926", "-" )
push( "0915 094b", "-" )
push( "0924 093e 091c 093e", "-" )
push( "0915 0930 0924 0947", "-" )
push( "0939 0941 090f", "-" )
push( "0909 0928 094d 0939 094b 0902 0928 0947", "-" )
push( "0932 093f 0916 093e", "-" )
push( "0915 093f", "-" )
push( "092e 0947 0930 0940", "-" )
push( "0906 0902 0916 094b 0902", "-" )
push( "0915 0947", "-" )
push( "0928 0940 091a 0947", "-" )
push( "0915 0947", "-" )
push( "0915 093e 0932 0947", "-" )
push( "0918 0947 0930 094b 0902", "-" )
push( "0938 0947", "-" )
push( "092e 0947 0930 0947", "-" )
push( "091a 093e 0930", "-" )
push( "0938 093e 0932", "-" )
push( "0915 0947", "-" )
push( "0932 0902 092c 0947", "-" )
push( "0938 0902 0918 0930 094d 0937", "-" )
push( "0915 093e", "-" )
push( "092a 0924 093e", "-" )
push( "0928 0939 0940 0902", "-" )
push( "091a 0932", "-" )
push( "0938 0915 0924 093e 0964", "-" )
push( "092c 0949 0932 0940 0935 0941 0921", "-" )
push( "0915 0940", "-" )
push( "0938 092c 0938 0947", "-" )
push( "092b 093f 091f 094d 091f 0947 0938 094d 091f", "-" )
push( "0914 0930", "-" )
push( "092b 093f 091f 0928 0947 0938", "-" )
push( "092b 094d 0930 0940 0915", "-" )
push( "090f 0915 094d 091f 094d 0930 0948 0938", "-" )
push( "092e 0947 0902", "-" )
push( "0936 0941 092e 093e 0930", "-" )
push( "096a 096a", "-" )
push( "0935 0930 094d 0937 0940 092f", "-" )
push( "0938 0941 0937 094d 092e 093f 0924 093e", "-" )
push( "0928 0947", "-" )
push( "0906 0917 0947", "-" )
push( "0932 093f 0916 093e", "-" )
push( "0915 093f", "-" )
push( "0907 0932 093e 091c", "-" )
push( "0915 0947", "-" )
push( "0926 094c 0930 093e 0928", "-" )
push( "0938 094d 091f 0947 0930 0949 092f 0921", "-" )
push( "0915 0947", "-" )
push( "0905 0938 0902 0916 094d 092f", "-" )
push( "0926 0941 0937 094d 092a 094d 0930 092d 093e 0935 094b 0902", "-" )
push( "0928 0947", "-" )
push( "092e 0947 0930 0947", "-" )
push( "0936 0930 0940 0930", "-" )
push( "092a 0930", "-" )
push( "092c 0939 0941 0924", "-" )
push( "092c 0941 0930 093e", "-" )
push( "0905 0938 0930", "-" )
push( "0921 093e 0932 093e 0964", "-" )
push( "092e 0948 0902", "-" )
push( "0916 0941 0926", "-" )
push( "0915 094b", "-" )
push( "0930 094b 091c", "-" )
push( "0938 092e 091d 093e 0924 0940", "-" )
push( "0925 0940", "-" )
push( "0932 0947 0915 093f 0928", "-" )
push( "0939 0930", "-" )
push( "0930 094b 091c", "-" )
push( "092f 0939 0940", "-" )
push( "0932 0917 0924 093e", "-" )
push( "0925 093e", "-" )
push( "0915 093f", "-" )
push( "092e 0948 0902", "-" )
push( "092f 0939", "-" )
push( "0932 0921 093c 093e 0908", "-" )
push( "0939 093e 0930", "-" )
push( "091c 093e 090a 0902 0917 0940 0964", "-" )
push( "0915 094d 092f 093e", "-" )
push( "0939 0948", "-" )
push( "090f 0921 093f 0938 0928", "-" )
push( "0930 094b 0917", "-" )
push( "0915 093e", "-" )
push( "0915 093e 0930 0923 0936 0930 0940 0930", "-" )
push( "0915 0940", "-" )
push( "090f 0921 094d 0930 093f 0928 0932", "-" )
push( "0917 094d 0930 0902 0925 093f 092f 094b 0902", "-" )
push( "092e 0947 0902", "-" )
push( "0939 094b 0928 0947", "-" )
push( "0935 093e 0932 0947", "-" )
push( "0907 0938", "-" )
push( "0930 094b 0917", "-" )
push( "092e 0947 0902", "-" )
push( "0936 0930 0940 0930", "-" )
push( "092a 0930 094d 092f 093e 092a 094d 0924", "-" )
push( "092e 093e 0924 094d 0930 093e", "-" )
push( "092e 0947 0902", "-" )
push( "092f 093e", "-" )
push( "092c 0939 0941 0924", "-" )
push( "0915 092e", "-" )
push( "092e 093e 0924 094d 0930 093e", "-" )
push( "092e 0947 0902", "-" )
push( "0915 094b 0930 094d 091f 093f 0938 094b 0932", "-" )
push( "0914 0930", "-" )
push( "090f 0932 094d 0921 094b 0938 094d 091f 0947 0930 094b 0928", "-" )
push( "0928 093e 092e", "-" )
push( "0915 0947", "-" )
push( "0939 093e 0930 094d 092e 094b 0928", "-" )
push( "0915 093e", "-" )
push( "0909 0924 094d 092a 093e 0926 0928", "-" )
push( "0915 0930 0924 093e", "-" )
push( "0939 0948 094d 0930 0964", "-" )
push( "0907 0938 0915 0947", "-" )
push( "0905 092d 093e 0935", "-" )
push( "092e 0947 0902", "-" )
push( "0936 0930 0940 0930", "-" )
push( "0915 0940", "-" )
push( "092a 094d 0930 0924 093f 0930 0915 094d 0937 093e", "-" )
push( "092a 094d 0930 0923 093e 0932 0940", "-" )
push( "090f 0921 094d 0930 093f 0928 0932", "-" )
push( "0917 094d 0930 0902 0925 093f 092f 094b 0902", "-" )
push( "092a 0930", "-" )
push( "0939 092e 0932 093e", "-" )
push( "0915 0930 0924 0940", "-" )
push( "0939 0948 0964", "-" )
push( "090f 0921 093f 0938 0928", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0915 0947", "-" )
push( "0915 093e 0930 0923", "-" )
push( "090f 0921 094d 0930 093f 0928 0932", "-" )
push( "0917 094d 0930 0902 0925 093f 092f 093e 0902", "-" )
push( "0935 093f 092b 0932 0939 094b", "-" )
push( "0938 0915 0924 0940", "-" )
push( "0939 0948", "-" )
push( "091c 093f 0938 0938 0947", "-" )
push( "091c 093e 0928", "-" )
push( "0915 094b", "-" )
push( "092d 0940", "-" )
push( "0916 0924 0930 093e", "-" )
push( "0939 094b", "-" )
push( "0938 0915 0924 093e", "-" )
push( "0939 0948 0964", "-" )
push( "0907 0938", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0938 0947", "-" )
push( "092a 094d 0930 0916 094d 092f 093e 0924", "-" )
push( "0932 0947 0916 0915", "-" )
push( "091c 0947 0928", "-" )
push( "0911 0938 094d 091f 0947 0928", "-" )
push( "0915 093e", "-" )
push( "092e 0947 0902", "-" )
push( "0938 093e 0932", "-" )
push( "0915 0940", "-" )
push( "0909 092e 094d 0930", "-" )
push( "092e 0947 0902", "-" )
push( "0928 093f 0927 0928", "-" )
push( "0939 094b", "-" )
push( "0917 092f 093e", "-" )
push( "0925 093e 0964", "-" )
push( "0910 0938 0947", "-" )
push( "0939 0940", "-" )
push( "092a 0942 0930 094d 0935", "-" )
push( "0926 093f 0935 0902 0917 0924", "-" )
push( "0905 092e 0930 0940 0915 0940", "-" )
push( "0930 093e 0937 094d 091f 094d 0930 092a 0924 093f", "-" )
push( "091c 0949 0928", "-" )
push( "090f 092b", "-" )
push( "0915 0948 0928 0947 0921 0940", "-" )
push( "0915 094b", "-" )
push( "092e 0947 0902", "-" )
push( "0938 093e 0932", "-" )
push( "0915 0940", "-" )
push( "0909 092e 094d 0930", "-" )
push( "092e 0947 0902", "-" )
push( "090f 0921 093f 0938 0928", "-" )
push( "0915 0940", "-" )
push( "092c 0940 092e 093e 0930 0940", "-" )
push( "0915 093e", "-" )
push( "092a 0924 093e", "-" )
push( "091a 0932 093e", "-" )
push( "0925 093e 0964", "-" )
push( "0917 094c 0930 0924 0932 092c", "-" )
push( "0939 0948", "-" )
push( "0915 093f", "-" )
push( "0938 093e 0932", "-" )
push( "092a 0939 0932 0947", "-" )
push( "092a 0942 0930 0940", "-" )
push( "0926 0941 0928 093f 092f 093e", "-" )
push( "0915 094b", "-" )
push( "091a 094c 0902 0915 093e 0924 0947", "-" )
push( "0939 0941 090f", "-" )
push( "0938 0941 0937 094d 092e 093f 0924 093e", "-" )
push( "0928 0947", "-" )
push( "092e 093f 0938", "-" )
push( "092f 0942 0928 093f 0935 0930 094d 0938", "-" )
push( "0915 093e", "-" )
push( "0916 093f 0924 093e 092c", "-" )
push( "0905 092a 0928 0947", "-" )
push( "0928 093e 092e", "-" )
push( "0915 093f 092f 093e", "-" )
push( "0914 0930", "-" )
push( "092d 093e 0930 0924", "-" )
push( "0915 094b", "-" )
push( "0926 0941 0928 093f 092f 093e", "-" )
push( "0915 0947", "-" )
push( "0928 0915 094d 0936 0947", "-" )
push( "092a 0930", "-" )
push( "0938 0941 0902 0926 0930 093f 092f 094b 0902", "-" )
push( "0915 0947", "-" )
push( "0926 0947 0936", "-" )
push( "0915 0947", "-" )
push( "0930 0942 092a", "-" )
push( "092e 0947 0902", "-" )
push( "0930 0947 0916 093e 0902 0915 093f 0924", "-" )
push( "0915 0930", "-" )
push( "0926 093f 092f 093e 0964", "-" )
push( "092f 0939", "-" )
push( "092a 0939 0932 0940", "-" )
push( "092c 093e 0930", "-" )
push( "0925 093e", "-" )
push( "091c 092c", "-" )
push( "0915 093f 0938 0940", "kisee Any" )
push( "092d 093e 0930 0924 0940 092f", "bharateeya Indian" )
push( "0915 094b", "-" )
push( "0907 0938", "-" )
push( "0916 093f 0924 093e 092c", "-" )
push( "0938 0947", "-" )
push( "0928 0935 093e 091c 093e", "navaaja Awarded" )
push( "0917 092f 093e", "-" )
push( "0925 093e 0964", "-" )


s= '%e0%a4%87%e0%a4%b0%e0%a4%ab%e0%a4%be%e0%a4%a8%e0%a4%96%e0%a4%be%e0%a4%a8%e0%a4%8b%e0%a4%b7%e0%a4%bf%e0%a4%95%e0%a4%aa%e0%a5%82%e0%a4%b0%e0%a4%95%e0%a5%87%e0%a4%ac%e0%a4%be%e0%a4%a6%e0%a4%85'

print (s)

def num(s):
    return sum([int(x,16)*16**i for i,x in enumerate(reversed(s))])
c= [s[3*n+1:3*n+3] for n in range(63)]
print (c)
n= [num(x) for x in c]
print (n)
n= [n[i:i+3] for i in range(0,len(n),3)]
print (n)
n= [bytes(x).decode() for x in n]
print (n)
n= [entity16ord(ord(x)) for x in n]
print (n)

s= open('b1', 'rb').read().decode().encode('latin1')
print (s)
s= s.split(b' ')
c= [bytes.decode(x) for x in s]

def hexz(x):
    return hex(x).split('x')[-1].zfill(4)
c= [ ' '.join([hexz(ord(y)) for y in x]) for x in c ]
c= [ 'push( "{}", "-" )'.format(x) for x in c ]
out= open('out', 'w')
for x in c: out.write(x+'\n')
out.close()
#n= [num(x) for x in c]
#n= [n[i:i+3] for i in range(0,len(n),3)]
#n= [ [bytes(x).decode() for x in cx] for cx in c]
#n= [entity16ord(ord(x)) for x in n]
#print (n)

dvngr['word'] = w


#print (hindi.unescape())
#print (kv.unescape())
#print (klc.unescape())
#print (ktc.unescape())

e= {}
e['kv']= kv.html()
e['klc']= klc.html()
e['ktc']= ktc.html()
e['polish']= polish.html()
e['devanagari']= dvngr


r7= range(0x0c80,0x0980)
kannada= { 'repr': 'Kannada' }
n1= 0


'''
Miscellaneous mathematical symbols
2200 ∀ FOR ALL
= universal quantifier
2201 ∁ COMPLEMENT
→ 0297 ʗ  latin letter stretched c
2202 ∂ PARTIAL DIFFERENTIAL
2203 ∃ THERE EXISTS
= existential quantifier
2204 ∄ THERE DOES NOT EXIST
≡ 2203 ∃  0338 $̸
2205 ∅ EMPTY SET
= null set
• used in linguistics to indicate a null morpheme
or phonological “zero”
→ 00D8 Ø  latin capital letter o with stroke
→ 2300 ⌀  diameter sign
⁓ 2205 FE00 ∅  zero with long diagonal stroke
overlay form
2206 ∆ INCREMENT
= Laplace operator
= forward difference
= symmetric difference (in set theory)
• other symbols may also be used for symmetric
difference
→ 0394 Δ  greek capital letter delta
→ 25B3 △  white up-pointing triangle
2207 ∇ NABLA
= backward difference
= gradient, del
• used for Laplacian operator (written with
superscript 2)
→ 25BD ▽  white down-pointing triangle
'''

s= json.dumps(e)
s= ['var duo= ', s, ';']
s= ''.join(s)
b= 'json.js'
b= open(b,'w')
b.write(s)
b.close()


