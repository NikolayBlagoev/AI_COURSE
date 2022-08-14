import numpy as np
import pandas as pd 
import tensorflow as tf
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

df = pd.read_csv('connect-4.csv')
df= df.dropna()
X = df.drop('winner', axis = 1)
y = df['winner']

X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.2,random_state=42)


# TRAIN SEQUENTIAL CLASSIFIER WITH KERAS
y_train=y_train.map(lambda x:x+1)
y_test=y_test.map(lambda x:x+1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(42),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(3)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=18)
test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)

print('Test accuracy:', test_acc)
print('Test Loss:', test_loss)

# clf.predict_proba(X_test[:1])

# clf.predict(X_test[:5, :])

# print(clf.score(X_test, y_test))
# y_pred = model_1.predict(X_test)
# print(accuracy_score(y_test,y_pred))
dump(model, 'SEQUENTIAL.joblib') 

