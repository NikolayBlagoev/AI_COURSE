from .agent import Agent

class Human_Agent(Agent):
 
    def __init__(self,order):
        self.order = order


    def move(self, game_state, turn):
        choice = -1
        print(game_state)
        print("WHERE DO YOU WANT TO PUT YOUR DISK?")
        while(choice==-1):
            choice = input()
            try:
                choice=int(choice)
            except ValueError:
                print("INVALID CHOICE! TRY AGAIN! CANNOT PUT AT COLUMN %s"%choice)
                choice=-1
                continue
            if(choice<1 or choice>7):
                print("INVALID CHOICE! TRY AGAIN! CANNOT PUT AT COLUMN %d"%choice)
                choice=-1
                continue
            choice = choice-1
            if(game_state[choice][0]!=0):
                print("INVALID CHOICE! TRY AGAIN! CANNOT PUT AT COLUMN %d"%choice)
                choice=-1
                continue
        return choice
        


    def introduce(self):
        return "HUMAN AGENT"