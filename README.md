# DAV Experiments 🧪

A collection of **Data Analysis and Visualization (DAV)** lab experiments implemented in Python (and R where applicable), originally from a Google Colab notebook.

---

## 📋 Experiment List

| File | Exp No | Topic |
|------|--------|-------|
| `exp01_simple_linear_regression.py` | EXP 01 | Simple Linear Regression (User Input) |
| `exp03_multiple_linear_regression.py` | EXP 03 | Multiple Linear Regression with 3D Visualization |
| `exp04_time_series_analysis.py` | EXP 04 | Time Series Analysis & ARIMA Forecasting |
| `exp05_arima_grid_search.py` | EXP 05 | ARIMA with Grid Search (Best p, d, q) |
| `exp06_sentiment_analysis.py` | EXP 06 | Interactive Sentiment Analysis (VADER/NLTK) |
| `exp07_visualization_python.py` | EXP 07 | Data Visualization using Matplotlib & Seaborn |
| `exp07_visualization.R` | EXP 07 | Data Visualization using ggplot2 & Base R |

---

## 🚀 Setup & Installation

### Python

```bash
pip install -r requirements.txt
```

### R (for EXP 07)

In R console:
```r
install.packages("ggplot2")
```

---

## ▶️ Running the Experiments

```bash
# EXP 01 – Simple Linear Regression
python exp01_simple_linear_regression.py

# EXP 03 – Multiple Linear Regression
python exp03_multiple_linear_regression.py

# EXP 04 – Time Series Analysis
python exp04_time_series_analysis.py

# EXP 05 – ARIMA Grid Search
python exp05_arima_grid_search.py

# EXP 06 – Sentiment Analysis (interactive)
python exp06_sentiment_analysis.py

# EXP 07 – Python Visualization
python exp07_visualization_python.py

# EXP 07 – R Visualization (run in RStudio or Rscript)
Rscript exp07_visualization.R
```

---

## 📦 Libraries Used

**Python:**
- `numpy`, `pandas` — data manipulation
- `matplotlib`, `seaborn` — visualization
- `scikit-learn` — machine learning models
- `statsmodels` — time series analysis (ARIMA, ADF)
- `nltk` — natural language processing (VADER sentiment)

**R:**
- `ggplot2` — data visualization
- Base R graphics

---

## 📁 Project Structure

```
DAV-Experiments/
├── exp01_simple_linear_regression.py
├── exp03_multiple_linear_regression.py
├── exp04_time_series_analysis.py
├── exp05_arima_grid_search.py
├── exp06_sentiment_analysis.py
├── exp07_visualization_python.py
├── exp07_visualization.R
├── requirements.txt
└── README.md
```
