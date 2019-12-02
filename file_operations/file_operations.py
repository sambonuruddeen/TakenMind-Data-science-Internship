import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#import csv as dataframe
dframe = pd.read_csv('025 demo.csv')
print dframe

#with header
dframe = pd.read_csv('025 demo.csv', header=None)
print dframe

#use readtable
dframe2 = pd.read_table('025 demo.csv',sep=',',header=None)
print 'readtable'
print dframe2

#partial rows importing
print pd.read_csv('025 demo.csv', nrows=2, header=None)

#dump data to csv file
dframe2.to_csv('outputCSV.csv',sep=',')

#selecting specific columns
dframe.to_csv('dataoutput.csv', columns=[0,1])


