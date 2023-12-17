import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
    # Step 1: Load data
    file_id = "1KpPyPWaIDMff9l9_LAQS5ZrYJNk508C7"
    csv_url = f"https://drive.google.com/uc?id={file_id}"
    data = pd.read_csv(csv_url)

    print("First 5 entries from loaded dataset")
    print(data.head())
    # print(data)

    print("Number of passengers are " + str(len(data)))

    # step 2: Analyse data
    print("Survived or non-survived passengers")
    figure()
    target = "Survived"

    countplot(data=data, x=target).set_title("Survived and non survived passengers")
    show()


    print("Visualisation: Survived and non survived passengers based on Gender")
    figure()
    target="Survived"

    countplot(data=data, x=target, hue="Sex").set_title("Survived and non survived passengers based on Gender")
    show()


    print("Visualisation: Survived and non survived passengers based on the passenger class")
    figure()
    target = "Survived"

    countplot(data=data, x=target, hue="Pclass").set_title("Survived and non survived passengers based on the passenger class")
    show()

    print("Visualisation: Survived and non survived passengers based on Age")
    figure()
    data["Age"].plot.hist().set_title("Survived and non survived passengers bassed on Age")
    show()


    print("Visualisation: Survived and non survived passengers based on the Fare")
    figure()
    data["Fare"].plot.hist().set_title("Survived and non survived passengers bassed on Fare")
    show()

    





def main():
    TitanicLogistic()

if __name__ == "__main__":
    main()