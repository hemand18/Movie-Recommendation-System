import streamlit as st
import pandas as pd

st.title("🎬 Movie Recommendation System")

# Test dataset
movies = pd.read_csv("dataset/movies.csv")
st.success("Dataset Loaded Successfully!")

# Test recommender import
try:
    from recommender import recommend
    st.success("Recommender Imported Successfully!")
except Exception as e:
    st.error(f"Import Error: {e}")
    st.stop()

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    try:
        recommendations = recommend(selected_movie)

        st.success("Recommendation Function Executed!")

        for movie in recommendations:
            st.write(movie)

    except Exception as e:
        st.error(f"Recommendation Error: {e}")