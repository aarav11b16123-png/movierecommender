import streamlit as st
import pickle
import pandas as pd
import requests
import urllib.parse

# 1 Load Data
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the dictionary and convert to DataFrame
movies_dict = pickle.load(open('models/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# 2. Re-calculate the similarity matrix on the fly
# This replaces the line: similarity = pickle.load(open('models/similarity.pkl', 'rb'))
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vector = tfidf.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vector)

#  OMDb API Key
OMDB_API_KEY = "8d60250e"

def get_movie_details_omdb(title):
    try:
        title_encoded = urllib.parse.quote(title)
        url = f"http://www.omdbapi.com/?t={title_encoded}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5).json()
        
        if response.get('Response') == "True":
            return {
                "title": response.get('Title', title),
                "year": response.get('Year', "N/A"),
                "director": response.get('Director', "N/A"),
                "actors": response.get('Actors', "N/A"),
                "plot": response.get('Plot', "Plot not available"),
                "poster": response.get('Poster', ""),
                "imdbRating": response.get('imdbRating', "N/A")
            }
        else:
            st.warning(f"OMDb API failed for '{title}': {response.get('Error', 'Unknown error')}")
            return None
    except Exception as e:
        st.error(f"Error fetching details for '{title}': {e}")
        return None

#  Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        details = get_movie_details_omdb(title)
        
        if details:
            recommended_movies.append(details)
        else:
            # fallback if OMDb fails
            recommended_movies.append({
                "title": title,
                "year": "N/A",
                "plot": "Plot not available",
                "poster": "",
                "imdbRating": "N/A"
            })
    return recommended_movies

#  Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Search your favourite movie here:",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    
    
    cols = st.columns(5)
    
    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            if movie['poster']:
                st.image(movie['poster'], width=120)  # smaller poster
            st.markdown(f"**{movie['title']} ({movie['year']})**")
            st.markdown(f"IMDb: {movie['imdbRating']}")
            st.caption(movie['plot'][:100] + '...')  # short plot for compact layout