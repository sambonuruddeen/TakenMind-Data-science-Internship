import pandas as pd
import numpy as np
from pandas import DataFrame

df1 = DataFrame({ 'reference': ['O','U', 'L', 'O','U'],
                   'data': range(5)
})

df2 = DataFrame({ 'profit': [10,20]},
                  index= ['O','U']
)

print pd.merge(df1,df2, left_on='reference', right_index=True)

df3 = DataFrame({'ref1':['A','A','O','O','A'],
                 'ref2':[5,10,15,20,25],
                 'ref3': np.arange(5,)
                 })
df4 = DataFrame({'ref1':['A','A','O','O','O'],
                 'ref2':[15,20,25,30,35],
                 'ref3': [2,3,4,5,6]
                 })

#df4 = DataFrame(np.arange(10).reshape(5,2), index=[['A','A','O','O','O'],[20,10,10,10,20]], columns=['col1','col2'])
#print pd.merge(df3,df4,left_on=['ref1','ref2'],right_index=True)

#join functions

print df3.join(df4, lsuffix='x',rsuffix='y')