import os
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.model_selection import GridSearchCV,StratifiedKFold, KFold, cross_validate
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.linear_model import LogisticRegression as LogR
from sklearn.preprocessing import OneHotEncoder
from itertools import chain

def merge_files(base_filename,filename):
  base = '/home/'
  base_df = pd.read_csv(base + base_filename,index_col=0)
  filename_df = pd.read_csv(base + filename+ ".csv",index_col=0)
  train_data = base_df.join(filename_df)
  return train_data

# Parsing Functions:

def get_integer_cols(df):
  int_type_cols=df.columns[[x=='int64' for x in df.dtypes]]
  df_res=df[int_type_cols]
  return(df_res)
def get_floats(df):
  float_type_cols=df.columns[[x=='float64' for x in df.dtypes]]
  df_res=df[float_type_cols]
  return(df_res)
def get_strings(df):
  str_type_cols=df.columns[[x!='int64' and x!='float64' for x in df.dtypes]]
  df_res=df[str_type_cols]
  return(df_res)

# Discrete data processing:

def filter_missing_data(df,missing_frac):
  missing_entry_vals=[66,99,77,88,666,999]
  #For all the columns in a data frame, removes columns where the fraction of 
  # entries exceeds "missing_frac" fraction of data
  keep_inds=df.apply(lambda x:(sum([y in missing_entry_vals for y in x])/len(x))<missing_frac,axis=0)
  df_res=df[keep_inds[[y is True for y in keep_inds]].index]
  return(df_res)

def compute_entropy(x):
  value_freq=pd.Series(x).value_counts(normalize=True,sort=False)
  return(- sum(value_freq*np.log(value_freq)) )

def filter_lowInfo_cols(df,thresh=1):
  #Filters out columns that have low entropy (there isn't much variability in the category):
  keep_inds=df.apply(lambda x:compute_entropy(x)>thresh)
  df_res=df[keep_inds[[y is True for y in keep_inds]].index]
  return(df_res)

def filter_lowInfo_cols_ohe(df,thresh=0.15):
  #Filters out columns that have low diversity based on threshold (lots of 1 or 0)
  keep_inds=df.apply(lambda x:(sum(x)/len(x))>thresh,axis=0)
  df_res=df[keep_inds[[y is True for y in keep_inds]].index]
  return(df_res)

def oneHot_wrapper(df_disc):
  #Convert discrete df into one hot encodings:
  enc=OneHotEncoder(handle_unknown='ignore')
  enc.fit(df_disc)
  new_colnames=[]
  for i in range(df_disc.shape[1]):
    for j in range(len(enc.categories_[i])):
      new_colnames.append(df_disc.columns[i]+"_"+str(enc.categories_[i][j]))
  new_disc_df=pd.DataFrame(enc.transform(df_disc).toarray(),index=df_disc.index,columns=new_colnames)
  return(new_disc_df)

#Continuous data processing:
from sklearn import preprocessing
def normalize_data(df):
  df_dta = df.apply(lambda x: np.log10(x+1))
  df_dta = preprocessing.StandardScaler().fit(df_dta).transform(df_dta)
  new_df=pd.DataFrame(data=df_dta,columns=df.columns,index=df.index)
  return new_df

def preprocess_main(df):
  # Filters and processes df columns:
  #1. Categorical data processing:
  cat_dta=get_integer_cols(df)
  if cat_dta.shape[1]!=0:
    cat_filt=filter_missing_data(cat_dta,missing_frac=0.5)
    cat_ohe=oneHot_wrapper(cat_filt)
    cat_dta=filter_lowInfo_cols_ohe(cat_ohe,thresh=0.15)
  
  #2. Float normalization:
  float_dta=get_floats(df)
  if float_dta.shape[1]!=0:
      float_dta=normalize_data(float_dta)
  
  #Merge data together:
  final_df=cat_dta.join(float_dta,how='left')
  return(final_df)

def extract_features_logistic(input_df,cvs):
  #Wraps up an skl model into a fitting routine
  #0. parse the features and the output into a model:
  y_vec=input_df[['PatientStatus']].values[:,0]
  covars=[col for col in input_df.columns if col!='PatientStatus']
  X_dta=input_df[covars]
  #1. Separate data into train test split:
  
 
  mdl=LogR(penalty='l1',solver='liblinear')
  paramGrid={'C':np.logspace(-2,3,10)}
  fit_obj=GridSearchCV(mdl,param_grid=paramGrid,scoring='roc_auc',cv=cvs)
  fit_obj.fit(X_dta,y_vec)
  #Store the best score:
  best_roc=fit_obj.best_score_
  fit_obj=fit_obj.best_estimator_
  #Extract features:
  coefficients=pd.Series(data=fit_obj.coef_[0,:],index=X_dta.columns)
  return best_roc,coefficients
