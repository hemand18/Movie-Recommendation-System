import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
movies = pd.read_csv("dataset/movies.csv")

# Handle missing values
movies['genres'] = movies['genres'].fillna('')

# Convert genres into vectors
cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(movies['genres'])

# Calculate similarity
similarity = cosine_similarity(vectors)

def recommend(movie_name):
    try:
        movie_index = movies[movies['title'] == movie_name].index[0]

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

    except:
        return ["Movie not found"]