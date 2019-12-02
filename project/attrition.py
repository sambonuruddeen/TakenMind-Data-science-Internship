import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import Series, DataFrame

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#import
employee_data = pd.ExcelFile('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx')

employee_existing = employee_data.parse('Existing employees')
employee_left = employee_data.parse('Employees who have left')

#add attrition column to each sheet
employee_existing = employee_existing.assign(attrition='no')
employee_left = employee_left.assign(attrition='yes')

#join existing and left employees
employee_all = pd.concat([employee_existing, employee_left])

#Check
#print employee_all.head()
#print employee_all.tail()

#print employee_all.isnull()
#print employee_all.dtypes

#Data Transformation

#copy all_employee df
employee_data = employee_all.copy()

#remove empID
employee_data = employee_data.drop('Emp ID', axis=1)
print employee_data.shape
#copy numerical data
employee_data_num = employee_data[['satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years']].copy()

#data visualisation - heatmap

sns.heatmap(employee_data_num.corr())
plt.show()

#copy categorical data
employee_data_cat = employee_data[['dept','salary','attrition']].copy()
#print employee_data_cat.head()


attr = {'yes':1, 'no':0}

employee_data_cat.attrition = [attr[item] for item in employee_data_cat.attrition]
#print employee_data_cat.tail()

#plot pie chart to show % of employees attrition
s = employee_data['attrition'].value_counts(normalize=True) * 100
plt.pie(s,labels=s.index,autopct='%1.2f%%')
plt.title('Attrition')
#plt.savefig('dist.png')
#plt.show()

#plot bar chart of attrition v salary
pd.crosstab(employee_data.attrition,employee_data.salary).plot(kind='bar')
plt.ylabel('No. of Employees')
#plt.savefig('salary_atr.png')
#plt.show()

#employee atrition by department

pd.crosstab(employee_data.dept,employee_data.attrition).plot(kind='bar')
plt.title('Attrition Frequency for Department')
plt.xlabel('Department')
plt.ylabel('No. of Employees')
plt.show()


employee_data_cat = pd.get_dummies(employee_data_cat)
#print employee_data_cat.head()

#combine numerical and categorical data
employee_data_final = pd.concat([employee_data_num,employee_data_cat],axis=1)
#print employee_data_final.tail()
#data analysis


#model building
target = employee_data_final['attrition']
features = employee_data_final.drop('attrition', axis = 1)

#create the train/test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.4, random_state=10)

#Create the model and train
model = RandomForestClassifier()
model.fit(X_train,y_train)
#predict the results for test
test_pred = model.predict(X_test)
#test the accuracy
print accuracy_score(y_test, test_pred)


#plot chart of factors leading to attrition
feat_importances = pd.Series(model.feature_importances_, index=features.columns)
feat_importances = feat_importances.nlargest(20)
feat_importances.plot(kind='barh')
#plt.savefig('attrition.png')
plt.show()

