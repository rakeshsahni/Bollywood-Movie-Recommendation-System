# Bollywood Movie Recommendation System

If you want to built contact me : https://sohipm.com

Hi! I am Rakesh Sahni B.E Final year computer science.
Current website : https://sohipm.com

#### used library
flask, sklearn, numpy, pandas, matplotlib, seaborn etc.


process to build this app

1.) First stage is undoubtly data acquisition -> https://www.kaggle.com/datasets/pncnmnp/the-indian-movie-database

Before jump any calculation we need to clean data first of all using spacy ( NLP )
2.) In NLP data cleaning and data munging is one of the crucial part we have to remove punctuation, stop words, html tag. spell correct etc. To do so i have used spacy nlp library

3.) I also consider imdb rating and imdb votes which is present in numeric form i converted to categorical form like low_raing, medium_rating, high_rating, very_high_rating

4.) Once data preproces complited after that i create tag for each movie on the basis of movie story, summary, rating, votes, genres and actors.

5.) After creating tags for each movie then I have converted these tags into vectors using CountVectorizer and TfidfVectorizer

6.) Once created vector for each movie it is easy to find similarity between two vector means two movies using cosine similarity ( cosine_similarity ).

7.) At end sort the similarity and extract top 5 movies among all movies and that movie show in our flask app.

## Installation

open terminal and type simply

```bash
pip install -r requirements.txt
```

After installation all python package simply write command in terminal

```bash
python app.py
```
Remember you are in app ( root ) folder

#### Thank you!
