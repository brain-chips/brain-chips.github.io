#https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
import fileinput
import csv
import pandas
from pandas.plotting import scatter_matrix
from pandas import DataFrame
import matplotlib.pyplot as plt
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
import spacy
from spacy.lang.id import Indonesian
import Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from collections import Counter

# #load dataset
url = "/Volumes/MLJKT/BINUS/Group task/Thesis Colloquium/10000testfrommain2.csv"
names = ['review']
dataset = pandas.read_csv(url, encoding="ISO-8859-1")
df = pandas.DataFrame()
#print(dataset['review'].head(5))

#lower case
dataset['review'] = dataset['review'].apply(lambda x: x.lower())
dataset['review'] = dataset['review'].str.replace('[^\w\s]','')
#print(dataset['review'].head(5))

StemFactory = StemmerFactory()
stemmer = StemFactory.create_stemmer()
StopFactory = StopWordRemoverFactory()
stopwords = StopFactory.get_stop_words()
stopwords.remove('ok')
# print(stopwords)

dataset['review'] = dataset['review'].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))
#print(dataset['review'].head(25))

dataset['review'] = dataset['review'].apply(lambda x: " ".join(stemmer.stem(x) for x in x.split()))
print(dataset['review'].head(25))

freq = pandas.Series(' '.join(dataset['review']).split()).value_counts()[:10]
print(freq)

# ====================
df = pandas.DataFrame(dataset['review'])#, dataset['class'])
df.to_csv('/Volumes/MLJKT/BINUS/Group task/Thesis Colloquium/hasiltestformmain2_5.csv', mode="a", header=False)