"""
EXP NO 05 - ARIMA with Grid Search
Data Analysis and Visualization (DAV)

Demonstrates ARIMA modelling with automated hyperparameter tuning
via grid search over (p, d, q) combinations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.graphics.tsaplots import plot_acf, plot_pacf
import itertools
import warnings

warnings.filterwarnings("ignore")


def main():
    # 1. Create dataset
    data = [
        20, 21, 19, 23, 25, 24, 26, 27, 29, 30,
        28, 31, 33, 32, 35, 36, 37, 38, 40, 42,
        41, 43, 45, 46, 47, 49, 50, 52, 53, 55
    ]
    ts = pd.Series(data)

    # 2. Plot original data
    plt.figure(figsize=(8, 4))
    plt.plot(ts)
    plt.title("Original Time Series Data")
    plt.show()

    # 3. Check stationarity
    result = adfuller(ts)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])

    # 4. Differencing
    ts_diff = ts.diff().dropna()
    plt.figure(figsize=(8, 4))
    plt.plot(ts_diff)
    plt.title("Differenced Series")
    plt.show()

    # 5. ACF and PACF
    plot_acf(ts_diff)
    plt.show()
    plot_pacf(ts_diff)
    plt.show()

    # 6. Grid search for best (p, d, q)
    p = q = range(0, 3)
    d = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    best_aic, best_order, best_model = np.inf, None, None

    for order in pdq:
        try:
            model = ARIMA(ts, order=order)
            results = model.fit()
            if results.aic < best_aic:
                best_aic, best_order, best_model = results.aic, order, results
        except Exception:
            continue

    print("Best ARIMA Order:", best_order)

    # 7. Forecast
    forecast = best_model.forecast(steps=5)
    print("Forecast Values:\n", forecast)

    # 8. Plot results
    plt.figure(figsize=(8, 4))
    plt.plot(ts, label="Actual Data")
    plt.plot(range(len(ts), len(ts) + 5), forecast, label="Forecast", color="red")
    plt.title("ARIMA Forecast")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
