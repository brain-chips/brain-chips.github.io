# %%
# load data
from collections import Counter
import csv
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

namaFile = "/Volumes/MLJKT/BINUS/Group task/Thesis Colloquium/databersihindonesia.csv"
data = []
label = []
with open(namaFile, 'r', encoding='ISO-8859-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)  # skip header
    for row in reader:
        data.append(row[0])
        label.append(row[1])

print("jumlah data:{}".format(len(data)))
print(Counter(label))
print("=================================\n")

# %%
# random urutan dan split ke data training dan test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=123)

print("Data training:")
print(len(x_train))
print(Counter(y_train))
print("=================================\n")

print("Data testing:")
print(len(x_test))
print(Counter(y_test))
print("=================================\n")
# %%

#spot check algorithms
print("Spot Check Algorithms")
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
print("=================================\n")


#evaluate each model in turn
# results = []
# names = []
# for name, model in models:
#     kfold = model_selection.KFold(n_splits=10, random_state=123)
#     cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring )
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s : %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)
# print("=================================\n")

#CARA 1
# transform ke tfidf dan train dengan naive bayes
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# text_clf = Pipeline([('vect', CountVectorizer()),
#                      ('tfidf', TfidfTransformer()),
#                      ('clf', MultinomialNB())])
# text_clf.fit(x_train, y_train)
# # %%
#
# # hitung akurasi data test
# import numpy as np
#
# pred = text_clf.predict(x_test)
# akurasi = np.mean(pred == y_test)
# print("Akurasi: {}".format(akurasi))
#
# print("=================================\n")
#
# predictions = text_clf.predict(x_test)
# print(accuracy_score(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))

#CARA 2
print("Make Predictions on Validation Dataset")
print("NAIVE BAYES")
nb = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('NB', MultinomialNB())])
# nb = GaussianNB()
nb.fit(x_train, y_train)
predictions = nb.predict(x_test)
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
print("=================================\n")

# print("SVM")
# svm = Pipeline([('vect', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('SVM', SVC(gamma='auto') )])
# # nb = GaussianNB()
# # svm = SVC(gamma='auto')
# svm.fit(x_train, y_train)
# predictions = svm.predict(x_test)
# print(accuracy_score(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))
# print("=================================\n")
#
# print("Logistic Regression")
# lr = Pipeline([('vect', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('LR', LogisticRegression(solver='liblinear', multi_class='ovr') )])
#
# lr.fit(x_train, y_train)
# predictions = lr.predict(x_test)
# print(accuracy_score(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))
# print("=================================\n")
#
# print("KNeighborsClassifier")
# knn = Pipeline([('vect', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('KNN', KNeighborsClassifier() )])
#
# knn.fit(x_train, y_train)
# predictions = knn.predict(x_test)
# print(accuracy_score(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))
# print("=================================\n")
#
# print("Decision Tree")
# cart = Pipeline([('vect', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('CART', DecisionTreeClassifier() )])
#
# cart.fit(x_train, y_train)
# predictions = cart.predict(x_test)
# print(accuracy_score(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))
# print("=================================\n")