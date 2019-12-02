import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import Series, DataFrame

employee_data = pd.ExcelFile('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx')
employee_existing = employee_data.parse('Existing employees')
left_employee_left = employee_data.parse('Employees who have left')

#print left_employee.shape
#add attrition column
existing_employee = existing_employee.assign(attrition='no')
left_employee = left_employee.assign(attrition='yes')

all_employee = pd.concat([existing_employee,left_employee])
#print all_employee.head()

#print all_employee.shape

attr = {'yes':1, 'no':0}

all_employee.attrition = [attr[item] for item in all_employee.attrition]



all_employee['dept']=np.where(all_employee['dept'] =='support', 'technical', all_employee['dept'])
all_employee['dept']=np.where(all_employee['dept'] =='IT', 'technical', all_employee['dept'])


#print all_employee['dept'].unique()

#Data exploration

#print all_employee.groupby('attrition').mean()
print '##******************######################'

#print all_employee.groupby('dept').mean()
print '**************department******************'

#print all_employee.groupby('salary').mean()
print '**************salary******************'

#DATA VISUALISATION

print '**************Department******************'
pd.crosstab(all_employee.dept,all_employee.attrition).plot(kind='bar')
plt.title('Attrition Frequency for Department')
plt.xlabel('Department')
plt.ylabel('Frequency of Attrition')
#plt.show()
#plt.savefig('department_bar_chart')

print '**************salary******************'
table=pd.crosstab(all_employee.salary, all_employee.attrition)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Attrition')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
#plt.savefig('salary_bar_chart')

#creating dummy variables for categorical data
all_employee = pd.get_dummies(all_employee)
print all_employee.head()

#existing.hist(figsize=(20,20))
#plt.show()
