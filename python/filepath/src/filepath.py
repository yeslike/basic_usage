#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
OUTDIR = '../data/'
OUTDIR = os.path.abspath(os.path.join(BASEDIR, OUTDIR))
INFILE = 'code'
INFILE = os.path.join(OUTDIR, INFILE)


if __name__ == '__main__':
    outfile = os.path.join(OUTDIR, 'out') 
    print 'BASEDIR:',BASEDIR
    print 'OUTDIR:',OUTDIR
    print 'INFILE:',INFILE
    print 'OUTFILE:',outfile
