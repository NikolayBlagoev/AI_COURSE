
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('connect-4.csv')
df= df.dropna()
X = df.drop('winner', axis = 1)
y = df['winner']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.35,random_state=42)
def normalize(x):
     if x<0:
          return 2
     else:
          return x
y_train=y_train.map(lambda x:x+1)
y_test=y_test.map(lambda x:x+1)
print(y_train)
import tensorflow as tf
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
# model_1 = make_pipeline(StandardScaler(), SVC(gamma='auto'))
# model_1.fit(X_train, y_train)
# model_1 = RandomForestClassifier(max_depth=30, random_state=15)
# model_1.fit(X_train, y_train)
# clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(42),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=15)
test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)

print('\nTest accuracy:', test_acc)


# clf.predict_proba(X_test[:1])

# clf.predict(X_test[:5, :])

# print(clf.score(X_test, y_test))
# y_pred = model_1.predict(X_test)
# print(accuracy_score(y_test,y_pred))
from joblib import dump, load
dump(model, 'PREDICTOR3.joblib') 

