# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:20:17 2020

@author: rjnsa
"""


import pandas as pd
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import requests
import bs4
import string
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import random
import tokenizer

stop_words = set(stopwords.words('english')) 

data = pd.read_csv("D:/Fall 2020/BIA 660/final-project.csv",encoding='latin1')
df= pd.DataFrame(data)
df.columns =['Title', 'Description']

#lowercase
df["Text_1"] = df.Description.str.lower()
#remove \n
df["Text_2"] = df.Text_1.str.replace("\\n", " ")
#remove punctuation and tokenize
df["Tokens"] = df.apply(lambda row: tokenizer.tokenize(row['Text_2']), axis=1)
#remove stopwords
#df['Tokens_1'] = df['Tokens'].apply(lambda x: [item for item in x if item not in stop_words])
df['Tokens_1']= df['Tokens'].astype(str).apply(lambda line: [token for token in word_tokenize(line) if token not in stop_words])
#merge tokens back into string text
df['Text_3']=[" ".join(txt) for txt in df["Tokens_1"].values]
#create bigrams
df["Tokens_2"] = df["Tokens_1"].apply(lambda row: list(ngrams(row, 2)))


X_train, X_test, y_train, y_test = train_test_split(df["Title"], df["Description"], test_size = 0.5, random_state = 2)

# Convert the arrays into a presence/absence matrix


count_vectorizer = CountVectorizer()
X_train_counts = count_vectorizer.fit_transform(X_train)
X_test_counts = count_vectorizer.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
nb_mult_model = MultinomialNB().fit(X_train_counts, y_train)
predicted = nb_mult_model.predict(X_test_counts)

print("Model Accuracy:", accuracy_score(y_test, predicted))


from sklearn.naive_bayes import BernoulliNB
nb_bern_model = BernoulliNB().fit(X_train_counts, y_train)
predicted = nb_bern_model.predict(X_test_counts)

# print the accuracies
print("Model Accuracy:", accuracy_score(y_test, predicted))

#encoder = LabelEncoder()
#y = encoder.fit_transform(df.Title)
#print("y", y)

#To transform the text into something usable, we transform the raw job description text into TFIDF format,
#v = TfidfVectorizer()
#x = df["Description"]
#v.fit(x)
#x_tfidf = v.transform(x)
#print(v.vocabulary_)
#
#
## Classifier - Algorithm - SVM
#s = svm.LinearSVC()
## fit the training dataset on the classifier
#s.fit(x_tfidf, y)# predict the labels on validation dataset
## make predictions using the trained model
#s_pred = s.predict(x_tfidf)
#
## Use accuracy_score function to get the accuracy
#print("SVM Accuracy Score -> ",accuracy_score(s_pred,y))
