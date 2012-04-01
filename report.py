"""
This code generates a quick report in Markdown format
__author__ = fccoelho
__date__ = 4 / 1 / 12

"""
__docformat__ = "restructuredtext en"



header="""
Benchmarking NLTK under Pypy
============================

Times for both Cpython 2.72 and PyPy 1.8
----------------------------------------

"""
import time

def setup(pypy=False):
    with open('README.md','w') as f:
        f.write(header)
    with open('pypy.times','w') as g:
        g.write(time.asctime()+'\n')
    if not pypy:
        with open('cpy.times','w') as h:
            h.write(time.asctime()+'\n')


def save_time(version, line):
    if version == 'PyPy 1.8':
        with open('pypy.times','a') as g:
            g.write(line)
    else:
        with open('cpy.times','a') as h:
            h.write(line)

def add_line(line):
    with open('README.md','a') as f:
        f.write(line)


def build():
    with open('pypy.times','r') as g:
        dat = g.readline().strip() #get datetime line
        plines = g.readlines()
    with open('cpy.times','r') as h:
        h.readline()
        clines = h.readlines()

    add_line('=='+dat+'=='+'\n\n')
    for pl,cl in zip(plines,clines):
        bname = pl.split(':')[1]
        add_line('* '+bname+'\n')
        add_line('    '+pl.split(':')[0]+': '+pl.split(':')[2])
        add_line('    '+cl.split(':')[0]+': '+cl.split(':')[2])