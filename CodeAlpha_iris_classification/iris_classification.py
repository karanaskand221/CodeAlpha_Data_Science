import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. LOAD DATA
# Load the dataset from the CSV file
df = pd.read_csv('Iris.csv')

# 2. PREPROCESSING
# Drop 'Id' as it's just an index and not a feature for prediction
# 'Species' is our target (y), everything else is a feature (X)
X = df.drop(['Id', 'Species'], axis=1)
y = df['Species']

# 3. TRAIN-TEST SPLIT
# We split the data: 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. MODEL BUILDING
# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model using the training data
model.fit(X_train, y_train)

# 5. PREDICTION AND EVALUATION
# Use the trained model to predict the species of the test data
y_pred = model.predict(X_test)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Overall Accuracy: {accuracy * 100:.2f}%")

# Detailed Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 6. VISUALIZING RESULTS (Confusion Matrix)
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Greens', 
            xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel('Predicted Species')
plt.ylabel('Actual Species')
plt.title('Iris Classification Confusion Matrix')
plt.show()