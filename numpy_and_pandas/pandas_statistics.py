import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

array_1 = np.array([[10,np.nan,20],[30,40,np.nan]])
print array_1
df1 = DataFrame(array_1,index=[1,2],columns=list('ABC'))
print df1

#sum()
print df1.sum() #sums along each column
print df1.sum(axis=1) #sums along indexes - each row

print 'min'
print df1.min()

print 'max'
print df1.max()

print 'idxmax'
print df1.idxmax()

print df1.cumsum()

#describe
print df1.describe()

#graphs
df2 = DataFrame(randn(9).reshape(3,3),index=[1,2,3],columns=list('ABC'))
print df2

plt.plot(df2)
plt.legend(df2.columns,loc="lower left")
plt.savefig("samplepic.png")
#plt.show()

ser1 = Series(list('abcccaabd'))
print ser1.unique()

print ser1.value_counts()


