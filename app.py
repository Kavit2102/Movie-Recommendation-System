import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movies.pkl", "rb") as m:
    movies = pickle.load(m)

similarity = joblib.load("similarities.joblib")

movie_names = movies['title'].values

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0] # Get the index of the selected movie
    recommendations = similarity[movie_index] # Get the similarity scores for the selected movie

    movies_list = sorted(list(enumerate(recommendations)), reverse=True, key=lambda x: x[1])[1:6] # Get the top 5 recommended movies (excluding the selected movie itself)
    recommended_movies = []

    # Display the recommended movies
    for i in movies_list: 
        recommended_movies.append(movies.iloc[i[0]].title) # Get the movie title using the index

    return recommended_movies

movie_name = st.selectbox("Select a movie:", movie_names)

if st.button("Recommend"):
    r = recommend(movie_name)

    st.write("Recommended Movies:")

    for i in r:
        st.write(i.title())

    