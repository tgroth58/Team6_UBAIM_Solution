import os
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import GridSearchCV,StratifiedKFold, KFold, cross_validate,train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingClassifier as GBC

#1. Load in the data:

patient_train=pd.read_csv('data_files/Tumor Information_train.csv',index_col=0)
patient_test=pd.read_csv('data_files/Tumor Information_test.csv',index_col=0)

#2. Load in our selected features:
featureSet=pd.read_csv('TOTAL_SELECTED_FEATURES_FINAL.csv',index_col=0)

#3. Create dftrain and dftest
dftrain = patient_train.join(featureSet, how="left")
dftest = patient_test.join(featureSet, how="left")

total_train_dta=pd.concat([dftrain,dftest])

#Gather columns in "train" that aren't the id or labels
cols = [col for col in total_train_dta.columns if col not in ['PatientStatus']]

types = total_train_dta.dtypes
cat_columns = [t[0] for t in types.iteritems() if ((t[1] not in ['int64', 'float64']))]

lbl = preprocessing.LabelEncoder()
for col in cat_columns:
    total_train_dta[col] = lbl.fit_transform(total_train_dta[col].astype(str))

#4. Split the data into train and test again:
train_processed_data = total_train_dta.iloc[:len(dftrain)]
test_processed_data = total_train_dta.iloc[len(dftrain):]

#5. Merge and align data:
# Might want to add PrimarySite, Histology or Grade:
# ------Maybe more feature engnieering here---------

# Parse the features and the output into a model:
covars=[col for col in train_processed_data.columns if col!='PatientStatus']
y_vec_train=train_processed_data[['PatientStatus']].values[:,0]
X_dta_train=train_processed_data[covars]
X_dta_test=test_processed_data[covars]
#Random Forest param grid:

param_Grid={'n_estimators':np.linspace(25,250,10,dtype='int64'),
            'learning_rate':np.logspace(-5,-1.5,5),
            'subsample':np.linspace(0.15,1,10),
            'max_depth':np.linspace(1,10,10,dtype='int64')
            }

classif=GBC()
gb_grid=GridSearchCV(classif,param_grid=param_Grid,cv=10,scoring='roc_auc',n_jobs=2)
gb_grid.fit(X_dta_train,y_vec_train)

#Get best estimator
gb_best=rf_grid.best_estimator_
print('Best Gradient Boost Ensemble AUC:'.format(gb_grid.best_score_))
#Make predictions:
y_test_pred=gb_best.predict_proba(X_dta_test)
#Create response dataframe:
PREDICTIONS=pd.Series(y_test_pred[:,0],index=test_processed_data.index)
PREDICTIONS.to_csv('Team6_GradientBoost_TestSet_Predictions.csv')


