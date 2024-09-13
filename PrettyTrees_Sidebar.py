import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout='wide')

st.title("Trees, now with Columns")
st.write("San Francisco tree data analysis")
tab1, tab2, tab3 = st.tabs(["Filter", "Charts", "Map"])

trees_df = pd.read_csv("trees.csv")
today = pd.to_datetime("today")
trees_df["date"] = pd.to_datetime(trees_df["date"])
trees_df["age"] = (today - trees_df["date"]).dt.days
unique_caretakers = trees_df["caretaker"].unique()

owners = st.sidebar.multiselect("Tree Owner Filter", unique_caretakers)

if owners: 
    trees_df= trees_df[trees_df["caretaker"].isin(owners)]
df_trees_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_trees_grouped.columns = ['tree_count']

with tab1:
    st.line_chart(df_trees_grouped)

with tab2:
    col1, col2 = st.columns(2) #if you move to tabs, does it still share data?

    with col1:
        fig = px.histogram(trees_df, x=trees_df["dbh"], title="Tree Width")
        st.plotly_chart(fig)

    with col2:
        fig = px.histogram(trees_df, x=trees_df["age"], title="Tree Age")
        st. plotly_chart(fig)

with tab3:
    st.write("Trees by Location")
    trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
    trees_df = trees_df.sample(n=1000, replace=True)
    st.map(trees_df)