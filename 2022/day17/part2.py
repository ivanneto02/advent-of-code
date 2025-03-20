import numpy as np
from sklearn.linear_model import LinearRegression

def main():

    data = np.loadtxt("./output.txt", dtype=int)

    x = np.array(data[:, 0]).reshape(-1, 1)
    y = np.array(data[:, 1])

    print(x)
    print(y)

    print("Fitting, might take a while...")
    regression = LinearRegression(fit_intercept=True).fit(X=x, y=y)

    x = 1000000000000

    print(f"prediction for {x}:")
    pred = regression.predict([[x]])
    print(pred)

if __name__ == "__main__":
    main()
