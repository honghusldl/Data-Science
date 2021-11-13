import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as ex
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def apply_pca(df):
    missing = df.isnull().sum()
    col_to_drop = df.columns[missing > len(df) * 0.2]
    df.drop(columns = col_to_drop,inplace = True)
    
    numerical_col = []
    categorical_col = []

    for i in df.columns:
        if df[i].dtype == np.dtype('float64') or df[i].dtype == np.dtype('int64'):
            numerical_col.append(df[i])
        else:
            categorical_col.append(df[i])

    numerical_df = pd.concat(numerical_col,axis = 1)
    categorical_df = pd.concat(categorical_col,axis=1)
    categorical_col_names = list(categorical_df.columns)

    numerical_df = numerical_df.apply(lambda x: x.fillna(np.mean(x)))

    # set up scaler
    scaler = StandardScaler() 
    scaled_values = scaler.fit_transform(numerical_df)

    # set up PCA
    pca = PCA()
    pca_values = pca.fit_transform(scaled_values)
    pca_values = pd.DataFrame(pca_values)

    new_col = ['PCA_' + str(i) for i in range(1,len(pca_values.columns) + 1)]
    old_col = list(pca_values.columns)
    col_mapper = dict(zip(old_col,new_col))

    pca_values.rename(columns=col_mapper, inplace = True)

    # output
    output = pd.concat([df, pca_values],axis = 1)

    return output, categorical_col_names, new_col