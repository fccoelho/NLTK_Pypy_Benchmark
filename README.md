
Benchmarking NLTK under Pypy
============================

Times for both Cpython 2.72 and PyPy 1.8
----------------------------------------

==Sun Apr  1 10:36:23 2012==

*  concordance_bench
    * _PyPy 1.8_:  0.0924 seconds
    * _CPython 2.7.2_:  0.1992 seconds
*  similar_bench
    * _PyPy 1.8_:  2.6458 seconds
    * _CPython 2.7.2_:  2.6849 seconds
*  collocations_bench
    * _PyPy 1.8_:  5.8604 seconds
    * _CPython 2.7.2_:  6.0382 seconds
*  generate_bench
    * _PyPy 1.8_:  1.5353 seconds
    * _CPython 2.7.2_:  5.2505 seconds
*  freqdist_bench
    * _PyPy 1.8_:  0.1016 seconds
    * _CPython 2.7.2_:  0.7280 seconds
*  sent_tokenizer_bench
    * _PyPy 1.8_:  2.4179 seconds
    * _CPython 2.7.2_:  0.7640 seconds
*  feat_grammar_parse_bench
    * _PyPy 1.8_:  0.0196 seconds
    * _CPython 2.7.2_:  0.0061 seconds
*  confusion_matrix_bench
    * _PyPy 1.8_:  0.8035 seconds
    * _CPython 2.7.2_:  0.2754 seconds
*  stemming_bench
    * _PyPy 1.8_:  1.2130 seconds
    * _CPython 2.7.2_:  4.3075 seconds
