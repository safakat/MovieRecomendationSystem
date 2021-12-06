import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Movie Recomendation System")

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies_df = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recomended_movie(movie):
    movie_index = movies_df[movies_df.title == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]
    for i in movies_list:
        st.write(movies_df.iloc[i[0]].title)

option = st.selectbox('How would you like to be contacted?',movies_df.title.values)

if st.button('Show Me Good Stuff'):
    recomended_movie(option)
else:
    st.write('Select a movie')