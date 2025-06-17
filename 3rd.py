import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Download the dataset directly from the UCI repository
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wine = pd.read_csv(url, sep=';')

# Display first few rows
print(wine.head())

# Dataset information
print(wine.info())

# Check for null values
print(wine.isnull().sum())

# Statistical summary
print(wine.describe())

# Countplot of original quality scores
sns.countplot(x=wine['quality'])
plt.title("Original Quality Distribution")
plt.xlabel("Quality Score")
plt.ylabel("Count")
plt.show()

# Reclassify quality scores
bins = (2, 6.5, 8)
group_names = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=group_names)

# Show unique classes and value counts
print(wine['quality'].unique())
print(wine['quality'].value_counts())

# Countplot after classification
sns.countplot(x=wine['quality'])
plt.title("Reclassified Quality Distribution")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()

# Prepare data for training
X = wine.drop('quality', axis=1)
Y = wine['quality']

# Split into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)  # Use transform here to avoid data leakage
