
import streamlit as st
import pandas as pd

st.title("Multi Page App Map")
st.write("San Francisco tree data analysis")

trees_df = pd.read_csv("trees.csv")
st.write("Trees by Location")
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)