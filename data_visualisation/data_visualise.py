import numpy as np 
import pandas as pd
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt 

iris = pd.read_csv('iris.csv')

print(iris)
labels = iris["variety"]
features = iris.drop("variety", axis=1)
pd.plotting.parallel_coordinates(iris, "variety", color=['red','green','blue'])
plt.show()

bins = np.arange(0.6, 7.3, 0.3)
plt.hist(features["petal.length"], bins = bins)
plt.xticks(bins)
plt.show()
print(bins)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.4, random_state=23)
model = DecisionTreeClassifier(max_depth=5)
model.fit(features_train, labels_train)
labels_pred = model.predict(features_test)
print(accuracy_score(labels_pred, labels_test))
plot_tree(model, feature_names=["SP Length", "SP width", "PTL length", "PTL width"], class_names=["Setosa", "Versicolor", "Virginica"], filled = True)
plt.show()
plot_confusion_matrix(model, features_test, labels_test, display_labels =["Setosa", "Versicolor", "Virginica"] )
plt.show()