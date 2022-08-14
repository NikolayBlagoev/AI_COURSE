import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

import matplotlib.pyplot as plt

df = pd.read_csv('connect-4.csv')
df = df.dropna()
label  = df["winner"]
X  = df.drop("winner", axis = 1)

X_train, X_test, label_train, label_test = train_test_split(X, label, test_size = 0.2, random_state = 42)

model = RandomForestClassifier(n_estimators = 150, max_depth = 49, random_state = 7,min_samples_leaf=1)

model.fit(X_train, label_train)

label_pred = model.predict(X_test)
print("SCORE: %f"%(accuracy_score(label_pred,label_test)))
plot_confusion_matrix(model, X_test, label_test, display_labels =["-1", "0", "1"] )
plt.show()
dump(model, 'RFCLASSIFIER.joblib') 
