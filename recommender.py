import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
movies = pd.read_csv("dataset/movies.csv")

# Handle Missing Values
movies["genres"] = movies["genres"].fillna("")

# Feature Extraction
cv = CountVectorizer(stop_words="english")

vectors = cv.fit_transform(
    movies["genres"]
)

# Similarity Matrix
similarity = cosine_similarity(vectors)

# Recommendation Function
def recommend(movie_name):

    matches = movies[
        movies["title"] == movie_name
    ]

    if len(matches) == 0:
        return ["Movie not found"]

    movie_index = matches.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations