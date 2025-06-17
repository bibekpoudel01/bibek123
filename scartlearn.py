# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data: hours studied vs exam score
hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
scores = np.array([35, 45, 50, 60, 65, 75])

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(hours, scores, test_size=0.2, random_state=42)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Showing results
print("Predictions:", predictions)
print("Actual:", y_test)

# Plotting the regression line
plt.scatter(hours, scores, color='blue', label='Actual Data')
plt.plot(hours, model.predict(hours), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.show()
