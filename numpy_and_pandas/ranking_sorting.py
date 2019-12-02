import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

ser1 = Series([500,1000,1500], index=['a','b','c'])

#sorting by index
print ser1.sort_index()

#sort by values
print ser1.sort_values()
print 's1 Rank'
print ser1.rank()
#ranking series
ser2 = Series(randn(10))
print ser2

print 's2 rank'
print ser2.rank()


