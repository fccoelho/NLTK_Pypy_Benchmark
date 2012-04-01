#!/usr/bin/env python
"""
This module contains some selected code from NLTK testing pages:
    http://nltk.googlecode.com/svn/trunk/doc/howto/portuguese_en.html
    http://nltk.googlecode.com/svn/trunk/doc/howto/featgram.html

this may required the downloads of some nltk data to run.
"""
from time import time
import nltk
from nltk import *
from nltk.examples.pt import *
from nltk import grammar, parse
from nltk.parse.featurechart import InstantiateVarsChart



sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
raw_text1 = machado.raw('romance/marm05.txt')
raw_text2 = machado.raw('romance/marm04.txt')
raw_text3 = machado.raw('romance/marm03.txt')

cp = parse.load_parser('grammars/book_grammars/feat0.fcfg', trace=1)


def timefun(fun):
    """
    Decorator to time functions
    """
    def timed(*args, **kw):
        ts = time()
        result = fun(*args, **kw)
        te = time()

        print '%r  %2.2f sec' %(fun.__name__ , te-ts)
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
    s=ptext1.similar('chegar')
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
    trees = cp.nbest_parse(tokens)

#@timefun
#def feat_grammar_parse_wbind_bench():
#    trees = cp2.nbest_parse('john feeds a dog. The dog barks'.split())

if __name__=="__main__":
#    concordance_bench()
#    similar_bench()
#    collocations_bench()
#    generate_bench()
    freqdist_bench()
    sent_tokenizer_bench()
    feat_grammar_parse_bench()
#    feat_grammar_parse_wbind_bench()