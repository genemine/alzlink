#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:53:56 2021

@author: lincxcsu
"""


import numpy as np
import pandas as pd
import random

from sklearn.ensemble import  ExtraTreesClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve



data=pd.read_csv('mat_training.txt',index_col=0,header=0,sep='\t')

mat2pred=pd.read_csv('mat2pred.txt',index_col=0,header=0,sep='\t')


model=ExtraTreesClassifier(n_estimators = 500,class_weight = "balanced_subsample", n_jobs = -1, bootstrap = True)
 
#cross validation score
AUROC=[]
AUPRC=[]

#score: to store prediction of models
score=pd.Series(np.zeros((len(mat2pred))))
score.index=mat2pred.index


times=100
for i in range(times):
    print('Iteration: '+str(i)+'/'+str(times))
    index=random.sample(list(data.index),len(data.index))
    data_new=data.loc[index,:]
    X=data_new.iloc[:,0:-1]
    y=data_new.iloc[:,-1]
    skf = StratifiedKFold(n_splits=5)
    y_pred=pd.Series([])
    y_new=pd.Series([])
    for train,test in skf.split(X,y):
        # training-test data
        X_train, X_test = X.iloc[train,:], X.iloc[test,:]
        y_train, y_test = y.iloc[train], y.iloc[test]
        # fit a model
        model.fit(X_train,y_train)
        # make predictions for posi-nega genes
        pred=model.predict_proba(X_test)[:,1]
        y_predi=pd.Series(pred)
        y_predi.index=y_test.index
        y_new=y_new.append(y_test)
        y_pred=y_pred.append(y_predi)
        # make predictions for unknown genes 
        Pred=model.predict_proba(mat2pred)[:,1]
        Pred=pd.Series(Pred)
        Pred.index=score.index
        score=score+Pred
    #store AUROC and AUPRC each time
    AUROC.append(round(roc_auc_score(y_new, y_pred),4))
    AUPRC.append(round(average_precision_score(y_new, y_pred),4))


score=score/(times*5)
prediction=score.sort_values(ascending=False)
prediction=prediction.round(4)
prediction=pd.DataFrame(prediction)
prediction.columns=['Score']
prediction.to_csv('prediction.txt',sep='\t')



        