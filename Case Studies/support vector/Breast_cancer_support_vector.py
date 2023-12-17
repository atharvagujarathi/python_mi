from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def marvelloussvm():
    # Load dataset
    cancer = datasets.load_breast_cancer()

    # Print the name of 13 features
    print("Features of the cancer dataset: ", cancer.feature_names)

    # Print the label(malignant, benign)
    print("Labels are :", cancer.target_names)

    # shape of the dataset
    print("shape of the dataset is :", cancer.data.shape)

    # print the cancer data features (top 5 records)
    print("First 5 records are :", cancer.data[0:5])

    # Print the cancer labels
    # print("Target are", cancer.target)

    # Split the dataset into training set and test set
    train_x, test_x, train_y, test_y = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109)
    # train_x, test_x, train_y, test_y = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109)


    # Create the svm classifier
    clf = svm.SVC(kernel='linear')

    # Train the model using the training sets
    clf.fit(train_x, train_y)

    # predict the responsee for test dataset
    y_pred = clf.predict(test_x)

    # Model Accuracy: how often is the classifier correct?
    print("Accuracy of thr model is :", metrics.accuracy_score(test_y, y_pred)*100)

def main():
    print("Support Vector Machine")

    marvelloussvm()

if __name__ == "__main__":
    main()