import numpy as np

x = np.array([100,400,500,600]) #Each memeber as a
y = np.array([10,15,20,25]) #Each member as b
condition = np.array([True,True,False,False])

#use loops indirectly

z = [a if cond else b for a,cond,b in zip(x, condition,y)]
print z

#np.where

z2 = np.where(condition,x,y)

print "z2"
print z2

z3 = np.where(x>0,0,1)
print "Z3"
print z3

#statndard functions of numpy

#sum
print x.sum()

n = np.array([[1,2],[3,4]])
#column sum
print n.sum(0)

#mean
print 'mean'
print x.mean()
#standard deviation
print 'std deviation'
print x.std()
#variance
print 'variance'
print x.var()

#logical operations -and / or-
condition2 = np.array([True, False, True])
print 'for operator'
print condition2.any() #for operator

print 'and operator'
print condition2.all() #and operator

#sorting in numpy arrays
unsorted_array = np.array([1,2,8,10,7,3])
unsorted_array.sort()
print "sorting"
print unsorted_array

#unique
arr2 = np.array(['solid','solid','liquid','liquid', 'gas','gas'])
print "unique"
print np.unique(arr2)

#in One Dimension
print "1 dimension"
print np.in1d(['solid', 'gas', 'plasma'],arr2)




