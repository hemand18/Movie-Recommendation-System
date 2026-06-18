import streamlit as st
import pandas as pd

movies = pd.read_csv("dataset/movies.csv")

st.write("Columns in Dataset:")
st.write(movies.columns.tolist())

st.write(movies.head())