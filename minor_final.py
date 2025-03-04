# -*- coding: utf-8 -*-
"""Minor_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19RILlEeApicpVQSb2a0aKAm7tnYIO691
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('/content/Toddler Autism dataset final.csv')
print(df)

df.isnull().sum()

df

data1=df.drop(['Case_No','Sex','Ethnicity'],axis=1)

data1

data1=data1.rename(columns={"Class/ASD Traits ":"Class"})

plt.figure(figsize=(11,12))
sns.displot(x=data1.A1,hue=data1.Class)
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A1[data1.Class==0])
sns.distplot(data1.A1[data1.Class==1])
plt.legend(['has ASD','no ASD'])

sns.countplot(x=data1.A2,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A3,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A4,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A5,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A6,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A7,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A8,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A8,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A9,hue=data1.Class)
plt.show()

sns.countplot(x=data1.A10,hue=data1.Class)
plt.show()

plt.figure(figsize=(3,3))
sns.distplot(data1.A2[data1.Class==0])
sns.distplot(data1.A2[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A3[data1.Class==0])
sns.distplot(data1.A3[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A4[data1.Class==0])
sns.distplot(data1.A4[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A5[data1.Class==0])
sns.distplot(data1.A5[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A6[data1.Class==0])
sns.distplot(data1.A6[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A7[data1.Class==0])
sns.distplot(data1.A7[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A8[data1.Class==0])
sns.distplot(data1.A8[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A9[data1.Class==0])
sns.distplot(data1.A9[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.A10[data1.Class==0])
sns.distplot(data1.A10[data1.Class==1])
plt.legend(['has ASD','no ASD'])

plt.figure(figsize=(3,3))
sns.distplot(data1.Age_Months[data1.Class==0])
sns.distplot(data1.Age_Months[data1.Class==1])
plt.legend(['has ASD','no ASD'])

sns.countplot(x=df.Sex,hue=data1.Class)
plt.show()

sns.countplot(x=data1.Jaundice,hue=data1.Class)
plt.show()

plt.figure(figsize=(17,10))
sns.countplot(x=df.Ethnicity,hue=data1.Class)
plt.show()

c=data1.corr()
plt.figure(figsize=(7,12))
sns.heatmap(c,annot=True,cmap='coolwarm')
plt.show()

sns.countplot(x=data1.Family_mem_with_ASD,hue=data1.Class)
plt.show()

from sklearn.preprocessing import LabelEncoder

le1=LabelEncoder()
df.Sex=le1.fit_transform(df.Sex)

le1=LabelEncoder()
df.Ethnicity=le1.fit_transform(df.Ethnicity)

ip=data1.drop(['Class'],axis=1)
op=data1['Class']

import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('Sex',OneHotEncoder(),[1]),
                      ('Ethnicity',OneHotEncoder(),[2])],
                     remainder='passthrough')
ip=np.array(ct.fit_transform(ip),dtype=str)

ip

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(ip,op,test_size=0.2)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(xtr)
sc.fit(xts)
xtr=sc.transform(xtr)
xts=sc.transform(xts)

from sklearn.neighbors import KNeighborsClassifier
alg=KNeighborsClassifier(n_neighbors=3)
alg.fit(xtr,ytr)
yp2=alg.predict(xts)

from sklearn import metrics
accuracy=metrics.accuracy_score(yts,yp2)
recall=metrics.recall_score(yts,yp2)
precision=metrics.precision_score(yts,yp2)
F1_score=metrics.f1_score(yts,yp2)
cf_matrix=metrics.confusion_matrix(yts,yp2)
print(F1_score)
print(precision)
print(recall)
print(accuracy)
print(cf_matrix)

from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
clf.fit(xtr,ytr)
yp1=clf.predict(xts)

from sklearn import metrics
accuracy=metrics.accuracy_score(yts,yp1)
recall=metrics.recall_score(yts,yp1)
precision=metrics.precision_score(yts,yp2)
F1_score=metrics.f1_score(yts,yp2)
cf_matrix=metrics.confusion_matrix(yts,yp1)
print(F1_score)
print(precision)
print(recall)
print(accuracy)
print(cf_matrix)

from sklearn.metrics import roc_curve, auc

KNN_fpr, KNN_tpr, threshold = roc_curve(yts, yp2)
auc_KNN = auc(KNN_fpr, KNN_tpr)

NB_fpr, NB_tpr, threshold = roc_curve(yts, yp1)
auc_NB = auc(NB_fpr, NB_tpr)

plt.figure(figsize=(4, 4), dpi=100)
plt.plot(NB_fpr, NB_tpr, linestyle='-', label='NB (auc = %0.3f)' % auc_NB)
plt.plot(KNN_fpr, KNN_tpr, marker='.', label='KNN (auc = %0.3f)' % auc_KNN)

plt.xlabel('False Positive Rate -->')
plt.ylabel('True Positive Rate -->')

plt.legend()

plt.show()

