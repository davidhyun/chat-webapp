import streamlit as st
import pandas as pd


df = pd.DataFrame({
    'co1': [1,2,3,4],
    'co2': [10,20,30,40]
})

st.write("Hello World")
st.write(df)