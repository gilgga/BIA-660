"""
* Name: 3_classify.py
* Description: BIA-660-WS Final Project: Script for Classifying Job Data from Indeed.com (Input comes from 2_parse.py)
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("job_ads.csv", encoding='UTF-8')
df= pd.DataFrame(data)
df.columns =['Text', 'Job_Title']

X_train, X_test, y_train, y_test = train_test_split(df["Text"], df["Job_Title"], test_size = 0.5, random_state = 2)

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
