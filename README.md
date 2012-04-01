
Benchmarking NLTK under Pypy
============================

Times for both Cpython 2.72 and PyPy 1.8
----------------------------------------

==Sun Apr  1 11:01:22 2012==

*  concordance_bench
    * _PyPy 1.8_:  0.0978 seconds
    * _CPython 2.7.2_:  0.2041 seconds
*  similar_bench
    * _PyPy 1.8_:  2.5432 seconds
    * _CPython 2.7.2_:  2.6919 seconds
*  collocations_bench
    * _PyPy 1.8_:  5.2469 seconds
    * _CPython 2.7.2_:  5.6797 seconds
*  generate_bench
    * _PyPy 1.8_:  1.5103 seconds
    * _CPython 2.7.2_:  5.0527 seconds
*  freqdist_bench
    * _PyPy 1.8_:  0.1000 seconds
    * _CPython 2.7.2_:  0.7145 seconds
*  sent_tokenizer_bench
    * _PyPy 1.8_:  2.3717 seconds
    * _CPython 2.7.2_:  0.7688 seconds
*  feat_grammar_parse_bench
    * _PyPy 1.8_:  0.0181 seconds
    * _CPython 2.7.2_:  0.0063 seconds
*  confusion_matrix_bench
    * _PyPy 1.8_:  0.8159 seconds
    * _CPython 2.7.2_:  0.2862 seconds
*  stemming_bench
    * _PyPy 1.8_:  1.2112 seconds
    * _CPython 2.7.2_:  4.3052 seconds
