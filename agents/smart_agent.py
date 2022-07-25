from .agent import Agent
from numpy.random import randint
class Smart_Agent(Agent):
 
    def __init__(self,order,levels):
        self.order = order
        
        self.MAX_LEVEL = levels
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
                score2 = self.evaluate(game_state,x,y,self.order,0,-1,self.MAX_LEVEL, turn)
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
        choice = valid2[randint(len(valid2),size=1)[0]]
        print("BEST CHOICE IS %d with score %d"%(choice,best_score2))
        return choice
    def evaluate(self,game_state,x,y,order,score,multiplier,level, turn):
        if turn == 42:
            return 0
        game_state[x][y]=order
        win,new_score = self.evaluate_board(game_state,order)
        
        if win:
            
            game_state[x][y]=0
            return -1*multiplier*new_score
        if level==0:
            game_state[x][y]=0
            return -1*multiplier*new_score
        xi=0
        valid=[]
        best_score=-300000000000000*multiplier
        for columns in game_state:
            if columns[0]==0:
                yi=self.make_move(game_state,xi,order)
                game_state[xi][yi]=order
                new_score = self.evaluate(game_state,xi,yi,order*(-1),score,multiplier*(-1),level-1, turn+1)
                
                game_state[xi][yi]=0
                if (new_score>best_score and multiplier==1) or (new_score<best_score and multiplier==-1):
                    valid = []
                    best_score = new_score
                    valid.append(xi)
                elif new_score==best_score:
                    valid.append(xi)
            xi+=1
        game_state[x][y]=0
        return best_score
    def evaluate_board(self,game_state, order):
        score = 0
        x = 0
        for column in game_state:
            y=0
            for row in column:
                if game_state[x][y]!=0:
                    win,new_score = self.evaluate_helper(game_state,x,y,game_state[x][y],game_state[x][y]==order)
                    if win:
                        return (True, new_score*order*game_state[x][y])
                    
                    score+= (new_score*order*(game_state[x][y]*1))
                y+=1
            x+=1
        return (False, score)
    def evaluate_helper(self,game_state,x,y,order,different):
        score=0
        
        if x==3:
            score+=6
        elif x==2 or x==4:
            score+=3
        elif x==1 or x==2:
            score+=1
        #downwards check:
        count = 0
        empties=0
        i = y

        while i<6:
            if game_state[x][i]!=order:
                if game_state[x][i]==0:
                    empties+=1
                break
            else:
                count+=1
            i+=1
        if count>=4:   
            return (True,300000000)
        elif count==3:
            if different and empties==1:
                return (True,300000000)
            score+=33
        elif count==2:
            score+=1
        
        
        #Sideways check:
        count = 0
        empties = 0
        i = x
        while i<7:
            if game_state[i][y]!=order:
                if game_state[i][y]==0:
                    empties+=1
                break
            else:
                count+=1
            i+=1
        i = x-1
        while i>=0:
            if game_state[i][y]!=order:
                if game_state[i][y]==0:
                    empties+=1
                break
            else:
                count+=1
            i-=1
        if count>=4:   
            return (True,300000000)
        elif count==3 and empties==2:
            if different:
                score+=3
            score+=100
        elif count==3 and empties ==1:
            if different:
                score+=1
            score+=33
        elif count==3 and empties==0:
            score+=0
        elif count==2 and empties ==2:
            score+=2
        elif count==2 and empties ==1:
            score+=1

        #Bottom-left to Top-right check:
        count = 0
        empties=0
        i = x
        j = y
        while i<7 and j<6:
            if game_state[i][j]!=order:
                if game_state[i][j]==0:
                    empties+=1
                break
            else:
                count+=1
            i+=1
            j+=1
        i = x-1
        j = y-1
        while i>=0 and j>=0:
            if game_state[i][j]!=order:
                if game_state[i][j]==0:
                    empties+=1
                break
            else:
                count+=1
            i-=1
            j-=1
        
        if count>=4:   
            return (True,300000000)
        elif count==3 and empties==2:
            if different:
                score+=3
            score+=100
        elif count==3 and empties ==1:
            if different:
                score+=1
            score+=33
        elif count==3 and empties==0:
            score+=0
        elif count==2 and empties ==2:
            score+=2
        elif count==2 and empties ==1:
            score+=1
        
        #Top-left to bottom-right check:
        count = 0
        empties=0
        i = x
        j = y
        while i<7 and j>=0:
            if game_state[i][j]!=order:
                if game_state[i][j]==0:
                    empties+=1
                break
            else:
                count+=1
            i+=1
            j-=1
        i = x-1
        j = y+1
        while i>=0 and j<6:
            if game_state[i][j]!=order:
                if game_state[i][j]==0:
                    empties+=1
                break
            else:
                count+=1
            i-=1
            j+=1
        if count>=4:   
            return (True,300000000)
        elif count==3 and empties==2:
            if different:
                score+=3
            score+=100
        elif count==3 and empties ==1:
            if different:
                score+=1
            score+=33
        elif count==3 and empties==0:
            score+=0
        elif count==2 and empties ==2:
            score+=2
        elif count==2 and empties ==1:
            score+=1
        return (False,score)
        
        
        
    def introduce(self):
        return "SMART AGENT"