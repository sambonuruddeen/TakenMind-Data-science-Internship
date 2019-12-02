import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

#1. manually create KDE suming guasian distribution
ds = randn(100)
sms.rugplot(ds)
#plt.ylim(0,1)
plt.hist(ds,alpha=0.5)
plt.savefig('img1.png')

x_axes = np.linspace(ds.min() - 1,ds.max() + 1,50)

#bandwidth creation
bandwidth = ((4*ds.std()**5)/(3*len(ds))) ** 0.2
kernels = []

for point in ds:
    kernel = stats.norm(point,bandwidth).pdf(x_axes)
    kernels.append(kernel)

    kernel = kernel / kernel.max()
    kernel = kernel * 0.6

    plt.plot(x_axes,kernel,alpha=0.5,color="red")

#plt.ylim(0,1)
plt.savefig('img2.png')

kde = np.sum(kernels,axis=0)
kde_fig = plt.plot(x_axes,kde,color='green')
sms.rugplot(ds)
plt.suptitle('KDE plot')
plt.savefig('img3.png')


#2. using seaborn - shortcut
kdefig = sms.kdeplot(ds)
fig = kdefig.get_figure()
fig.savefig('img4.png')