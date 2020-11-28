"""
* Name: 3_classify.py
* Description: BIA-660-WS Final Project: Script for Classifying Job Data from Indeed.com (Input comes from 2_parse.py)
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

import csv
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import VotingClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB


def classify(test_file):

    print("Opening and Vectorizing Data Files...")
    # *** Open Train Data
    train_data = pd.read_csv("job_ads.csv", encoding='UTF-8')
    train_df = pd.DataFrame(train_data)
    train_df.columns = ['Text', 'Job_Title']

    # *** Open Test Data
    test_data = pd.read_csv(test_file, encoding='UTF-8')
    test_df = pd.DataFrame(test_data)
    test_df.columns = ["Text"]

    # *** Assign Train Data and Test Data to Variables
    X_train = train_df["Text"]
    y_train = train_df["Job_Title"]
    X_test = test_df["Text"]

    # *** Transform Data into Count Vectors
    count_vectorizer = CountVectorizer()
    X_train_counts = count_vectorizer.fit_transform(X_train)
    X_test_counts = count_vectorizer.transform(X_test)

    print("Training Classification Model and Making Predictions with Voting Classifier...")
    # *** Initialize 3 Classification Algorithms
    lr_clf = LogisticRegression(solver='liblinear', max_iter=10000)
    dt_clf = DecisionTreeClassifier()
    mnb_clf = MultinomialNB()

    predictors = [('lr_clf', lr_clf),
                  ('dt_clf', dt_clf),
                  ('mnb_clf', mnb_clf)]

    # *** Initialize and Fit VotingClassifier
    VT = VotingClassifier(predictors)
    VT.fit(X_train_counts, y_train)

    # *** Predict with VotingClassifier
    predictions = VT.predict(X_test_counts)

    print("Writing Predictions to output.csv file...")
    # *** Write prediction outputs to "output.csv"
    output = open( 'output.csv', 'w', encoding='UTF-8' )
    writer = csv.writer( output, lineterminator='\n' )
    writer.writerow(['predictions'])

    for prediction in predictions:
        writer.writerow([prediction])

    print("Done!")

classify("test.csv")