import sys
import os
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.model_selection import GridSearchCV,StratifiedKFold, KFold, cross_validate
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.linear_model import LogisticRegression as LogR
from sklearn.preprocessing import OneHotEncoder
from itertools import chain

from util_files import *
inputFile=sys.argv[1]

def get_top_features(df,featureRanks,top_n=10):
    #Top positive features
    highVals=featureRanks.sort_values(by=1,ascending=False)[0:(top_n)].index
    #Top negative features
    lowVals=featureRanks.sort_values(by=1,ascending=True)[0:(top_n)].index
    cols=list(highVals)+list(lowVals)
    df_features=df[cols]
    return(df_features)


from functools import reduce
def merge_dataframes(df_list):
  return(reduce(lambda left,right:pd.merge(left,right,left_index=True,right_index=True),df_list))

newFeatures='Food Habits_new_featureMat.csv'
topFeatureVec='Food Habits_featureVector.csv'
nf_mat=pd.read_csv(newFeatures,index_col=0)
tf_mat=pd.read_csv(topFeatureVec,index_col=0,header=None)

topFeatureMat=get_top_features(nf_mat,tf_mat)
topFeatureMat.to_csv('Food Habits_topFeatures.csv')

dta_prefix=inputFile.split('.csv')[0].split('/')[-1]
featureWeights=pd.read_csv('')
feature_data=pd.read_csv(inputFile,index_col=0).fillna(value=0)
# -----Might need to add further processing to data ---------




#feature_data=merge_files("Tumor information_train.csv",inputFile)
#2. Feature Trimming
proc_dta=preprocess_main(feature_data)
proc_dta.to_csv(dta_prefix+'_'+'new_featureMat.csv',sep=',')
feature_data_merge=train_dta.join(proc_dta).drop(['PrimarySite','Histology','Grade','SEERSummStage2000'],axis=1)
#3. Feature Selection
best_score,features=extract_features_logistic(feature_data_merge,cvs=10)
print('Best estimator AUC score: {0}'.format(best_score))
#4. Saving
features.to_csv(dta_prefix+'_featureVector.csv',sep=',')
