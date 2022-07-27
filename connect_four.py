from cgi import print_directory
from agents import *
import numpy as np

def is_legal(game_state,choice):
    return not (choice<0 or choice>6 or game_state[choice][0]!=0)
def make_move(game_state,choice,order):
    i = 0
    while i<6 and game_state[choice][i]==0:
        i=i+1
    game_state[choice][i-1]=order
    return i-1
def is_win(game_state,x,y):
    order = game_state[x][y]
    print(x)
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
        print(25)
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
        print(45)
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
        print(69)
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
        print(93)
        return True
    return False

def main():
    game_state = np.zeros((7,6),dtype=np.int32)
    
    agent1 = ML_Agent(1,0,"Classifiers/RANDOMFOREST.joblib")
    agent2 = ML_Agent(-1,0,"Classifiers/RANDOMFOREST_COMBINED.joblib")
    # agent2 = Smart_Agent(-1,1)
    game_over = False
    turn =1
    
    # game_state[0]=[1, 1 , 1 , -1 ,-1, 1]
    # game_state[1]=[ 0 ,0, 0,  0,  0,  0]
    # game_state[2]=[ -1, 1,  1,  -1, 1,  -1]
    # game_state[3]=[ -1,1,  1, -1, 1,  1]
    # game_state[4]=[-1 , 1,-1 ,-1 ,1,-1]
    # game_state[5]=[ 0 , 0 , 0,  0, 0 ,0]
    # game_state[6]=[ 0  ,0 , 0 , 0,  0,  -1]
    # print(game_state)
    # print(agent2.move(game_state,33))
    # exit()
    while(not game_over):
        choice = agent1.move(np.copy(game_state),turn)
        if not is_legal(game_state,choice):
            print("A2 WINS due to illegal move. A1 tried to play %d "%choice)
            game_over=True
            break
        y = make_move(game_state,choice,agent1.order)
        if is_win(game_state,choice,y):
            print("A1 WINS")
            game_over=True
            break
        turn+=1
       
        choice = agent2.move(np.copy(game_state),turn)
        if not is_legal(game_state,choice):
            print("A1 WINS due to illega move. A2 tried to play %d "%choice)
            game_over=True
            break
        y = make_move(game_state,choice,agent2.order)
        if is_win(game_state,choice,y):
            print("A2 WINS")
            game_over=True
            break
   
        turn+=1
        if turn >=42:
            game_over=True
            print("DRAW")
            break
        # print(game_state)
        

        
    
    print(game_state)

if __name__=="__main__":
    main()