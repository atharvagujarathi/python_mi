from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class marvellousknnn():

    def fit(self, trainingData, trainingTarget):
        self.trainingData = trainingData
        self.trainingTarget = trainingTarget

    def predict(self, testData):
        predictions = []
        for row in testData:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    
    def closest(self, row):
        bestDistance = euc(row, self.trainingData[0])
        bestIndex = 0
        for i in range(1, len(self.trainingData)):
            dist = euc(row, self.trainingData[i])
            if dist < bestDistance:
                bestDistance = dist
                bestIndex = i
        return self.trainingTarget[bestIndex]
    
def MarvellousKNeighbor():
    border = "-"*50

    iris = load_iris()

    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID: %d, Label: %s, Feature: %s" % (i, iris.data[i], iris.target[i]))
    print("Size of Actual Data Set %d" %(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    print(border)
    print("Training data set")
    print(border)
    for i in range(len(data_test)):
        print("ID: %d, Label: %s, Feature: %s" % (i, data_test[i], target_test[i]))
    print("Size od test data set %d" %(i+1))
    print(border)

    classifier = marvellousknnn()

    classifier.fit(data_train, target_train)
    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy
    
def main():

    Accuracy = MarvellousKNeighbor()
    print("Accuracy is", Accuracy*100, "%")

if __name__ == "__main__":
    main()     