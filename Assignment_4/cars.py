# An example of how to implement Car as a class
class Car:
    # color = "blue"
    # make = "Toyota"
    # model = "Prius"
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        # default value for ALL instances of a class
        self.gas = 0

    def get_gas(self):
        self.gas += 10

    def check_gas(self):
        return print(self.gas)
    
def random_thing():
    print('random thing')