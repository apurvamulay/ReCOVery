import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm, naive_bayes, tree, ensemble, neighbors, linear_model
from sklearn.metrics import classification_report

REPEAT_NUM = 100
data = pd.read_csv('../../dataset/recovery-news-data.csv', encoding='utf-8')
labels = data['reliability'].values
features = np.load("./rst-features.npy")
features = preprocessing.scale(features)


'''
Decision Tree
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable
for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = tree.DecisionTreeClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('=== Decision Tree ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))


'''
Naive Bayes
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable
for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = naive_bayes.GaussianNB()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('\n=== Naive Bayes ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))


'''
SVM
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable
for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = svm.SVC()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('\n=== SVM ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))

'''
Logistic Regression
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable
for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = linear_model.LogisticRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('\n=== Logistic Regression ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))


'''
KNN
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable

for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = neighbors.KNeighborsClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('\n=== K-Nearest Neighbors ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))


'''
Random Forest
'''
pres1, recs1, fs1 = [], [], []     # reliable
pres0, recs0, fs0 = [], [], []     # unreliable
for repeat in range(REPEAT_NUM):
    # Divide the overall dataset as training data and testing data (0.8:0.2)
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    model = ensemble.RandomForestClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    result = classification_report(y_test, y_pred, digits=4, output_dict=True, target_names=['Unreliable', 'Reliable'])

    pres1.append(result['Reliable']['precision'])
    recs1.append(result['Reliable']['recall'])
    fs1.append(result['Reliable']['f1-score'])

    pres0.append(result['Unreliable']['precision'])
    recs0.append(result['Unreliable']['recall'])
    fs0.append(result['Unreliable']['f1-score'])

# Print general performance
print('\n=== Random Forest ===')

print('-- Predicting reliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres1)), np.std(np.array(pres1))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs1)), np.std(np.array(recs1))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs1)), np.std(np.array(fs1))))

print('-- Predicting unreliable news ---')
print('Precision: %.3f (std: %.3f)' %(np.mean(np.array(pres0)), np.std(np.array(pres0))))
print('Recall: %.3f (std: %.3f)' %(np.mean(np.array(recs0)), np.std(np.array(recs0))))
print('F1 score: %.3f (std: %.3f)' %(np.mean(np.array(fs0)), np.std(np.array(fs0))))



