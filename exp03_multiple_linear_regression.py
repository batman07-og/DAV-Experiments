"""
EXP NO 03 - Multiple Linear Regression with Visualization
Data Analysis and Visualization (DAV)

Demonstrates multiple linear regression with 2 features and various visualizations
including 3D scatter plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from mpl_toolkits.mplot3d import Axes3D


def main():
    # 1. Generate Sample Data
    np.random.seed(42)
    X1 = np.random.rand(100) * 10
    X2 = np.random.rand(100) * 5
    y = 3 * X1 + 2 * X2 + np.random.randn(100) * 2
    X = np.column_stack((X1, X2))

    # 2. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # 4. Evaluation
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("R2 Score:", r2_score(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

    # 5. Visualization: Actual vs Predicted
    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, color="blue", alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted")
    plt.grid(True)
    plt.show()

    # 6. Visualization: Feature vs Target
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(X1, y, alpha=0.6)
    plt.xlabel("X1")
    plt.ylabel("y")
    plt.title("X1 vs y")
    plt.subplot(1, 2, 2)
    plt.scatter(X2, y, alpha=0.6)
    plt.xlabel("X2")
    plt.ylabel("y")
    plt.title("X2 vs y")
    plt.tight_layout()
    plt.show()

    # 7. 3D Visualization
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(X1, X2, y, alpha=0.5)
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("y")
    ax.set_title("3D View of Multiple Linear Regression Data")
    plt.show()


if __name__ == "__main__":
    main()
