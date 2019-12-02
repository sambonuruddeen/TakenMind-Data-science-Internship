import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

ds1 = randn(1000)
ds2 = randn(100)

plt.hist(ds1)
plt.savefig('image1.png')
#plt.show()

plt.hist(ds2)
plt.savefig('image2.png')
#plt.show()

plt.hist(ds1,density=True,color='green',bins=15,alpha=0.5)
plt.hist(ds2,density=True,bins=15,alpha=0.5)
plt.savefig('image3.png')
#plt.show()

#sms
ds3 = randn(1000)
ds4 = randn(1000)

sms_plot = sms.jointplot(ds3,ds4)
sms_plot.savefig('image4.png')

sms_plot2 = sms.jointplot(ds3,ds4,kind="hex")
sms_plot2.savefig('image5.png')
