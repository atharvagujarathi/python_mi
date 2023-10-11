import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def playPredictor(csv_path):
    # First we have to give the path to the function
    data = pd.read_csv(csv_path, index_col=0)
    print("The size of the dataset is", len(data))

    featureName = ['Whether', 'Temperature']
    print("The name of the features are", featureName[0], "&", featureName[1])

    whether = data.Whether
    temp = data.Temperature
    play = data.Play

    encod = preprocessing.LabelEncoder()

    print(whether)
    whetherFeatureAfterEnoding = encod.fit_transform(whether)
    print(whetherFeatureAfterEnoding)

    print(temp)
    tempFeatureAfterEncoding = encod.fit_transform(temp)
    print(tempFeatureAfterEncoding)

    print(play)
    playLabelAfterEncoding = encod.fit_transform(play)
    print(playLabelAfterEncoding)

    features = list(zip(whetherFeatureAfterEnoding, tempFeatureAfterEncoding))
    
    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(features, playLabelAfterEncoding)

    test = model.predict([[0,2]])
    print(test)


def main():
    print("This is the playpredictor case study in PYTHON MACHINE LEARNING")
    playPredictor(r"C:\Users\athar\OneDrive\Desktop\Python Machine Learning\Assignments\Assignment No. 14\PlayPredictor.csv")

if __name__ == "__main__":
    main()