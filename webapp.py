import streamlit as st
import pickle
import pandas as pd

similarity=pickle.load(open('similarity1.pkl','rb'))
def reccomend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances= similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse= True,key=lambda x:x[1])[1:11]
    reccomended_movies=[]
    for i in movies_list:
        reccomended_movies.append(movies.iloc[i[0]].title)
    return reccomended_movies
st.caption("made by tanisha jain")

st.title('MOVIE RECCOMENDER SYSTEM')
movie_dict= pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movie_dict)
SELECTED_MOVIE_NAME= st.selectbox('choose a movie',movies['title'].values)

if st.button("RECCOMEND"):
    rec= reccomend(SELECTED_MOVIE_NAME)
    for i in rec:
        st.write(i)


