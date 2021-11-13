import streamlit as st
import pandas as pd
import plotly.express as px
from application_functions import apply_pca


st.set_page_config(layout='wide')
scatter_column, settings_column = st.columns((4,1))

scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")


upload_file = settings_column.file_uploader("Upload File")

if upload_file is not None:
    file_imported = pd.read_csv(upload_file,encoding = "ISO-8859-1")
    pca_data, cat_cols, pca_cols = apply_pca(file_imported)

    categorical_variable = settings_column.selectbox("Select Varaible", options = cat_cols)
    categorical_variable_2 = settings_column.selectbox("Select Second Varaible", options = cat_cols)

    pca_1 = settings_column.selectbox('PCA Component 1', options = pca_cols, index = 0)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox('PCA Component 2', options = pca_cols)

    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x = pca_1, y = pca_2,
                                            color = categorical_variable, template = "simple_white",height = 800, hover_data = [categorical_variable_2]),
                                            use_container_width = True)

else:
    scatter_column.header("Please Upload a File")
