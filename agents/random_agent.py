from .agent import Agent
from numpy.random import randint
class Random_Agent(Agent):
 
    def __init__(self,order):
        self.order = order


    def move(self, game_state, turn):
        valid = []
        i=0
        for x in game_state:
            if x[0]==0:
                valid.append(i)
            i=i+1
        if len(valid)<1:
            return -1
        return valid[randint(len(valid),size=1)[0]]


    def introduce(self):
        return "RANDOM AGENT"