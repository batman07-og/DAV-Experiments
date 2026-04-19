"""
EXP NO 07 - Data Visualization (Python)
Data Analysis and Visualization (DAV)

Demonstrates data visualization using Matplotlib and Seaborn:
- Bar Plot
- Pie Chart
- Scatter Plot
- Box Plot

Note: The R equivalent uses ggplot2 and base R graphics — see exp07_visualization.R
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    students = pd.DataFrame({
        'Name': ['A', 'B', 'C', 'D', 'E'],
        'Marks': [78, 85, 90, 67, 88],
        'Age': [18, 19, 18, 20, 19]
    })

    # Bar Plot
    plt.figure(figsize=(8, 4))
    plt.bar(students['Name'], students['Marks'], color='skyblue')
    plt.title("Bar Plot - Student Marks")
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.show()

    # Pie Chart
    plt.figure(figsize=(8, 4))
    plt.pie(students['Marks'], labels=students['Name'], autopct='%1.1f%%')
    plt.title("Pie Chart - Marks Distribution")
    plt.show()

    # Seaborn Scatter Plot
    plt.figure(figsize=(8, 4))
    sns.scatterplot(x='Age', y='Marks', data=students, s=100)
    plt.title("Scatter Plot - Age vs Marks")
    plt.show()

    # Seaborn Box Plot
    plt.figure(figsize=(8, 4))
    sns.boxplot(y='Marks', data=students)
    plt.title("Box Plot - Marks")
    plt.show()


if __name__ == "__main__":
    main()
