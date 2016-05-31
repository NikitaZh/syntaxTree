# -*- coding: utf8 -*-
from sklearn import preprocessing, grid_search, svm
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import random


data = 'vectors.txt'


def get_data(txt):
    d = open(txt, 'r', encoding='utf-8')
    arr = []
    for line in d:
        line = line.split(';')
        arr.append(line[:-1])
    d.close()
    return arr
"""
sl = {}
for line in get_data(data):
    if line[17] not in sl:
        sl[line[17]] = 1
    else:
        sl[line[17]] += 1

for q in sl:
    print(q, ';', sl[q])

"""
t = 0
p = 0
src0 = []
trg0 = []
src1 = []
trg1 = []

for q in get_data(data):
    if q[-1] == '1':
        t += 1
        src1.append(q[:-1])
        trg1.append(q[-1])
    else:
        p += 1
        src0.append(q[:-1])
        trg0.append(q[-1])

print(t, '-количество положительных параметров')
print(p, '-количество отрицательных параметров')
random.shuffle(src0)
random.shuffle(src1)
src = src0[:3000] + src1[:1400]
trg = trg0[:3000] + trg1[:1400]
#src = src0 + src1
#trg = trg0 + trg1
#norm_src = preprocessing.normalize(src)
standart_src = preprocessing.scale(src)
expected = trg0[3000:4000] + trg1[1400:2072]
pred = src0[3000:4000] + src1[1400:2072]
pred = preprocessing.scale(pred)


model = ExtraTreesClassifier()
model.fit(standart_src, trg)
# display the relative importance of each attribute
print('importance of each attribute')
print(model.feature_importances_)
print('________________________')
"""
model1 = LogisticRegression()
model1.fit(standart_src, trg)
print(model1)
# make predictions
#expected = trg
predicted = model1.predict(pred)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

model2 = GaussianNB()
model2.fit(standart_src, trg)
print(model2)
# make predictions
#expected = trg
predicted = model2.predict(pred)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

# fit a k-nearest neighbor model to the data
model3 = KNeighborsClassifier()
model3.fit(standart_src, trg)
print(model3)
# make predictions
#expected = trg
predicted = model3.predict(pred)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

# fit a CART model to the data
model4 = DecisionTreeClassifier()
model4.fit(standart_src, trg)
print(model4)
# make predictions
#expected = trg
predicted = model4.predict(pred)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')
"""


# fit a SVM model to the data
model5 = SVC()
model5.fit(standart_src, trg)
print(model5)
# make predictions
#expected = trg
predicted = model5.predict(pred)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')



