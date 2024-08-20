# Content-Based Movie Recommendation System

This project is a content-based filtering movie recommendation system that suggests movies to users based on the similarity of movie features using cosine similarity. The system is built with Python and Streamlit for the web interface and  uses a Jupyter Notebook for the implementation and demonstration.
![movie1](https://github.com/user-attachments/assets/b85a1956-56d2-4239-9a53-b022c28624c7)
![movie2](https://github.com/user-attachments/assets/1c984d98-048d-433a-8959-2c60612f9f48)



## Project Overview

The movie recommendation system takes user input for a favorite movie and suggests similar movies based on cosine similarity between the movie vectors. This system uses metadata such as genres, keywords, cast, and crew to compute the similarity score between movies.

## Features

- Suggests movies similar to the user's input based on movie metadata
- Uses cosine similarity to measure the similarity between movie vectors
- Web interface built using Streamlit
- Easy-to-use interface with instant recommendations

## Requirements

- Python 3
- Streamlit
- Pandas
- NumPy
- Pickle (for saving and loading pre-processed data)
- scikit-learn

Download from releases:
similarity1.pkl
tmdb_5000_credits.xls

Install the required Python packages:
pip install jupyter pandas numpy scikit-learn pickle

Run project using webapp.py:
streamlit run webapp.py



