import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def HeadBrainPredictor():

    # Load the Data:
    data = pd.read_csv(r"C:\Users\atharva.gujarathi\OneDrive - Reliance Corporate IT Park Limited\Desktop\python_mi\Case Studies\Head Brain Case Study\MarvellousHeadBrain (1).csv")

    print("The shape of the dataset", data.shape)

    x = data['Head Size(cm^3)'].values
    y = data["Brain Weight(grams)"].values

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    n = len(x)

    numerator = 0
    denomenator = 0

    # Equation of line is y = mx + c
    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denomenator += (x[i] -mean_x)**2

    m = numerator / denomenator

    c = mean_y - (m * mean_x)

    print("Slope of regression line is", m)
    print("Y intercept of regression line is", c)

    max_x = np.max(x) + 100
    min_x = np.min(x) - 100

    #Display plotting of above points
    x_x = np.linspace(min_x, max_x)

    y_y = m * x_x + c

    plt.plot(x_x, y_y, color='#58b970', label='Regression Line')
    plt.scatter(x, y, color='#ef5423', label='Scatter Plot')
    plt.xlabel("Head Size in cm3")
    plt.ylabel("Brain Weight in gm")

    plt.legend()
    plt.show()

    # Findout Goodness of fit i.e. R-square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * x[i]
        ss_t += (y[i] - mean_y) ** 2
        ss_r += (y[i] - y_pred) ** 2

    r2 = (1 - (ss_r/ss_t)) * 100
    print(r2)

def main():
    print("Supervised Machine Learning")
    print("Linear Regression on Head & Brain size data set")
    HeadBrainPredictor()

if __name__ == "__main__":
    main()
