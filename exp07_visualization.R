# EXP NO 07 - Data Visualization (R)
# Data Analysis and Visualization (DAV)
#
# Demonstrates data visualization using:
# - ggplot2: bar plot, scatter plot, boxplot
# - Base R: barplot, pie chart
#
# Install required packages if not already installed:
# install.packages("ggplot2")

library(ggplot2)

# --- Dataset 1: Category Values ---
data <- data.frame(
  category = c('A', 'B', 'C', 'D', 'E'),
  value    = c(10, 25, 15, 30, 20)
)

# ggplot2 Bar Chart
ggplot(data, aes(x = category, y = value, fill = category)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  ggtitle("ggplot2 Bar Chart")

# --- Dataset 2: Students ---
students <- data.frame(
  Name  = c("A", "B", "C", "D", "E"),
  Marks = c(78, 85, 90, 67, 88),
  Age   = c(18, 19, 18, 20, 19)
)

# Base R Bar Plot
barplot(students$Marks,
        names.arg = students$Name,
        col       = "skyblue",
        main      = "Student Marks",
        xlab      = "Student",
        ylab      = "Marks")

# Base R Pie Chart
pie(students$Marks,
    labels = students$Name,
    main   = "Pie Chart - Marks Distribution")

# ggplot2 Scatter Plot
ggplot(students, aes(x = Age, y = Marks)) +
  geom_point(size = 4, color = "purple") +
  ggtitle("Scatter Plot - Age vs Marks") +
  theme_minimal()

# ggplot2 Box Plot
ggplot(students, aes(y = Marks)) +
  geom_boxplot(fill = "lightgreen") +
  ggtitle("Box Plot - Marks") +
  theme_minimal()
