"""
* Name: classifier.py
* Description: BIA-660-WS Homework 7 - Classification II
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

"""
A simple script that demonstrates how we can use grid search to set the parameters of a classifier
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier

# *** 5 Classification Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

# *** Read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')
        reviews.append(review.lower())
        labels.append(rating)
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')

# *** Build a counter based on the training dataset
counter = CountVectorizer(stop_words=stopwords.words('english'))
counter.fit(rev_train)

# *** Count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


# *** =======================================================================================
# *** Initialize 5 Classification Algorithms
lr_clf = LogisticRegression(solver='liblinear', max_iter=10000)
dt_clf = DecisionTreeClassifier()
knn_clf = KNeighborsClassifier()
rf_clf = RandomForestClassifier()
svm_clf = LinearSVC(max_iter=10000)

# *** Create parameter grids for every algorithm
lr_pgrid = [{'penalty': ['l1', 'l2'], 'class_weight': [None, 'balanced']}]
dt_pgrid = [{'criterion': ['gini', 'entropy'], 'class_weight': [None, 'balanced']}]
knn_pgrid = [{'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'weights':['uniform', 'distance']}]
rf_pgrid = [{'criterion': ['gini', 'entropy'], 'class_weight': ['balanced', 'balanced_subsample']}]
svm_pgrid = [{'loss': ['hinge', 'squared_hinge'], 'class_weight': [None, 'balanced']}]

# *** Initialize and Fit GridSearchCV for every algorithm
lr_gridsearch = GridSearchCV(lr_clf, lr_pgrid, cv=5, n_jobs=-1)
lr_gs = lr_gridsearch.fit(counts_train, labels_train)

dt_gridsearch = GridSearchCV(dt_clf, dt_pgrid, cv=5, n_jobs=-1)
dt_gs = dt_gridsearch.fit(counts_train, labels_train)

knn_gridsearch = GridSearchCV(knn_clf, knn_pgrid, cv=5, n_jobs=-1)
knn_gs = knn_gridsearch.fit(counts_train, labels_train)

rf_gridsearch = GridSearchCV(rf_clf, rf_pgrid, cv=5, n_jobs=-1)
rf_gs = rf_gridsearch.fit(counts_train, labels_train)\

svm_gridsearch = GridSearchCV(svm_clf, svm_pgrid, cv=5, n_jobs=-1)
svm_gs = svm_gridsearch.fit(counts_train, labels_train)

# *** Initialize Predictors for VotingClassifier with Optimized Estimators from GridSearchCV
predictors = [('lr_clf_optimized', lr_gs.best_estimator_),
            ('dt_clf_optimized', dt_gs.best_estimator_),
            ('knn_clf_optimized', knn_gs.best_estimator_),
            ('rf_clf_optimized', rf_gs.best_estimator_),
            ('svm_clf_optimized', svm_gs.best_estimator_)]

# *** Initialize and Fit VotingClassifier
VT = VotingClassifier(predictors)
VT.fit(counts_train,labels_train)

# *** Predict with VotingClassifier and Print Accuracy
predicted = VT.predict(counts_test)

print( accuracy_score(predicted,labels_test) )
# Multiple Runs result in different accuracies as high as 0.87667
