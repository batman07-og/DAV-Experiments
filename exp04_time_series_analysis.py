"""
EXP NO 04 - Time Series Analysis
Data Analysis and Visualization (DAV)

Demonstrates time series analysis including seasonal decomposition,
stationarity test (ADF), and ARIMA forecasting.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA


def main():
    # Create dummy data.csv
    data = {
        'date': pd.to_datetime(pd.date_range(start='2020-01-01', periods=60, freq='MS')),
        'value': np.random.randint(100, 200, size=60) + np.sin(np.arange(60) / 3) * 20
    }
    dummy_df = pd.DataFrame(data)
    dummy_df.to_csv('data.csv', index=False)
    print("data.csv created successfully.")

    # Load and preprocess
    df = pd.read_csv("data.csv")
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Visualize
    plt.figure(figsize=(10, 5))
    plt.plot(df, label="Time Series")
    plt.title("Time Series Plot")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.show()

    # Decomposition
    decomposition = seasonal_decompose(df['value'], model='additive', period=12)
    decomposition.plot()
    plt.show()

    # Stationarity Test
    result = adfuller(df['value'])
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    if result[1] < 0.05:
        print("Series is stationary")
    else:
        print("Series is NOT stationary")

    # ARIMA Model
    model = ARIMA(df['value'], order=(1, 1, 1))
    model_fit = model.fit()
    print(model_fit.summary())

    # Forecast
    forecast = model_fit.forecast(steps=12)
    plt.figure(figsize=(10, 5))
    plt.plot(df['value'], label="Original Data")
    plt.plot(forecast, label="Forecast", color='red')
    plt.legend()
    plt.title("Time Series Forecast")
    plt.show()


if __name__ == "__main__":
    main()
