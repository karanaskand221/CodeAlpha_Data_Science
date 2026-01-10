# CodeAlpha_Data_Science


Iris Flower Classification GitHub README

CodeAlpha Iris Flower Classification
This project fulfills Task 1 from the CodeAlpha Data Science Internship: building a machine learning model to classify Iris flower species (setosa, versicolor, virginica) using sepal and petal measurements.
​

Project Overview
The Iris dataset contains features like sepal length, sepal width, petal length, and petal width to predict one of three species. A classification model is trained with Scikit-learn, evaluated for accuracy on test data, demonstrating core ML concepts like data preprocessing and model performance metrics.
​

Technologies Used
Python

Scikit-learn (for dataset loading, model training, evaluation)

Pandas (data manipulation)

Matplotlib/Seaborn (visualizations)

Steps to Run
Clone the repository: git clone https://github.com/yourusername/CodeAlphaIrisFlowerClassification.git

Install dependencies: pip install -r requirements.txt

Run the main script: python iris_classification.py

View the Jupyter notebook: jupyter notebook Iris_Classification.ipynb

Dataset
Download from the official source via Scikit-learn or the provided link in instructions: www.codealpha.tech. The dataset includes 150 samples with 4 features and 1 target label.
​

Model and Results
Model: Logistic Regression / Random Forest / SVM (choose based on best performance)

Preprocessing: Train-test split (80/20), feature scaling if needed

Accuracy: Achieved ~95-98% on test set (update with your results)

Visualizations include species scatter plots and confusion matrix.

Example code snippet for training:

python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
Insights
This task introduces binary/multiclass classification, highlighting how simple features yield high accuracy in well-separated data.
​

Author
Karan Askand, Computer Engineering Student, Sandip Institute of Technology and Research
