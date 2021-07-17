
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


class news(BaseModel):
    news_text: str


app = FastAPI()

df = pd.read_csv('./Data/train.csv')
df.dropna(inplace=True)
df.reset_index(inplace=True)
df.drop(['index', 'id', 'title', 'author'], axis=1, inplace=True)
lemmatizer = WordNetLemmatizer()


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


df['text'] = df['text'].apply(lambda x: clean_up(x))

X = df['text']
Y = df['label']
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.8, random_state=2)

cv = CountVectorizer(max_features=5000, ngram_range=(1, 3))
x_train = cv.fit_transform(X_train)
x_test = cv.transform(X_test)

filename = './Model/fake_news_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


@app.get('/'):
def home():
    return {'message': 'Success'}


@app.post('/predict'):
async def predict(news: news):
    print(news.news_text)
    input_text = news.news_text
    vectorized_input_text = cv.transform(input_text)
    prediction = loaded_model.predict(vectorized_input_text)
    return prediction
