"""
EXP NO 01 - Simple Linear Regression
Data Analysis and Visualization (DAV)

Demonstrates simple linear regression using user-provided data points.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def main():
    # 1. Get sample data from user input
    while True:
        try:
            num_entries = int(input("Enter the number of data entries (at least 2): "))
            if num_entries < 2:
                print("Number of entries must be at least 2 for linear regression. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    X_user = []
    y_user = []

    print("\nEnter X and Y values for each entry:")
    for i in range(num_entries):
        while True:
            try:
                x_val = float(input(f"Enter X value for entry {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                y_val = float(input(f"Enter Y value for entry {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        X_user.append([x_val])
        y_user.append([y_val])

    X = np.array(X_user)
    y = np.array(y_user)

    # 2. Create a Linear Regression model
    lin_reg = LinearRegression()

    # 3. Train the model
    lin_reg.fit(X, y)

    # 4. Make predictions for plotting the regression line
    min_x_val = X.min() - (X.max() - X.min()) * 0.1 if X.min() < X.max() else X.min() - 1
    max_x_val = X.max() + (X.max() - X.min()) * 0.1 if X.min() < X.max() else X.max() + 1
    X_new = np.array([[min_x_val], [max_x_val]])
    y_predict = lin_reg.predict(X_new)

    print("\nIntercept:", lin_reg.intercept_[0])
    print("Coefficient (slope):", lin_reg.coef_[0][0])
    print("\nPredicted line points for plotting:")
    for i, x_val in enumerate(X_new):
        print(f"X = {x_val[0]:.2f}, Predicted y = {y_predict[i][0]:.2f}")

    # 5. Plot the results
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, alpha=0.7, label='User Data')
    plt.plot(X_new, y_predict, "r-", linewidth=2, label='Linear Regression Line')
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Simple Linear Regression Example with User Data")
    plt.grid(True)
    plt.legend()
    plt.show()

    # 6. Show the equation
    print(f"\nThe linear regression equation is: y = {lin_reg.coef_[0][0]:.2f} * X + {lin_reg.intercept_[0]:.2f}")


if __name__ == "__main__":
    main()
