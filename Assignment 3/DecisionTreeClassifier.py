from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


class DecisionTree:

    def __init__(self, criterion, split):
        self.decisionTree = DecisionTreeClassifier(criterion=criterion, splitter=split)

    def train_and_predict(self, X_train, X_test, y_train, y_test):
        self.decisionTree.fit(X_train, y_train)
        y_prediction = self.decisionTree.predict(X_test)
        score = self.decisionTree.score(X_test, y_test)
        accuracy = accuracy_score(y_test, y_prediction)
        confusionMatrix = confusion_matrix(y_test, y_prediction)

        report = metrics.classification_report(y_test, y_prediction)

        return score, accuracy, confusionMatrix, report

    def validation_part(self, valData, valLabels):
        y_prediction = self.decisionTree.predict(valData)
        accuracy = accuracy_score(valLabels, y_prediction)
        confusionMatrix = confusion_matrix(valLabels, y_prediction)
        report = metrics.classification_report(valLabels, y_prediction)

        return accuracy, confusionMatrix, report
