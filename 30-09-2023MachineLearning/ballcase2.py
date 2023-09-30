from sklearn import tree


def main():
    print("Ball classification case study")

    # Rough means 1 & Smooth means 0
    # Load the Data
    Ballfeatures = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [
        35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]
    Labels = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis",
              "Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket"]

    obj = tree.DecisionTreeClassifier()  # Decide the algorithm

    obj = obj.fit(Ballfeatures, Labels)  # Train the model

    print(obj.predict([[36, 1], [91, 0]]))  # Test the model


if __name__ == "__main__":
    main()
