from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


class KNearest:

    def __init__(self, n_neighbors):
        self.kClass = KNeighborsClassifier(n_neighbors=n_neighbors)

    def train_and_predict(self, X_train, X_test, y_train, y_test, n_neighbors):
        self.kClass.fit(X_train, y_train)
        y_prediction = self.kClass.predict(X_test)
        score = self.kClass.score(X_test, y_test)
        accuracy = accuracy_score(y_test, y_prediction)
        confusionMatrix = confusion_matrix(y_test, y_prediction)
        report = metrics.classification_report(y_test, y_prediction)
        return score, accuracy, confusionMatrix, report

    def validation_part(self,valData,valLabels):
        y_prediction = self.kClass.predict(valData)
        accuracy = accuracy_score(valLabels, y_prediction)
        confusionMatrix = confusion_matrix(valLabels, y_prediction)
        report = metrics.classification_report(valLabels, y_prediction)

        return accuracy, confusionMatrix, report