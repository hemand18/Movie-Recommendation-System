import streamlit as st
import pandas as pd
from recommender import recommend

# Page Config
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Load Dataset
movies = pd.read_csv("dataset/movies.csv")

# Sidebar
st.sidebar.title("🎬 Movie Recommender")

st.sidebar.info("""
### About

This AI-powered Movie Recommendation System suggests movies based on genre similarity.

### Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-Learn

### Algorithm
Content-Based Filtering
Cosine Similarity
""")

# Header
st.title("🎬 AI Movie Recommendation System")
st.write(
    "Discover movies similar to your favorites using Machine Learning."
)

st.divider()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Movies Available", len(movies))

with col2:
    st.metric("Recommendation Engine", "AI Powered")

with col3:
    st.metric("Status", "Online")

st.divider()

# Movie Selection
selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies["title"].values
)

# Recommendation Button
if st.button("🚀 Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("⭐ Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.success(f"{i}. {movie}")

st.divider()

# Analytics Section
st.subheader("📊 Dataset Insights")

try:
    genre_counts = (
        movies["genres"]
        .fillna("Unknown")
        .str.split(r"\|")
        .explode()
        .value_counts()
        .head(10)
    )

    st.bar_chart(genre_counts)

except Exception:
    st.info("Genre analytics unavailable.")

# Dataset Preview
with st.expander("📄 View Dataset Sample"):
    st.dataframe(movies.head())

# Footer
st.divider()

st.caption(
    "Built with ❤️ using Python, Streamlit, Pandas and Scikit-Learn"
)