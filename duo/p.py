

import os, json, html

class Alphabet:

    def __init__(self, x, sound= None):
        self.x= x
        self.i= int(x,16)
        self.h= hex(self.i).split('x')[1].zfill(4)
        self.sound= sound

    def key(self):
        ret= '&amp;&num;{};=&amp;&num;x{};'
        return ret.format( self.i, self.h )

    def html(self): return '<span style="font-size: 100px; background-color: linen">&#x{};</span>'.format( self.h )

    def show(self):
        return '<span style="font-size: small; font-family: serif">{}{}</span>'.format(self.html(), str(self.sound))

    def unescape(self): return html.unescape( self.html() )

    def json(self): return { self.key(): self.show() }


class ShowRange:

    def __init__(self,r,a=None, meaning= None):
        if a:
            r= r[:len(a)]
        else:
            a= [None for x in r]
        self.r= r
        self.a= { i: Alphabet(hex(i),v) for i,v in zip(r,a) }
        self.meaning= ' '.join([str(x) for x in [meaning, 'count=', len(a)]])

    def unescape(self):
        return [ k.unescape() for k,v in self.a.items() ]

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

r6= range(0x0900, 0x0980)
dvngr= ShowRange(r6)


'''ą ć ę ł ń ó ś ź ż &#261; &#263; &#281; &#322; &#324; &#243; &#347; &#378; &#380; &#x0105; &#x0107; &#x0119; &#x0142; &#x0144; &#x00F3; &#x015B; &#x017A; &#x017C;
'''


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
093F DEVANAGARI VOWEL SIGN I • stands to the left of the consonant
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


a= Virama= '''094D DEVANAGARI SIGN VIRAMA = halant (the preferred Hindi name) • suppresses inherent vowel'''.split('\n')
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



s= json.dumps(e)
s= ['var duo= ', s, ';']
s= ''.join(s)
b= 'json.js'
b= open(b,'w')
b.write(s)
b.close()


