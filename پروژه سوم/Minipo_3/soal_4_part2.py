# -*- coding: utf-8 -*-
"""Soal_4_Part2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f7FDbO37V1fetkCu0o3d5nMt265c4PcQ

## **🔸 Decision Tree (sklearn)**
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn import metrics

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=83)

# Create a decision tree classifier
# You can experiment with different hyperparameters, including pruning-related ones
# Example with max_depth as a pruning parameter
max_depth_values = [5 ,10]  # Replace with your desired values
for max_depth in max_depth_values:
    clf = DecisionTreeClassifier(max_depth=max_depth)

    # Train the model
    clf.fit(X_train, y_train)

    # Plot the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
    plt.title(f'Decision Tree - Max Depth: {max_depth}')
    plt.savefig(f'decision_tree_max_depth_{max_depth}.png')
    plt.show()

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn import metrics

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=83)

# Create a decision tree classifier
# You can experiment with different hyperparameters, including pruning-related ones
# Example with ccp_alpha as a pruning parameter
ccp_alpha_values = [0.0, 0.01, 0.02]  # Replace with your desired values
for ccp_alpha in ccp_alpha_values:
    clf = DecisionTreeClassifier(ccp_alpha=ccp_alpha)

    # Train the model
    clf.fit(X_train, y_train)

    # Plot the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
    plt.title(f'Decision Tree - ccp_alpha: {ccp_alpha}')
    plt.savefig(f'decision_tree_ccp_alpha_{ccp_alpha}.png')
    plt.show()

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn import metrics

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=83)

# Create a decision tree classifier
# You can experiment with different hyperparameters, including pruning-related ones
# Example with ccp_alpha as a pruning parameter
ccp_alpha_values = [0.5]  # Replace with your desired values
for ccp_alpha in ccp_alpha_values:
    clf = DecisionTreeClassifier(ccp_alpha=ccp_alpha)

    # Train the model
    clf.fit(X_train, y_train)

    # Plot the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
    plt.title(f'Decision Tree - ccp_alpha: {ccp_alpha}')
    plt.savefig(f'decision_tree_ccp_alpha_{ccp_alpha}.png')
    plt.show()

"""#### * Predict"""

# Analyze two samples from the test set
    sample1 = X_test[0]
    sample2 = X_test[1]

    # Make predictions for the samples
    prediction1 = clf.predict([sample1])[0]
    prediction2 = clf.predict([sample2])[0]

    # Display the results
    print(f"\nAnalysis for Decision Tree with max_depth={max_depth}:\n")

    # Sample 1
    print("Sample 1:")
    print("Features:", sample1)
    print("True Label:", y_test[0])
    print("Predicted Label:", prediction1)
    print("\n")

    # Sample 2
    print("Sample 2:")
    print("Features:", sample2)
    print("True Label:", y_test[1])
    print("Predicted Label:", prediction2)

# Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred)

    # Display the results
    print(f"\nAnalysis for Decision Tree with max_depth={max_depth}:\n")
    print("Accuracy:", accuracy)

# Set max_depth to 5
max_depth = 5

# Create a decision tree classifier
clf = DecisionTreeClassifier(max_depth=max_depth)

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)

# Display the results
print(f"\nAnalysis for Decision Tree with max_depth={max_depth}:\n")
print("Accuracy:", accuracy)