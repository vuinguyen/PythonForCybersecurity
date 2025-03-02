# Dog class with methods for dog actions

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def get_name(self):
        print(f"This dog's name is {self.name}")

    def get_age(self):
        print(f"{self.name} is {self.age} years old")
    
    def get_breed(self):
        print(f"{self.name} is a {self.breed}")

    def bark(self):
        print(f"{self.name} says woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball")

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")

    def go_on_walk(self):
        print(f"{self.name} is going on a walk") 
