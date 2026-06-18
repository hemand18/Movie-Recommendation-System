import streamlit as st
import pandas as pd
from recommender import recommend

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

movies = pd.read_csv("dataset/movies.csv")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎬 Movie Recommender")

st.sidebar.info("""
### AI Movie Recommendation System

Built using:

- Python
- Streamlit
- Pandas
- Scikit-Learn
- Machine Learning

Algorithm:
Content-Based Filtering + Cosine Similarity
""")

st.sidebar.success("✅ Model Loaded Successfully")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎬 AI Movie Recommendation System")

st.markdown("""
Discover movies similar to your favorites using
Machine Learning and Content-Based Filtering.
""")

st.divider()

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎥 Total Movies",
        value=len(movies)
    )

with col2:
    st.metric(
        label="🤖 AI Model",
        value="Active"
    )

with col3:
    st.metric(
        label="⚡ Recommendations",
        value="Instant"
    )

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    "🎬 Recommendations",
    "📊 Analytics",
    "ℹ️ About"
])

# ==================================================
# TAB 1
# ==================================================

with tab1:

    st.subheader("Find Similar Movies")

    selected_movie = st.selectbox(
        "Choose a Movie",
        movies["title"].values
    )

    if st.button("🚀 Recommend Movies"):

        recommendations = recommend(selected_movie)

        st.success(
            f"Top recommendations for: {selected_movie}"
        )

        cols = st.columns(2)

        for i, movie in enumerate(recommendations):

            with cols[i % 2]:
                st.info(f"🎬 {movie}")

# ==================================================
# TAB 2
# ==================================================

with tab2:

    st.subheader("Dataset Insights")

    st.write("Movies Available in Dataset")

    genre_counts = (
        movies["genres"]
        .fillna("Unknown")
        .str.split("|")
        .explode()
        .value_counts()
        .head(10)
    )

    st.bar_chart(genre_counts)

    st.write("Top Genres")

    st.dataframe(
        genre_counts.reset_index(),
        use_container_width=True
    )

# ==================================================
# TAB 3
# ==================================================

with tab3:

    st.subheader("About Project")

    st.write("""
This project uses Machine Learning techniques
to recommend movies based on similarity.

### Technologies Used
- Python
- Pandas
- Scikit-Learn
- Streamlit

### Machine Learning Concepts
- Content-Based Filtering
- Count Vectorization
- Cosine Similarity

### Features
- Personalized Recommendations
- Interactive Dashboard
- Real-Time Predictions
- Data Visualization
""")

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Built with ❤️ using Streamlit and Machine Learning"
)