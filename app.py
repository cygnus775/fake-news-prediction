
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle


from fastapi import FastAPI
from pydantic import BaseModel

lemmatizer = WordNetLemmatizer()

df = pd.read_csv('Data/cleaned.csv')
X = df['text']
Y = df['label']
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.8, random_state=2)
print('ok till train test split')
cv = CountVectorizer(max_features=5000, ngram_range=(1, 3))
x_train = cv.fit_transform(X_train)
filename = './Model/fake_news_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print('Fullly up!')


def clean_up(x):
    s = re.sub('[^a-zA-Z]', " ", x)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(s)
    filtered_sentence = [w.lower()
                         for w in word_tokens if not w.lower() in stop_words]
    fin = []
    for w in filtered_sentence:
        fin.append(lemmatizer.lemmatize(w))
    return " ".join(fin)


class news(BaseModel):
    news_text: str


app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'Success'}


@app.post('/predict')
def predict(news: news):
    """ df = pd.read_csv('Data/cleaned.csv')
    X = df['text']
    Y = df['label']
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.8, random_state=2)
    print('ok till train test split')
    cv = CountVectorizer(max_features=5000, ngram_range=(1, 3))
    x_train = cv.fit_transform(X_train)
    filename = './Model/fake_news_model.sav'
    loaded_model = pickle.load(open(filename, 'rb')) """
    input_text = news.news_text
    print(type(input_text))
    print("ok till input_text")
    clean_text = clean_up(input_text)
    vectorized_input_text = cv.transform([clean_text])
    prediction = loaded_model.predict(vectorized_input_text)
    pred_dict = {'prediction': int(prediction)}

    return pred_dict
