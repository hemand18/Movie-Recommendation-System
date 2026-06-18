import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite movie.")

try:
    # Import recommendation function
    from recommender import recommend

    # Load dataset
    movies = pd.read_csv("dataset/movies.csv")

    st.success("Application loaded successfully!")

    # Movie selection
    selected_movie = st.selectbox(
        "Select a Movie",
        movies['title'].values
    )

    # Recommend button
    if st.button("Recommend Movies"):

        recommendations = recommend(selected_movie)

        st.subheader("Recommended Movies")

        if recommendations:
            for movie in recommendations:
                st.write(f"✅ {movie}")
        else:
            st.warning("No recommendations found.")

except FileNotFoundError as e:
    st.error(f"Dataset file not found: {e}")

except ImportError as e:
    st.error(f"Import error: {e}")

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.exception(e)