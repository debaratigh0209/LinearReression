# -*- coding: utf-8 -*-
"""logistic_reggression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZewFHula9mjMjKxNtFBX6ZXi2rZbqlln
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import classification_report

claimants=pd.read_csv("/content/drive/MyDrive/claimants.csv")
claimants

claimants.drop(["CASENUM"],inplace=True,axis=1)
sb.countplot(x="ATTORNEY",data=claimants,palette="hls")
pd.crosstab(claimants.ATTORNEY,claimants.CLMINSUR).plot(kind="bar")
sb.countplot(x="CLMSEX",data=claimants,palette="hls")

sb.countplot(x="ATTORNEY",data=claimants,palette="hls")
pd.crosstab(claimants.ATTORNEY,claimants.CLMINSUR).plot(kind="bar")
sb.countplot(x="CLMSEX",data=claimants,palette="hls")

pd.crosstab(claimants.ATTORNEY,claimants.CLMINSUR).plot(kind="bar")

sb.countplot(x="CLMSEX",data=claimants,palette="hls")

claimants.isnull().sum()

claimants.shape

claimants.dropna().shape

claimants.CLMSEX.mode()
claimants.CLMINSUR.mode()

claimants['CLMSEX'].fillna(1,inplace=True)

claimants['CLMINSUR'].fillna(1,inplace=True)

claimants.SEATBELT.mean()

claimants['SEATBELT'].fillna(0,inplace=True)

claimants.CLMAGE.mean()

claimants['CLMAGE'].fillna(28.4144,inplace=True)

claimants.isnull().sum()

x=claimants.iloc[:,[1,2,3,4,5]]
y=claimants.iloc[:,0]
Classifier=LogisticRegression()

Classifier=LogisticRegression()

Classifier.fit(x,y)

Classifier.coef_

Classifier.predict_proba(x)

y_pred=Classifier.predict(x)

y_prob=pd.DataFrame(Classifier.predict_proba(x.iloc[:,:]))

new_df=pd.concat([claimants,y_prob],axis=1)

from sklearn.metrics import confusion_matrix
cf=confusion_matrix(y,y_pred)
cf

accuracy=sum(y==y_pred)/claimants.shape[0]
accuracy

pd.crosstab(y,y_pred)