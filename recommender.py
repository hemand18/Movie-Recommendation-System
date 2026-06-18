import pandas as pd

print("Step 1: Loading dataset")

movies = pd.read_csv("dataset/movies.csv")

print("Step 2: Dataset loaded")

print(movies.columns.tolist())

print("Step 3: Import successful")

def recommend(movie_name):
    return ["Test Movie 1", "Test Movie 2"]