# -*- coding: utf8 -*-
from sklearn import preprocessing, grid_search, svm
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


data = 'vectors.txt'

def get_data(txt):
    d = open(txt, 'r', encoding='utf-8')
    arr = []
    for line in d:
        line = line.split(';')
        arr.append(line[:-1])
    d.close()
    return arr

t = 0
src = []
trg = []

src0 = []
trg0 = []
src1 = []
trg1 = []

for q in get_data(data):
    if q[-1] == '1':
        src1.append(q[:-1])
        trg1.append(q[-1])
    else:
        src0.append(q[:-1])
        trg0.append(q[-1])


    src.append(q[:-1])
    trg.append(q[-1])
#print(len(src), len(trg))

#norm_src = preprocessing.normalize(src)
standart_src = preprocessing.scale(src)

model = ExtraTreesClassifier()
model.fit(standart_src, trg)
# display the relative importance of each attribute
print('importance of each attribute')
print(model.feature_importances_)
print('________________________')

model1 = LogisticRegression()
model1.fit(standart_src, trg)
print(model1)
# make predictions
expected = trg
predicted = model1.predict(standart_src)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

model2 = GaussianNB()
model2.fit(standart_src, trg)
print(model2)
# make predictions
expected = trg
predicted = model2.predict(standart_src)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

# fit a k-nearest neighbor model to the data
model3 = KNeighborsClassifier()
model3.fit(standart_src, trg)
print(model3)
# make predictions
expected = trg
predicted = model3.predict(standart_src)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

# fit a CART model to the data
model4 = DecisionTreeClassifier()
model4.fit(standart_src, trg)
print(model4)
# make predictions
expected = trg
predicted = model4.predict(standart_src)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')

'''
# fit a SVM model to the data
model5 = SVC()
model5.fit(standart_src, trg)
print(model5)
# make predictions
expected = trg
predicted = model5.predict(standart_src)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print('________________________')
'''

parameters = {'C': (0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)
first_3out4_src = src0[:23000]+src1[:1500]
first_3out4_src_st = preprocessing.scale(first_3out4_src)
first_3out4_trg = trg0[:23000]+trg1[:1500]
first_3out4_trg_st = preprocessing.scale(first_3out4_trg)
gs.fit(first_3out4_src_st, first_3out4_trg)
print(gs.best_score_)
print(gs.grid_scores_)

last_4out4_src = src0[23000:]+src1[1500:]
last_4out4_src_st = preprocessing.scale(last_4out4_src)
last_4out4_trg = trg0[23000:]+trg1[1500:]
clf = svm.SVC(kernel='linear', C=0.1).fit(first_3out4_src_st, first_3out4_trg)
print('score')
print(clf.score(last_4out4_src_st, last_4out4_trg),'-   SVM score')






