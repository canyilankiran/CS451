from NaïveBayesClassifier import NaiveBayes
from KNearestNeighbourClassifier import KNearest
from DecisionTreeClassifier import DecisionTree
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np
import pandas as pd

if __name__ == "__main__":
    print("------ Naive Bayes ------")
    digits = datasets.load_digits()
    data = digits.data.reshape((len(digits.data), -1))
    x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2, shuffle=False)
    x_train, valData, y_train, valLabels = train_test_split(x_train, y_train, test_size=0.1, shuffle=False)
    naiveBayes = NaiveBayes()
    score, accuracy, confusionMatrix, report = naiveBayes.train_and_predict(x_train, x_test, y_train, y_test)
    print("Train test for NaiveBayes")
    print("Score:" + str(score))
    print("Accuracy: " +str (accuracy))
    print(confusionMatrix)
    print(report)
    accuracyVal, confusionMatrixVal, reportVal = naiveBayes.validation_part(valData, valLabels)
    print(accuracyVal)
    print(confusionMatrixVal)
    print(reportVal)
    print("------ KNearest ------")
    highest_accuracies = []
    for k in range(1, 30, 2):
        kNear = KNearest(k)
        scoreForK, accuracyForK, confusionMatrixForK, reportForK = kNear.train_and_predict(x_train, x_test, y_train,
                                                                                         y_test, k)
        print("Train test for kNearest")
        print("K value: " + str(k))
        print(scoreForK)
        print(accuracyForK)
        print(confusionMatrixForK)
        print(reportForK)
        accuracyValForK, confusionMatrixValForK, reportValForK = naiveBayes.validation_part(valData, valLabels)
        print("Validate for kNearest")
        print(accuracyValForK)
        print(confusionMatrixForK)
        print(reportValForK)
        highest_accuracies.append(float(scoreForK))
    print("Highest accuaracy is " + str(float(np.argmax(highest_accuracies))))

    criterion_split = {}
    criterion_split["Criterion"] = ['gini', 'entropy']
    criterion_split["Split"] = ['random', 'best']

    print("------ DecisionTree ------")

    for criter in criterion_split["Criterion"]:
        for split in criterion_split["Split"]:
            print("Used criterion is " + criter + " and used split method is " + split)
            decisionT = DecisionTree(criter, split)
            scoreForT, accuracyForT, confusionMatrixForT, reportForT = decisionT.train_and_predict(x_train, x_test,
                                                                                                   y_train,
                                                                                                   y_test)
            print(scoreForT)
            print(accuracyForT)
            print(confusionMatrixForT)
            print(reportForT)
            accuracyValForT, confusionMatrixValForT, reportValForT = decisionT.validation_part(valData, valLabels)
            print(accuracyValForT)
            print(confusionMatrixForT)
            print(reportValForT)


