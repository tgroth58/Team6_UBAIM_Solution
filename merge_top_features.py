import os
import pandas as pd
#Code responsible for extracting top_n features from featureMats based on featureVectors 
from parse_top_featureData import *

#Get the feature matrices loaded into a list:
fPath='./feature_files/'
fNames=list([x.split('_new_featureMat.csv')[0] for x in os.listdir(fPath) if '_new_featureMat.csv' in x])
featureMat_list=[pd.read_csv(fPath+x+'_new_featureMat.csv',index_col=0) for x in fNames]
#Get the top features loaded into a list:
topFeatures_List=[pd.read_csv(fPath+x+'_featureVector.csv',index_col=0,header=None) for x in fNames]
#Get top feature matrices:
topFeatureMat_list=[get_top_features(x,y) for x,y in zip(featureMat_list,topFeatures_List)]
#Merge the data
merged_topFeatures=merge_dataframes(topFeatureMat_list)
