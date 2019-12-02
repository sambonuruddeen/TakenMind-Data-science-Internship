import pandas as pd
from pandas import Series, DataFrame
import numpy as np

clip = pd.read_clipboard()

print clip

#columns
print clip.columns
#print clip['poster']

#multiple columns

print DataFrame(clip, columns=['9', 'Volkswagen', 'Automotive'])
#Nan
clip2 = DataFrame(clip, columns=['9', 'Volkswagen','Automotive', 'loss'])
#head and tail
print 'head'
print clip.head(1)

print 'tail'
print clip.tail(1)

#access rows in dataframe
print clip.ix[0] #row1
print clip.ix[2] #row3

#aasign values
#numpy
array1 = np.array([1,2])
clip2['loss'] = array1

print 'Numpy'
print clip2['loss']
#series
profits = Series([900,1000],index=[1,2])
clip2['loss'] = profits

print 'series'
print clip2

#del
#del clip[profit]

#dictionary
sample = {
    'company': ['A', 'B'],
     'loss': ['100', '500']
}

sample_df = DataFrame(sample)
print sample_df





