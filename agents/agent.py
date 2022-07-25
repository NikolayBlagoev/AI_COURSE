from abc import ABC, abstractmethod
class Agent(ABC):
    
    def __init__(self,order):
        pass

    @abstractmethod
    def move(self, game_state, turn):
        pass

    @abstractmethod
    def introduce(self):
        pass