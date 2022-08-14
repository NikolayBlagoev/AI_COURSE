
import numpy as np
import pandas as pd

# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
game_state = [0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
              0,0,0,-1,0,0,0,
              0,0,0,1,0,0,0]
game_state = [0,0,0,0,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0,
              1,-1,0,0,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0]

game_state2 = [1,-1,0,0,0,0,
              0,0,0,0,0,0,
              -1,0,0,0,0,0,
              1,-1,0,0,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0,
              1,0,0,0,0,0]

game = dict()
i=1
for x in game_state:
    if i<10:
        game.update({"pos_0"+str(i):x})
    else:
        game.update({"pos_"+str(i):x})
    i+=1

data_frame = pd.DataFrame(game,index=[0])

game2 = dict()
i=1
for x in game_state2:
    if i<10:
        game2.update({"pos_0"+str(i):x})
    else:
        game2.update({"pos_"+str(i):x})
    i+=1

data_frame2 = pd.DataFrame(game2,index=[0])



from joblib import load
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

model_1 = load("PREDICTOR.joblib")

out = model_1.predict(data_frame)
print(out)
out = model_1.predict(data_frame2)
print(out)

model_1 = load("PREDICTOR3.joblib")

out = model_1.predict(data_frame)
print(out)
out = model_1.predict(data_frame2)
print(out)




