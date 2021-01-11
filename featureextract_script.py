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
# "util_files.py" contains all custom preprocessing scripts 
# for metadata:
from util_files import *

# inputFile can be read from stdin on the command line, 
# or it can be specified with a path as a variable:
inputFile=sys.argv[1]
inputFile='data_files/Lifetime use of Supplements.csv'
#Capture the name of the dataset as a prefix:
dta_prefix=inputFile.split('.csv')[0].split('/')[-1]

#MAIN PIPELINE

#1. load files
# train_dta=pd.read_csv('data_files/Tumor Information_train.csv',index_col=0)
feature_data=pd.read_csv(inputFile,index_col=0).fillna(value=0)
# -----Might need to add further processing to data ---------

#feature_data=merge_files("Tumor information_train.csv",inputFile)
#2. Feature Trimming
# "preprocess_main": comes from "util_files.py"
# Does the following to input data:
#  -Filters categorical data where more than 50% of information is "missing", converts categorical data into one hot encodings, then finally removes data where the majority of one hot encodings are 1 or 0 (threshold set to 15% or less of either 1 or 0)
#  - All continuous data are log-normalized and z-scored.  Some data were found to be log-normally distributed. This approach would still be valid even when applied to normally distributed data as well.
proc_dta=preprocess_main(feature_data)
#The preprocessed feature matrix is then written to a .csv file:
proc_dta.to_csv(dta_prefix+'_'+'new_featureMat.csv',sep=',')

# During feature selection, we remove the "PrimarySite","Histology","Grade", and "SEERSummStage2000" variable from the matrix.  We only want to assess data-specific variables here.
feature_data_merge=train_dta.join(proc_dta).drop(['PrimarySite','Histology','Grade','SEERSummStage2000'],axis=1)

#3. Feature Selection
# The "extract_features_logistic" function from "util_files.py" will do the following:
#  - Runs a logistic regression with L1 penalty, with varying degress of regularization
#    * Regularization occurs over 10 logrithmically spaced values from 10^-2 to 10^3
#    * Logistic regression is cross-validated over the data.  This script specifies the number of cross validations "cvs" to 10
#  - Features and their weights are then stored in a pandas series for further processing
best_score,features=extract_features_logistic(feature_data_merge,cvs=10)
print('Best estimator AUC score: {0}'.format(best_score))
#4. Saving
features.to_csv(dta_prefix+'_featureVector.csv',sep=',')
