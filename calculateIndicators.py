#!/usr/bin/python

from pandas import *
import sys
import os
import re

if len(sys.argv) != 2:
    print 'Usage: calculateIndicators.py NCM.AX.csv'
    #exit(1)

#AA find all files in current directory matching XXX.AX.csv
files = os.walk(os.path.join(os.getcwd(), 'data')).next()[2]
asxfilepattern = re.compile("\D\D\D\.AX\.csv")
asxfiles = [f for f in files if asxfilepattern.match(f) != None]

for f in asxfiles:
    print os.path.join(os.getcwd(), 'data',f)
    try:
        df = pandas.io.parsers.read_csv(os.path.join(os.getcwd(), 'data',f))
        df = df.sort_index(by=['Date'], ascending=[True])
        df['Volume52Mean'] = rolling_mean(df.Volume, 52)
        df.to_csv(os.path.join(os.getcwd(), 'data',f[0:6]) + '.Indicators.csv', headers=True)
        print df
    except:
        print 'error with file: ' + f

