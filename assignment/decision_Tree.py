import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Iris.csv')

#print df.columns
all_inputs = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
all_classes = df['Species'].values
#print all_inputs

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
print dtc.score(test_inputs, test_classes)
#print dtc.predict([[1,1,1,1]])
#print dtc.predict([[4.9, 2.5, 4.5, 1.7]])
#print dtc.predict([[6.5, 3.1, 5.5, 1.8]])
#print dtc.predict([[5, 3, 2.5,0.8]])
