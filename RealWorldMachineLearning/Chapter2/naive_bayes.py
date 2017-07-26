import numpy as np
import matplotlib.pyplo as plt
from sklearn.naive_bayes import GaussianNB

from LogisticRegression import plot_classifier

input_file = 'data_multivar.txt'

X = []
y = []
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = [float(x) for x in line.split(',')]
        X.append(data[:-1])
        y.append(data[-1])
        
X = np.array(X)
y = np.array(y)

classifier_gaussiannb = GaussianNB()
classifier_gaussiannb.fit(X, y)
y_pred = classifier_gaussiannb.predict(X)

# compute accuracy of the classifier
accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
print("Accuracy of the classifier = ", round(accuracy, 2),'%')

plot_classifier(classifier_gaussiannb, X, y)