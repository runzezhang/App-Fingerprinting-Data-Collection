import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.utils import resample
import random
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default="output.csv", type=str)
    result = parser.parse_args()
    print(result)

    # Read input file
    file_data = np.genfromtxt(result.input, delimiter=',', autostrip=True, dtype='unicode')
    file_data = file_data[1:, :]

    # Shuffle data
    random.shuffle(file_data)

    # Bootstrapping
    file_data = resample(file_data, n_samples=1000)

    # Get x and y
    x = file_data[:, 0:-1].astype(np.float)
    y = file_data[:, -1].astype(np.str)

    # Normalize input
    normalized_X = preprocessing.scale(x)

    # Round 1
    print("Round 1 - kernel='rbf', probability=True")

    clf = SVC(kernel='rbf', probability=True)
    scores = cross_val_score(clf, normalized_X, y, cv=10, scoring='accuracy')

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # Round 2
    print("Round 2 - kernel='sigmoid', probability=True")

    clf = SVC(kernel='sigmoid', probability=True)
    scores = cross_val_score(clf, normalized_X, y, cv=10, scoring='accuracy')

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # Round 3
    print("Round 3 - kernel='poly', probability=True, degree=3")

    clf = SVC(kernel='poly', probability=True, degree=3)
    scores = cross_val_score(clf, normalized_X, y, cv=10, scoring='accuracy')

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # Round 4
    print("Round 4 - kernel='poly', probability=True, degree=8")

    clf = SVC(kernel='poly', probability=True, degree=8)
    scores = cross_val_score(clf, normalized_X, y, cv=10, scoring='accuracy')

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # Round 5
    print("Round 5 - kernel='poly', C=10, probability=True, degree=8")

    clf = SVC(kernel='poly', C=10, probability=True, degree=8)
    scores = cross_val_score(clf, normalized_X, y, cv=10, scoring='accuracy')

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

if __name__ == "__main__":
    main()