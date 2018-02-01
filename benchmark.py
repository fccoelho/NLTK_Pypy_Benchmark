#!/usr/bin/env python
"""
This module contains some selected code from NLTK testing pages:
    http://nltk.googlecode.com/svn/trunk/doc/howto/portuguese_en.html
    http://nltk.googlecode.com/svn/trunk/doc/howto/featgram.html

this may required the downloads of some nltk data to run.
"""
import sys
import codecs
import report
from time import time
# if 'PyPy' in sys.version:
    # import numpypy #important to make numpy import in NLTK work
import nltk
from nltk import *
from nltk.corpus import machado
from nltk import grammar, parse
from nltk.parse.featurechart import InstantiateVarsChart

sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
raw_text1 = machado.raw('romance/marm05.txt')
raw_text2 = machado.raw('romance/marm04.txt')
raw_text3 = machado.raw('romance/marm03.txt')

ptext1 = nltk.Text(machado.words('romance/marm01.txt'))
ptext2 = nltk.Text(machado.words('romance/marm02.txt'))
ptext3 = nltk.Text(machado.words('romance/marm03.txt'))
ptext4 = nltk.Text(machado.words('romance/marm04.txt'))

cp = parse.load_parser('grammars/book_grammars/feat0.fcfg', trace=1)
stemmer = nltk.stem.RSLPStemmer()

## Checking version of the benchmarking
if 'PyPy' in sys.version:
    version = 'PyPy {}'.format(sys.version)
else:
    version = 'CPython {}'.format(sys.version)

report.setup('PyPy' in version)

def mute():
    sys.stdout = codecs.open('/dev/null','w','utf8') #use codecs to avoid decoding errors
def unmute():
    sys.stdout = sys.__stdout__

def timefun(fun):
    """
    Decorator to time functions
    """
    def timed(*args, **kw):
        mute()
        ts = time()
        result = fun(*args, **kw)
        te = time()
        tt = te-ts
        unmute()
        report.save_time(version,'* _%s_: %s: %2.4f seconds\n'%(version,fun.__name__ , tt))
        print ('%r  %2.4f sec' %(fun.__name__ , tt))
        return result
    return timed

@timefun
def concordance_bench():
    #TODO: find and equivalent text which doesn't print the result
    ptext1.concordance('olhos')
    ptext2.concordance('olhos')
    ptext3.concordance('olhos')
    ptext4.concordance('olhos')

@timefun
def similar_bench():
    s = ptext1.similar('chegar')
    ptext2.similar('chegar')
    ptext3.similar('chegar')
    ptext4.similar('chegar')

@timefun
def collocations_bench():
    ptext1.collocations()
    ptext2.collocations()
    ptext3.collocations()
    ptext4.collocations()

@timefun
def generate_bench():
    ptext1.generate()
    ptext2.generate()
    ptext3.generate()
    ptext4.generate()

@timefun
def freqdist_bench():
    fd1 = FreqDist(ptext1)
    fd2 = FreqDist(ptext2)
    fd3 = FreqDist(ptext3)
    fd4 = FreqDist(ptext4)

@timefun
def sent_tokenizer_bench():
    sentences1 = sent_tokenizer.tokenize(raw_text1)
    sentences2 = sent_tokenizer.tokenize(raw_text2)
    sentences3 = sent_tokenizer.tokenize(raw_text3)

@timefun
def feat_grammar_parse_bench():
    sent = 'Kim likes children'
    tokens = sent.split()
    trees = cp.parse_all(tokens)

@timefun
def confusion_matrix_bench():
    reference = 'This is the reference data.  Testing 123.  aoaeoeoe'
    test =      'Thos iz_the rifirenci data.  Testeng 123.  aoaeoeoe'
    ConfusionMatrix(raw_text1,raw_text1)

@timefun
def stemming_bench():
    [stemmer.stem(w) for w in machado.words('romance/marm05.txt')]

#@timefun
#def feat_grammar_parse_wbind_bench():
#    trees = cp2.nbest_parse('john feeds a dog. The dog barks'.split())

if __name__=="__main__":
    concordance_bench()
    similar_bench()
    collocations_bench()
    #generate_bench()
    freqdist_bench()
    sent_tokenizer_bench()
    feat_grammar_parse_bench()
#    feat_grammar_parse_wbind_bench()
    confusion_matrix_bench()
    stemming_bench()

if 'PyPy' in version:
    print ("building report:")
    report.build()

