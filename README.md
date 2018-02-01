
Benchmarking NLTK under Pypy
============================

See also this post: http://pyinsci.blogspot.com.br/2012/04/benchmarking-nltk-under-pypy.html

Times for both Cpython 2.72 and PyPy 1.8
----------------------------------------

==Thu Feb  1 09:24:58 2018==

* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  concordance_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.0962 seconds
    [GCC 7.2.0]_:  0.1217 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  similar_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  1.1685 seconds
    [GCC 7.2.0]_:  2.0291 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  collocations_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.3302 seconds
    [GCC 7.2.0]_:  0.7898 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  freqdist_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.0452 seconds
    [GCC 7.2.0]_:  0.2823 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  sent_tokenizer_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.5008 seconds
    [GCC 7.2.0]_:  0.4100 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  feat_grammar_parse_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.0102 seconds
    [GCC 7.2.0]_:  0.0040 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  confusion_matrix_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.2307 seconds
    [GCC 7.2.0]_:  0.1814 seconds
* 08
    * _PyPy 3.3.5 (619c0d5af0e5, Oct 08 2016, 21: 33)
    * _CPython 3.6.3 (default, Oct  3 2017, 21: 48) 
*  stemming_bench
    [PyPy 5.5.0-alpha0 with GCC 4.8.2]_:  0.6291 seconds
    [GCC 7.2.0]_:  3.4938 seconds
