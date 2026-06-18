import streamlit as st

st.title("Debug Test")

st.write("Step 1")

import pandas as pd

st.write("Step 2")

movies = pd.read_csv("dataset/movies.csv")

st.write("Step 3")

from recommender import recommend

st.write("Step 4")

st.success("Everything loaded successfully!")