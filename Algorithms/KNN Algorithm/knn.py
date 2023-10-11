import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    # Step-1 : Load Data
    data = pd.read_csv(data_path, index_col=0)

    print("Size of Actual dataset", len(data))

    # Step-2: Clean, prepare & manipulate the data
    feature_names = ['Whether', 'Temperature']

    print("Names of features are ", feature_names)

    Whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # Creating LabelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers
    Whether_encoded = le.fit_transform(Whether) # 2-sunny, 0-overcast, 1-rainy
    print(Whether_encoded)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature) # 1-hot, 2-mild, 0-cool
    label = le.fit_transform(play) # 0-no, 1-yes
    print(temp_encoded)
    print(label)

    # combining whether and temp into single list of tuples
    features = list(zip(Whether_encoded, temp_encoded))
    print(features)
    # Step-3: Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features, label)

    # Test data
    predicted = model.predict([[0, 2]])  #0: overcast, 2:Mild
    print(predicted)

def main():
    # MarvellousPlayPredictor("C:\Users\athar\OneDrive\Desktop\Python Machine Learning\Algorithms\KNN Algorithm\PlayPredictor.csv")    
    MarvellousPlayPredictor(r"C:\Users\athar\OneDrive\Desktop\Python Machine Learning\Algorithms\KNN Algorithm\PlayPredictor.csv")

if __name__ == "__main__":
    main()
