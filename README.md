
Benchmarking NLTK under Pypy
============================

See also this post: http://pyinsci.blogspot.com.br/2012/04/benchmarking-nltk-under-pypy.html

Times for both Cpython 2.72 and PyPy 1.8
----------------------------------------

==Mon Jul 16 10:49:50 2012==

*  concordance_bench
    * _PyPy 1.9_:  0.0826 seconds
    * _CPython 2.7.2_:  0.1758 seconds
*  similar_bench
    * _PyPy 1.9_:  2.2209 seconds
    * _CPython 2.7.2_:  2.4053 seconds
*  collocations_bench
    * _PyPy 1.9_:  4.5280 seconds
    * _CPython 2.7.2_:  4.8633 seconds
*  freqdist_bench
    * _PyPy 1.9_:  0.0794 seconds
    * _CPython 2.7.2_:  0.6239 seconds
*  sent_tokenizer_bench
    * _PyPy 1.9_:  2.2404 seconds
    * _CPython 2.7.2_:  0.6519 seconds
*  feat_grammar_parse_bench
    * _PyPy 1.9_:  0.0128 seconds
    * _CPython 2.7.2_:  0.0054 seconds
*  confusion_matrix_bench
    * _PyPy 1.9_:  0.3311 seconds
    * _CPython 2.7.2_:  0.2303 seconds
*  stemming_bench
    * _PyPy 1.9_:  1.1121 seconds
    * _CPython 2.7.2_:  3.8277 seconds
