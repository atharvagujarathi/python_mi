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
    
    def