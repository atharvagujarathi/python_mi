# Required Python packages
# ########################
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# File Paths
############
input_path = 'Case Studies/Breast Cancer Random Forest/breast-cancer-wisconsin (1).data'
output_path = 'Case Studies/Breast Cancer Random Forest/breast-cancer-wisconsin (1).csv'

# Headers
#########

Headers = ["Codenumber", "ClumpThickness", "UniformalityCellSize", "UniformalityCellShape", "MarginatAdhesion", "SingleEpitheticalCellSize", "BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses", "CancerType"]


##############################################
# Function Name: read_data
# Description: Read the data into pandas dataframe
# Input: path of CSV file
# Output: Gives the data
# Author: Atharva Gujarathi
# Date: 14/12/2023

def read_data(path):
    data = pd.read_csv(path)
    return data

################################################
# Function Name: get_headers
# Description: Dataset headers
# Input: dataset
# Output: returns the header
# Author: Atharva Gujarathi
# Date: 14/12/2023

def get_headers(dataset):
    return dataset.columns.values

#################################################
# Function Name: add_headers
# Description: Add the headers to the dataset
# Input: dataset
# Output: update the dataset
# Author: Atharva Gujarathi
# Date: 14/12/2023
def add_headers(dataset, headers):
    dataset.columns = headers
    return dataset

#################################################
# Function Name: data_file_into_csv
# Description: Nothing
# Input: Write the data to csv
# Output: update the dataset
# Author: Atharva Gujarathi
# Date: 14/12/2023
def data_file_into_csv():
    Headers = ["Codenumber", "ClumpThickness", "UniformalityCellSize", "UniformalityCellShape", "MarginatAdhesion", "SingleEpitheticalCellSize", "BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses", "CancerType"]
    # Load the dataset into pandas dataframe
    dataset = read_data(input_path)
    # Add the headers to the loadded dataset
    dataset = add_headers(dataset, Headers)
    # Save the loaded dataset into csv format
    dataset.to_csv(output_path, index=False)
    print("File saved...!")

#################################################
# Function Name: Split_dataset
# Description: split the dataset with train percentage
# Input: dataset with related information
# Output: Dataset after splitting
# Author: Atharva Gujarathi
# Date: 14/12/2023
def Split_dataset(dataset, train_percentage, feature_headers, target_header):
    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header], train_size=train_percentage)
    return train_x, train_y, test_x, test_y

#################################################
# Function Name: handle_missing_value
# Description: Filter missing values from the dataset
# Input: Dataset with missing values
# Output: Dataset by remocing missing values
# Author: Atharva Gujarathi
# Date: 14/12/2023

def handle_missing_value(dataset, missing_values_header, missing_label):
    return dataset[dataset[missing_values_header] != missing_label]

#################################################
# Function Name: random_forest_classifier
# Description: To train the random forest classifier with features and target data
# Author: Atharva Gujarathi
# Date: 16/12/2023
def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

#################################################
# Function Name: dataset_statistics
# Description: Basic statistics of the dataset
# Input: Dataset
# Output: Description of Dataset
# Author: Atharva Gujarathi
# Date: 16/12/2023

def dataset_statistics(dataset):
    print(dataset.describe())

#################################################
# Function Name: main
# Description: main function from where execution starts
# Author: Atharva Gujarathi
# Date: 16/12/2023
    
def main():
    # Load the csv file into pandas dataframe
    dataset = pd.read_csv(output_path)
    # Get basic statistics of the loaded dataset
    dataset_statistics(dataset)

    # Filter missing values
    # dataset = handle_missing_value(dataset, Headers[6], '?')
    dataset = handle_missing_value(dataset, Headers[6], '?')

    train_x, train_y, test_x, test_y = Split_dataset(dataset, 0.7, Headers[1:-1], Headers[-1])

    # Train and test dataset size details
    print("Train_x shape ::", train_x.shape)
    print("Train_y shape ::", train_y.shape)
    print("Test_x shape ::", test_x.shape)
    print("Test_y shape ::", test_y.shape)

    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y)
    print("Trained model ::", trained_model)
    predictions = trained_model.predict(test_x)

    for i in range(0, 205):
        print("Actual Outcome :: {} and Predicted Outcome :: {}".format(list(test_y)[i], predictions[i]))
    print("Train Accuracy ::", accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy ::", accuracy_score(test_y, predictions))
    print("Confusion Matrix", confusion_matrix(test_y, predictions))

#################################################
# application starter
if __name__ == "__main__":
    main()