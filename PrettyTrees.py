import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')

st.title("Trees, now with Columns")
st.write("San Francisco tree data analysis")

first_width = st.number_input("First Width?", min_value=1, value=1)
second_width = st.number_input("Second Width?", min_value=1, value=1)
third_width = st.number_input("Third Width?", min_value=1, value=1)

trees_df = pd.read_csv("trees.csv")

df_trees_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_trees_grouped.columns = ['tree_count']


#df_trees_grouped['new col'] = np.random.randn(len(df_trees_grouped)) * 1000
#st.line_chart(df_trees_grouped)




col1, col2, col3 = st.columns((first_width, second_width, third_width), gap="large")
with col1:
    st.line_chart(df_trees_grouped)
with col2:
    st.bar_chart(df_trees_grouped)
with col3:
    st.area_chart(df_trees_grouped)


#or
# col1.write("Other Col1")
# col2.write("Other Col2")
# col3.write("Other Col3")