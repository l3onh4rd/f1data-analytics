from abc import ABC, abstractmethod

class Standings(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def generate_chart(self):
        pass