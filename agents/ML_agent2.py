from .agent import Agent

from joblib import load
import numpy as np
import pandas as pd
import tensorflow as tf
class ML_Agent2(Agent):
 
    def __init__(self,order,max_level,file_name):
        self.order = order
        self.model = tf.keras.Sequential([load(file_name), 
                                         tf.keras.layers.Softmax()])

        self.MAX_LEVEL=max_level


    def make_move(self,game_state,choice,order):
        i = 0
        
        while i<6 and game_state[choice][i]==0:
            i=i+1
        
        return i-1

    def move(self, game_state, turn):
        valid = []
        valid2 = []
        best_score = -10000000000
        best_score2 = -10000000000
        x=0
        for columns in game_state:
            if columns[0]==0:
                y=self.make_move(game_state,x,self.order)
                game_state[x][y]=self.order
                if self.is_win(game_state,x,y):
                    score2 = 100000
                else:
                    score2 = self.evaluate_board(game_state,self.order)
                    x2=0
                    for columns2 in game_state:
                        if columns2[0]==0:
                            y2 = self.make_move(game_state,x2,self.order*-1)
                            game_state[x2][y2]=self.order*-1
                            if self.is_win(game_state,x2,y2):
                                score2=-100000
                            game_state[x2][y2]=0
                        x2+=1
                    
                game_state[x][y]=0
                # print("MOVE: %d HAS SCORE: %d ORDER: %d"%(x,score2,self.order))
                if score2>best_score2:
                    valid2 = []
                    best_score2 = score2
                    valid2.append(x)
                elif score2==best_score2:
                    valid2.append(x)
                
            x=x+1
        if len(valid2)<1:
            return -1
        # print("BEST CHOICE IS %d with score %d"%(valid2[0],best_score2))
        # print(game_state)
        # print("======================")
        # randint(len(valid2),size=1)[0]]
        choice = valid2[np.random.randint(len(valid2),size=1)[0]]
        print("BEST CHOICE IS %d with score %d"%(choice,best_score2))
        return choice
  
    def evaluate_board(self,game_state, order):
        game_rep = []
        for row in game_state:
            y = 5
            while y>=0:
                game_rep.append(row[y])
                y-=1
        game = dict()
        i=1
        for x in game_rep:
            if i<10:
                game.update({"pos_0"+str(i):x})
            else:
                game.update({"pos_"+str(i):x})
            i+=1
        
        data_frame = pd.DataFrame(game,index=[0])
        
        out = np.argmax(self.model.predict(data_frame))-1
        return 1000 if out==order else -1000
    def is_win(self,game_state,x,y):
        order = game_state[x][y]
        
        #downwards check:
        count = 0
        i = y
        while i<6:
            if game_state[x][i]!=order:
                break
            else:
                count+=1
            i+=1
        if count>=4:
            
            return True
        
        #Sideways check:
        count = 0
        i = x
        while i<7:
            if game_state[i][y]!=order:
                break
            else:
                count+=1
            i+=1
        i = x-1
        while i>=0:
            if game_state[i][y]!=order:
                break
            else:
                count+=1
            i-=1
        if count>=4:
            
            return True

        #Top-left to bottom-right check:
        count = 0
        i = x
        j = y
        while i<7 and j<6:
            if game_state[i][j]!=order:
                break
            else:
                count+=1
            i+=1
            j+=1
        i = x-1
        j = y-1
        while i>=0 and j>=0:
            if game_state[i][j]!=order:
                break
            else:
                count+=1
            i-=1
            j-=1
        if count>=4:
            
            return True
        
        #Bottom-left to top-right check:
        count = 0
        i = x
        j = y
        while i<7 and j>=0:
            if game_state[i][j]!=order:
                break
            else:
                count+=1
            i+=1
            j-=1
        i = x-1
        j = y+1
        while i>=0 and j<6:
            if game_state[i][j]!=order:
                break
            else:
                count+=1
            i-=1
            j+=1
        if count>=4:
            
            return True
        return False
        
    
    def introduce(self):
        return "Machine Learning AGENT"