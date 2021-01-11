from functools import reduce
import pandas as pd
def get_top_features(df,featureRanks,top_n=10):
    featureRanks=featureRanks[[x!=0 for x in featureRanks[1]]]
    if featureRanks.shape[0] < (2*top_n):
        #Top positive features
        highVals=featureRanks[[x>0 for x in featureRanks[1]]].index
        lowVals=featureRanks[[x<0 for x in featureRanks[1]]].index
    else:
        #Top positive features
        highVals=featureRanks.sort_values(by=1,ascending=False)[0:(top_n)].index
        #Top negative features
        lowVals=featureRanks.sort_values(by=1,ascending=True)[0:(top_n)].index

    cols=list(set(list(highVals)+list(lowVals)))
    df_features=df[cols]
    return(df_features)


def merge_dataframes(df_list):
    merged_dfs=reduce(lambda x,y:pd.merge(x,y,left_index=True,right_index=True),df_list)
    return(merged_dfs)
