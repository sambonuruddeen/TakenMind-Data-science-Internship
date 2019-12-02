import pandas as pd

datafile = pd.ExcelFile('data.xlsx')

#df = datafile.parse('class1')



count = 1
while (count <= 10):

    nm = 'class%d' %count
    df = datafile.parse(nm)

    output = nm + '.csv'
    df.to_csv(output, sep=',')

    count = count + 1