
import streamlit as st
import pandas as pd

st.title("Editing Example")
st.write("San Francisco tree data analysis")

trees_df = pd.read_csv("trees.csv")
st.write("Trees by Location")
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df_filtered = trees_df[trees_df["legal_status"] == "Private"] #fixed filter
#st.dataframe(trees_df_filtered)
#st.experimental_data_editor(trees_df_filtered)
edited_df = st.data_editor(trees_df_filtered)

trees_df.loc[edited_df.index] = edited_df #find the index of the filter and update
if st.button("Save data and overwrite..."):
    trees_df.to_csv("trees.csv", index=False)
    st.write("SAVED!")