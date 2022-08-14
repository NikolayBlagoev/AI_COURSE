from .agent import Agent
from numpy.random import randint
from joblib import load
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
class ML_Agent(Agent):
 
    def __init__(self,order):
        self.order = order
        self.model = load("/Classifiers/RFCLASSIFIER.joblib")
        self.MAX_LEVEL=1


    def make_move(self,game_state,choice,order):
        i = 0
        
        while i<6 and game_state[choice][i]==0:
            i=i+1
        
        return i-1

    def move(self, game_state, turn):
        valid = []
        
        best_score = -10000000000
        
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
                if score2>best_score:
                    valid = []
                    best_score = score2
                    valid.append(x)
                elif score2==best_score:
                    valid.append(x)
                
            x=x+1
        if len(valid)<1:
            return -1
        # print("BEST CHOICE IS %d with score %d"%(valid2[0],best_score2))
        # print(game_state)
        # print("======================")
        # randint(len(valid2),size=1)[0]]
        choice = valid[randint(len(valid),size=1)[0]]
        print("BEST CHOICE IS %d with score %d"%(choice,best_score))
        return choice
    
    def set_classifier(self, filename):
        self.model = load("/Classifiers/RFCLASSIFIER.joblib")
    
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
        out = self.model.predict(data_frame)
        if out == self.order:
            return 1000
        elif out == 0:
            return 0
        else:
            return -1000
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