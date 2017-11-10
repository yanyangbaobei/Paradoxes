from random import choice
class MontyHall(object):
    def __init__(self, T):
        self.T = T
        self.stay = []
        self.switch = []
    
    def OneSimulation(self):
        car = choice([1, 2, 3])
        mychoice = choice([1, 2, 3])
        if car == mychoice:
            self.stay.append(1)
            # I will loose the chance to win no matter what host do
            self.switch.append(0)
        else:
            self.stay.append(0)
            # host need to reveal the goat door
            self.switch.append(1)

    def Simulation(self):
        for i in range(self.T):
            self.OneSimulation()
        staywin = sum(self.stay) / len(self.stay)
        switchwin = sum(self.switch) / len(self.switch)
        return (staywin, switchwin)