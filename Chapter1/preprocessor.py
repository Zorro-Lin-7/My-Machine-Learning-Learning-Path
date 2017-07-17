import numpy as np
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4],
                 [0, 4, -0.3, 2.1],
                 [1, 3.3, -1.9, -4.3]])

# mean removel
data_standardized = preprocessing.scale(data)
print('\nMean =', data_standardized.mean(axis=0))
print("\nStd deviation = ", data_standardized.std(axis=0))