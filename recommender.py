import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("dataset/movies.csv")

movies["genres"] = movies["genres"].fillna("")

cv = CountVectorizer(stop_words="english")

vectors = cv.fit_transform(movies["genres"])

similarity = cosine_similarity(vectors)

def recommend(movie_name):

    movie_index = movies[
        movies["title"] == movie_name
    ].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations