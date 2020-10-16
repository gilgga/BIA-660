"""
* Name: classifier.py
* Description: BIA-660-WS Homework 4 - Classification
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score



# *** Read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')
        reviews.append(review.lower())
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')


# *** Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)


# *** Count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

# *** Train Different Classifiers

# ** Train Decision Tree Classifier ---------------------------------------------------
from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier()

# Train all classifier on the same datasets
dt_clf.fit(counts_train,labels_train)

# Use hard voting to predict (majority voting)
dt_pred = dt_clf.predict(counts_test)

# Print accuracy
print('Decision Tree Classifier Accuracy: ', accuracy_score(dt_pred,labels_test))


# ** Train Linear SVM Classifier ---------------------------------------------------
from sklearn.svm import LinearSVC
lsvc_clf = LinearSVC(random_state=0, tol=1e-5, dual=True, max_iter=10000)

lsvc_clf.fit(counts_train, labels_train)
lsvc_pred = lsvc_clf.predict(counts_test)

print('Linear SVM Classifier Accuracy: ', accuracy_score(lsvc_pred, labels_test))


from sklearn.linear_model import LogisticRegression
# ** Train Logistic Regression Classifier ---------------------------------------------------
lr_clf = LogisticRegression(max_iter=100000)

lr_clf.fit(counts_train, labels_train)
lr_pred = lr_clf.predict(counts_test)

print('Logistic Regression Classifier Accuracy: ', accuracy_score(lr_pred, labels_test))


# ** Train Multinomial Naive Bayes Classifier ---------------------------------------------------
from sklearn.naive_bayes import MultinomialNB
mnb_clf = MultinomialNB()

mnb_clf.fit(counts_train, labels_train)
mnb_pred = mnb_clf.predict(counts_test)

print('Multinomial Naive Bayes Classifier Accuracy: ', accuracy_score(mnb_pred, labels_test))


# ** Train Multilyer Perception Classifier ---------------------------------------------------
from sklearn.neural_network import MLPClassifier
mlp_clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

mlp_clf.fit(counts_train, labels_train)
mlp_pred = mlp_clf.predict(counts_test)

print('Multilyer Perception Classifier Accuracy: ', accuracy_score(mlp_pred, labels_test))


# ** Train K Nearest Neighbors Classifier
from sklearn.neighbors import KNeighborsClassifier

k_and_scores = []
for k in range(1,100):
    knn_clf = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)

    knn_clf.fit(counts_train, labels_train)
    knn_pred = knn_clf.predict(counts_test)

    k_and_scores.append((k, accuracy_score(knn_pred, labels_test)))

print('K Nearest Neighbors Classifier Accuracy: ', sorted(k_and_scores, key = lambda x : x[1], reverse=True)[0][1])

